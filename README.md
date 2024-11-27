
# Subtitle Master
*Various features of subtitle processing*

---
## 0. Table of Content

-  1. Intro
-  2. Functions
-  3. Required environment
-  4. Contribution
-  5. Liscence
-  6. Contact information
---
## 1. Intro
**Subtitle Master** is a project that uses Python FFmpeg as its backend and Python wxWidgets as its frontend. It is designed to enable a range of subtitle processing operations through a simple and lightweight program.

Each program comes with both a non-GUI and a GUI version. The non-GUI version offers the simplest operations and code, making it easier to understand. The GUI version supports more complex operations, providing a more advanced and user-friendly experience.

Due to my limited capabilities, the code may have some imperfections. I warmly welcome everyone to share their suggestions and contribute to the project. For more details, please see the Contribution. Thank you for your understanding!

---
## 2.Functions

### 2.1. Structure

This is the sturcture of this project:

![structure](https://github.com/user-attachments/assets/e6cb2cce-49eb-44f7-9a39-7c073f7a861b)


### 2.2. Info about SubtitleHarcoder

The function of **SubtitleHardcoder** is to embed hardcoded subtitles into a video when both the video and subtitle files are provided.

In **SubtitleHardcoder.py**, the program executes the operation by allowing the user to input the video path, subtitle path, and output path separately.

In **SubtitleHardcoder(GUI).py**, users can use a graphical user interface (GUI) to process videos and subtitles individually or in batches. For batch processing, the video and subtitle files must have matching names to be correctly paired.

### 2.3. Info about FormatTransformer

The function of **FormatTransformer** is to convert subtitle files between different formats.

In **FormatTransformer.py**, the program performs the conversion based on the file path and target format provided by the user.

In **FormatTransformer(GUI).py**, users can use a graphical user interface (GUI) to convert subtitle file formats individually or in batches.

---
## 3. Required environment
- 1. Compile FFmpeg with libass support.
- 2. Install wxWidgets (only for GUI-version files).
```bash
pip install wxPython
```

---

## 4. Contribution

Contributions are welcome! Follow these steps:
 - 1. Fork project.
 - 2. Create branch:
 ```bash
 git checkout -b feature-name
```
- 3. Submit changes:
```bash
git commit -m "Explain changes"
```
- 4. Push branch:
```bash
git push orgin feature-name
```
- 5. Submit Pull Request.

---
## 5. License

This project uses [MIT LICENSE](https://github.com/SomeB1oody/SubtitleMaster/blob/main/LICENSE).

---
## 6. Contact information

- Email: stanyin64@gmail.com
- GitHub: [@SomeB1ooody](https://github.com/SomeB1oody)
