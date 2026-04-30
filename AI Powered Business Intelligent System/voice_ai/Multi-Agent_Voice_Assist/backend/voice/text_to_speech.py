from gtts import gTTS
import pygame
import time
import os
import uuid

pygame.mixer.init()

def speak(text):
    try:
        filename = f"voice_{uuid.uuid4().hex}.mp3"

        tts = gTTS(text=text, lang='en')
        tts.save(filename)

        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        # 🔥 Wait until speaking finishes
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

        pygame.mixer.music.unload()
        os.remove(filename)

    except Exception as e:
        print("TTS Error:", e)