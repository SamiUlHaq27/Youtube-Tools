import pytube_mng
import ffmpeg_mng
import os


if __name__=="__main__":
    # link = ""
    # youtube_object = pytube_mng.get_object(link)
    # streams = pytube_mng.get_streams(youtube_object)
    
    # for stream in streams:
    #     pass
    
    result = ffmpeg_mng.merge_audio_video("output/audio.mp3", "output/video.mp4", "output/result.mp4")
    print(result)