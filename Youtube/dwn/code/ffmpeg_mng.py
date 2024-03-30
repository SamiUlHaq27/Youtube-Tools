import os


def merge_audio_video(audio, video, output):
    output = os.system(f"ffmpeg -i {audio} -i {video} {output}")
    return output

def get_audio(input, output):
    output = os.system(f"ffmpeg -i {input} -vn {output}")
    return output

def get_video(input, output):
    output = os.system(f"ffmpeg -i {input} -an {output}")
    return output
    
def change_format(input, output):
    output = os.system(f"ffmpeg -i {input} {output}")
    return output