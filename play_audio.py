from playsound import playsound

def play_audio(audiopath: str):
    try:
        playsound(audiopath)
    except Exception as e:
        print(e)