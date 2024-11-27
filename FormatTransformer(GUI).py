import wx
import os
import subprocess

def convert_subtitle(input_path: str, desired_format: str, output_path: str):
    # 检查输入文件是否存在
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file {input_path} does not exist.")

    output_path = output_path + desired_format

    # 使用subprocess调用ffmpeg进行格式转换
    try:
        subprocess.run(
            ['ffmpeg', '-i', input_path, output_path],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        print(f"File has successfully saved as {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error during processing: {e.stderr.decode('utf-8')}")

def convert_subtitles_in_folder(input_folder: str, output_folder: str, desired_format: str):
    # 检查输入文件夹是否存在
    if not os.path.exists(input_folder):
        raise FileNotFoundError(f"Input folder {input_folder} does not exist.")

    # 检查输出文件夹是否存在，如果不存在则创建
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历输入文件夹中的所有文件
    for file_name in os.listdir(input_folder):
        input_path = os.path.join(input_folder, file_name)

        # 仅处理文件
        if os.path.isfile(input_path):
            convert_subtitle(input_path, desired_format, output_folder)

class SubtitleFormatTransformerWX(wx.Frame):
    def __init__(self, *args, **kw):
        super(SubtitleFormatTransformerWX, self).__init__(*args, **kw)

        panel = wx.Panel(self)
        self.vbox = wx.BoxSizer(wx.VERTICAL)

        # 选择覆盖模式
        self.process_type = wx.RadioBox(
            panel, label="", choices=[
                'Individual processing', 'Batch processing'
            ]
        )
        self.process_type.Bind(wx.EVT_RADIOBOX, self.on_process_type)
        self.vbox.Add(self.process_type, flag=wx.ALL, border=5)

        # 输入字幕路径和字幕文件夹路径
        self.hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        self.subtitle_file_button = wx.Button(panel, label="Select subtitle")
        self.Bind(wx.EVT_BUTTON, self.on_select_subtitle, self.subtitle_file_button)
        self.hbox2.Add(self.subtitle_file_button, flag=wx.ALL, border=5)

        self.subtitle_folder_button = wx.Button(panel, label="Select subtitle folder")
        self.Bind(wx.EVT_BUTTON, self.on_select_subtitle_folder, self.subtitle_folder_button)
        self.hbox2.Add(self.subtitle_folder_button, flag=wx.ALL, border=5)
        self.subtitle_folder_button.Enable(False)

        self.input_path_text_ = wx.StaticText(
            panel, label="Click \"Select subtitle\" or \"Select subtitle folder\" first"
        )
        self.vbox.Add(self.hbox2, flag=wx.EXPAND)
        self.vbox.Add(self.input_path_text_, flag=wx.ALL, border=5)

        # 选择输出格式
        self.desired_format = wx.RadioBox(
            panel, label="choose a desired format", choices=[
                '.srt', '.ass', '.ssa', '.sub'
            ]
        )
        self.vbox.Add(self.desired_format, flag=wx.ALL, border=5)

        # 输出路径
        self.hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        self.folder_button = wx.Button(panel, label="Select output folder")
        self.Bind(wx.EVT_BUTTON, self.on_select_folder, self.folder_button)
        self.hbox3.Add(self.folder_button, flag=wx.ALL, border=5)
        self.output_path_text = wx.StaticText(panel, label="Click \"Select output folder\" first")
        self.vbox.Add(self.hbox3, flag=wx.EXPAND)
        self.vbox.Add(self.output_path_text, flag=wx.ALL, border=5)

        # 处理按钮
        self.transform_button = wx.Button(panel, label="Process")
        self.transform_button.Bind(wx.EVT_BUTTON, self.on_transform)
        self.vbox.Add(self.transform_button, flag=wx.ALL, border=5)

        # 设置面板的布局管理器
        panel.SetSizer(self.vbox)
        panel.Layout()

    def on_process_type(self, event):
        choice = self.process_type.GetStringSelection()
        if choice == 'Individual processing':
            self.subtitle_folder_button.Enable(False)
            self.subtitle_file_button.Enable(True)
        else:
            self.subtitle_folder_button.Enable(True)
            self.subtitle_file_button.Enable(False)

    def on_select_subtitle(self, event):
        with wx.FileDialog(None, "Select a subtitle", wildcard="所有文件 (*.*)|*.*",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as dialog:
            if dialog.ShowModal() == wx.ID_OK:
                self.input_path_text_.SetLabel(f"{dialog.GetPath()}")
                self.selected_subtitle_file = dialog.GetPath()

    def on_select_subtitle_folder(self, event):
        with wx.DirDialog(None, "Select a folder for subtitles", "",
                          style=wx.DD_DEFAULT_STYLE) as dialog:
            if dialog.ShowModal() == wx.ID_OK:
                self.input_path_text_.SetLabel(f"{dialog.GetPath()}")
                self.selected_subtitle_folder = dialog.GetPath()

    def on_select_folder(self, event):
        with wx.DirDialog(None, "Select a folder for output", "",
                          style=wx.DD_DEFAULT_STYLE) as dialog:
            if dialog.ShowModal() == wx.ID_OK:
                self.output_path_text.SetLabel(f"{dialog.GetPath()}")
                self.selected_folder = dialog.GetPath()

    def on_transform(self, event):
        desired_format = self.desired_format.GetStringSelection()
        output_path = self.selected_folder
        process_type = self.process_type.GetStringSelection()

        if not output_path:
            wx.MessageBox("Please select an output folder first", "Error", wx.OK | wx.ICON_ERROR)
            return

        if process_type == 'Individual processing':
            subtitle_path = self.selected_subtitle_file

            if not subtitle_path:
                wx.MessageBox("Please select a subtitle file first", "Error", wx.OK | wx.ICON_ERROR)
                return

            try:
                # 获取文件名和扩展名
                video_name_with_ext = os.path.basename(subtitle_path)
                file_name, _ = os.path.splitext(video_name_with_ext)
                path = f'{output_path}/{file_name}'
                convert_subtitle(subtitle_path, desired_format, path)
                wx.MessageBox(f"File saved as {path}", "Success", wx.OK | wx.ICON_INFORMATION)
            except subprocess.CalledProcessError as e:
                wx.MessageBox(
                f"Error during processing: {e.stderr.decode('utf-8')}", "Error", wx.OK | wx.ICON_ERROR
                )
                return
        else:
            subtitle_folder = self.selected_subtitle_folder

            if not subtitle_folder:
                wx.MessageBox("Please select a subtitle folder first", "Error", wx.OK | wx.ICON_ERROR)
                return

            try:
                convert_subtitles_in_folder(subtitle_folder, output_path, desired_format)
                wx.MessageBox(f"Files saved in {output_path}", "Success", wx.OK | wx.ICON_INFORMATION)
            except subprocess.CalledProcessError as e:
                wx.MessageBox(
                f"Error during processing: {e.stderr.decode('utf-8')}", "Error", wx.OK | wx.ICON_ERROR
                )
                return

if __name__ == "__main__":
    app = wx.App()
    frame = SubtitleFormatTransformerWX(None)
    frame.SetTitle('Subtitle Format Transformer with GUI')
    frame.SetSize((450, 325))
    frame.Show()
    app.MainLoop()