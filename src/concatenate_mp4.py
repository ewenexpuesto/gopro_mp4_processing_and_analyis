from moviepy import VideoFileClip, concatenate_videoclips
import os

def concatenate_mp4(video_paths: list, output_path: str) -> None:
    """
    Concatenates a list of mp4 files and writes the output to a given path. But it doesn't keep GoPro metadata (GPMF).

    Parameters
    ----------
    - video_paths: List of strings, each a path to a video file.
    - output_path: Output file path (e.g., "output/final_video.mp4").
    """

    if not video_paths:
        raise ValueError("The list of video paths is empty.")

    try:
        # Load all video clips
        clips = [VideoFileClip(path) for path in video_paths]

        # Ensure all videos have the same size and fps
        sizes = [tuple(clip.size) for clip in clips]
        fps_values = [clip.fps for clip in clips]

        if len(set(sizes)) > 1:
            raise ValueError("All videos must have the same resolution.")
        if len(set(fps_values)) > 1:
            raise ValueError("All videos must have the same frame rate.")

        # Concatenate
        final_clip = concatenate_videoclips(clips, method="compose")

        # Create output folder if it doesn't exist
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        # Write output video
        final_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")

        # Close clips to release resources
        for clip in clips:
            clip.close()
        final_clip.close()

        print(f"Video successfully saved to {output_path}")

    except Exception as e:
        print(f"Error during video concatenation: {e}")

mp4_input_1 = ["data1/GH010025.MP4", "data1/GH020025.MP4"]
mp4_input_2 = ["data2/GH010024.MP4", "data2/GH020024.MP4", "data2/GH030024.MP4"]
mp4_output_1 = "data/video1.mp4"
mp4_output_2 = "data/video2.mp4"

concatenate_mp4(mp4_input_1, mp4_output_1)
concatenate_mp4(mp4_input_2, mp4_output_2)