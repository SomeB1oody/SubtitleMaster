
# Subtitle Master
*Various features of subtitle processing*
*多功能字幕处理工具*

---
## 0. Table of Content 目录

-  1. Intro 简介
-  2. Functions 功能
-  3. Required environment 要求环境
-  4. Contribution 贡献
-  5. Liscence 证书
-  6. Contact information 联系方式
---
## 1. Intro
**Subtitle Master** is a project that uses Python FFmpeg as its backend and Python wxWidgets as its frontend. It is designed to enable a range of subtitle processing operations through a simple and lightweight program.
**Subtitle Master** 是一个以 Python FFmpeg 作为后端、Python wxWidgets 作为前端的项目，旨在通过一个简单轻量的程序实现各种字幕处理操作。

Each program comes with both a non-GUI and a GUI version. The non-GUI version offers the simplest operations and code, making it easier to understand. The GUI version supports more complex operations, providing a more advanced and user-friendly experience.
每个程序都提供了 GUI 和非 GUI 版本。非 GUI 版本提供最简单的操作和代码，更易于理解；而 GUI 版本支持更复杂的操作，提供更先进且用户友好的体验。

Due to my limited capabilities, the code may have some imperfections. I warmly welcome everyone to share their suggestions and contribute to the project. For more details, please see the Contribution. Thank you for your understanding!
由于个人能力有限，代码可能存在一些不足，热烈欢迎大家分享建议并为项目做出贡献。详细信息请参考贡献方式。感谢您的理解！

---
## 2.Functions 功能

### 2.1. Structure 结构

This is the sturcture of this project:
以下是项目的结构：

![structure](https://github.com/user-attachments/assets/e6cb2cce-49eb-44f7-9a39-7c073f7a861b)


### 2.2. Info about SubtitleHarcoder

The function of **SubtitleHardcoder** is to embed hardcoded subtitles into a video when both the video and subtitle files are provided.
**SubtitleHardcoder** 的功能是将硬字幕嵌入到视频中，需要提供视频文件和字幕文件。

In **SubtitleHardcoder.py**, the program executes the operation by allowing the user to input the video path, subtitle path, and output path separately.
在 **SubtitleHardcoder.py** 中，程序通过允许用户分别输入视频路径、字幕路径和输出路径来完成操作。

In **SubtitleHardcoder(GUI).py**, users can use a graphical user interface (GUI) to process videos and subtitles individually or in batches. For batch processing, the video and subtitle files must have matching names to be correctly paired.
在 **SubtitleHardcoder(GUI).py** 中，用户可以通过图形用户界面（GUI）单独或批量处理视频和字幕文件。对于批量处理，视频和字幕文件必须具有匹配的名称才能正确配对。

### 2.3. Info about FormatTransformer

The function of **FormatTransformer** is to convert subtitle files between different formats.
**FormatTransformer** 的功能是将字幕文件在不同格式之间进行转换。

In **FormatTransformer.py**, the program performs the conversion based on the file path and target format provided by the user.
在 **FormatTransformer.py** 中，程序根据用户提供的文件路径和目标格式执行转换操作。

In **FormatTransformer(GUI).py**, users can use a graphical user interface (GUI) to convert subtitle file formats individually or in batches.
在 **FormatTransformer(GUI).py** 中，用户可以通过图形用户界面（GUI）单独或批量转换字幕文件格式。

---
## 3. Required environment 要求环境
- 1. Compile FFmpeg with libass, fontconfig, fribidi and harfbuzz support (install freetype first).
     编译支持 libass、fontconfig、fribidi、harfbuzz 的 FFmpeg（先下载freetype）。
- 2. Install wxWidgets (only for GUI-version files).
     安装 wxWidgets（仅用于 GUI 版本文件）。
```bash
pip install wxPython
```

---

## 4. Contribution 贡献

Contributions are welcome! Follow these steps:
欢迎贡献！请按照以下步骤操作：
 - 1. Fork project.
      Fork 项目。
 - 2. Create branch:
      创建分支：
 ```bash
 git checkout -b feature-name
```
- 3. Submit changes:
     提交更改：
```bash
git commit -m "Explain changes"
```
- 4. Push branch:
     推送分支：
```bash
git push orgin feature-name
```
- 5. Submit Pull Request.
     提交拉取请求。

---
## 5. License 证书

This project uses [MIT LICENSE](https://github.com/SomeB1oody/SubtitleMaster/blob/main/LICENSE).
本项目使用[MIT LICENSE](https://github.com/SomeB1oody/SubtitleMaster/blob/main/LICENSE)。

---
## 6. Contact information 联系方式

- Email: stanyin64@gmail.com
- GitHub: [@SomeB1ooody](https://github.com/SomeB1oody)
