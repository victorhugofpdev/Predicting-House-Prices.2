import subprocess
import os

def convert_mkv_to_mp4(input_path, output_path=None):
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file does not exist: {input_path}")
    
    if output_path is None:
        output_path = os.path.splitext(input_path)[0] + ".mp4"
    
    # FFmpeg command: copy video and audio streams without re-encoding
    command = [
        'ffmpeg',
        '-i', input_path,
        '-c', 'copy',
        '-map', '0',
        output_path
    ]
    
    try:
        subprocess.run(command, check=True)
        print(f"Successfully converted to: {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")

# Example usage
convert_mkv_to_mp4("example.mkv")
