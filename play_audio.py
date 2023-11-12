from playsound import playsound
from afplay import afplay, is_installed
from resource_path import resource_path

def play_audio(audiopath: str):
    try:
        playsound(resource_path(audiopath), block=False)
    except Exception as e:
        print(e)
