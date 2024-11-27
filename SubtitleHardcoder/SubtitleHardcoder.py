import subprocess

def add_subtitle_to_video(video_path, subtitle_path, output_path):
    # 使用FFmpeg将字幕嵌入视频中
    command = [
        'ffmpeg',
        '-i', video_path,
        '-vf', f'subtitles={subtitle_path}',
        '-c:a', 'copy',
        output_path
    ]

    try:
        subprocess.run(command, check=True)
        print("Subtitles were successfully added to the video!")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while processing video: {e}")


def main():
    video_path = input("Please enter the video file path:")
    subtitle_path = input("Please enter the subtitle file path:")
    output_path = input("Please output video file path:")

    add_subtitle_to_video(video_path, subtitle_path, output_path)


if __name__ == "__main__":
    main()
