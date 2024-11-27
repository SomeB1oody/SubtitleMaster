import subprocess
import os

# 定义支持的字幕文件格式
SUPPORTED_FORMATS = {'srt', 'ass', 'ssa', 'sub'}


def convert_subtitle(input_path: str, output_format: str):
    # 检查输入文件是否存在
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file {input_path} does not exist.")

    # 检查目标格式是否有效
    if output_format not in SUPPORTED_FORMATS:
        raise ValueError(f"Invalid desired format: {output_format}. Supported format {', '.join(SUPPORTED_FORMATS)}")

    # 获取文件名和扩展名
    base = os.path.splitext(input_path)[0]
    output_path = f"{base}.{output_format}"

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


if __name__ == "__main__":
    input_path = input("Enter file path: ")
    output_format = input("Enter desired format(e.g., srt, ass, ssa, sub): ")

    try:
        convert_subtitle(input_path, output_format)
    except (FileNotFoundError, ValueError) as e:
        print(e)
