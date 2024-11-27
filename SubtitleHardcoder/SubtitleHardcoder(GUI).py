import wx
import os
import subprocess

def add_subtitle_to_video(video_path, subtitle_path, output_path):
    video_name_with_ext = os.path.basename(video_path)
    _, ext = os.path.splitext(video_name_with_ext)
    if ext == '.ass':
        vf = f"ass='{subtitle_path}'"
    else:
        vf = f"subtitles='{subtitle_path}'"

    # 使用FFmpeg将字幕嵌入视频中
    command = [
        'ffmpeg',
        '-i', video_path,
        '-vf', vf,
        '-c:a', 'copy',
        f'{output_path}'
    ]

    try:
        subprocess.run(command, check=True)
        print("Subtitles were successfully added to the video!")
    except subprocess.CalledProcessError as e:
        raise ValueError(e)

def process_videos_and_subtitles(video_dir, subtitle_dir, output_dir):
    def is_supported_subtitle_file(file_name):
        #检查是否是支持的字幕文件
        supported_extensions = ['.srt', '.ass', '.ssa', '.sub']
        return any(file_name.endswith(ext) for ext in supported_extensions)

    for video_file in os.listdir(video_dir):
        video_name, video_ext = os.path.splitext(video_file)

        for subtitle_file in os.listdir(subtitle_dir):
            subtitle_name, subtitle_ext = os.path.splitext(subtitle_file)

            if video_name == subtitle_name and is_supported_subtitle_file(subtitle_file):
                video_path = os.path.join(video_dir, video_file)
                subtitle_path = os.path.join(subtitle_dir, subtitle_file)
                output_path = os.path.join(output_dir, video_name + "_with_subtitle" + video_ext)

                try:
                    print(f'Adding subtitle to {video_file}...')
                    add_subtitle_to_video(video_path, subtitle_path, output_path)
                except subprocess.CalledProcessError as e:
                    raise RuntimeError(e)

class SubtitleAdderWX(wx.Frame):
    def __init__(self, *args, **kw):
        super(SubtitleAdderWX, self).__init__(*args, **kw)

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

        # 输入视频路径和视频文件夹路径
        self.hbox = wx.BoxSizer(wx.HORIZONTAL)
        self.video_file_button = wx.Button(panel, label="Select video")
        self.Bind(wx.EVT_BUTTON, self.on_select_video, self.video_file_button)
        self.hbox.Add(self.video_file_button, flag=wx.ALL, border=5)

        self.video_folder_button = wx.Button(panel, label="Select video folder")
        self.Bind(wx.EVT_BUTTON, self.on_select_video_folder, self.video_folder_button)
        self.hbox.Add(self.video_folder_button, flag=wx.ALL, border=5)
        self.video_folder_button.Enable(False)

        self.input_path_text = wx.StaticText(
            panel, label="Click \"Select video\" or \"Select video folder\" first"
        )
        self.vbox.Add(self.hbox, flag=wx.EXPAND)
        self.vbox.Add(self.input_path_text, flag=wx.ALL, border=5)

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
            self.video_folder_button.Enable(False)
            self.video_file_button.Enable(True)
            self.subtitle_folder_button.Enable(False)
            self.subtitle_file_button.Enable(True)
        else:
            self.video_folder_button.Enable(True)
            self.video_file_button.Enable(False)
            self.subtitle_folder_button.Enable(True)
            self.subtitle_file_button.Enable(False)

    def on_select_video(self, event):
        with wx.FileDialog(None, "Select a video", wildcard="所有文件 (*.*)|*.*",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as dialog:
            if dialog.ShowModal() == wx.ID_OK:
                self.input_path_text.SetLabel(f"{dialog.GetPath()}")
                self.selected_video_file = dialog.GetPath()

    def on_select_video_folder(self, event):
        with wx.DirDialog(None, "Select a folder for videos", "",
                          style=wx.DD_DEFAULT_STYLE) as dialog:
            if dialog.ShowModal() == wx.ID_OK:
                self.input_path_text.SetLabel(f"{dialog.GetPath()}")
                self.selected_video_folder = dialog.GetPath()

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
        process_type = self.process_type.GetStringSelection()
        output_path = self.selected_folder

        if not output_path:
            wx.MessageBox("Please select an output folder first", "Error", wx.OK | wx.ICON_ERROR)
            return

        if process_type == 'Individual processing':
            video_path = self.selected_video_file
            subtitle_path = self.selected_subtitle_file

            if not video_path:
                wx.MessageBox("Please select a video file first", "Error", wx.OK | wx.ICON_ERROR)
                return
            if not subtitle_path:
                wx.MessageBox("Please select a subtitle file first", "Error", wx.OK | wx.ICON_ERROR)
                return

            video_name_with_ext = os.path.basename(video_path)
            file_name, ext = os.path.splitext(video_name_with_ext)
            output_path = output_path + file_name + '_with_subtitle' + ext
            try:
                add_subtitle_to_video(video_path, subtitle_path, output_path)
                wx.MessageBox(f"File saved at {output_path}", "Success", wx.OK | wx.ICON_INFORMATION)
            except ValueError as e:
                wx.MessageBox(str(e), "Error", wx.OK | wx.ICON_ERROR)
                return
        else:
            video_dir = self.selected_video_folder
            subtitle_dir = self.selected_subtitle_folder

            if not video_dir:
                wx.MessageBox("Please select a video folder first", "Error", wx.OK | wx.ICON_ERROR)
                return
            if not subtitle_dir:
                wx.MessageBox("Please select a subtitle folder first", "Error", wx.OK | wx.ICON_ERROR)
                return

            try:
                process_videos_and_subtitles(video_dir, subtitle_dir, output_path)
                wx.MessageBox(f"Files saved at {output_path}", "Success", wx.OK | wx.ICON_INFORMATION)
            except RuntimeError as e:
                wx.MessageBox(str(e), "Error", wx.OK | wx.ICON_ERROR)
                return

if __name__ == "__main__":
    app = wx.App()
    frame = SubtitleAdderWX(None)
    frame.SetTitle('Subtitle Adder with GUI')
    frame.SetSize((450, 325))
    frame.Show()
    app.MainLoop()
