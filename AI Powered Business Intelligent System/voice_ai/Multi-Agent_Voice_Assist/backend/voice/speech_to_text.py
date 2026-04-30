import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎤 Listening...")

        # 🔥 reduce background noise
        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            # 🔥 increased timing for better capture
            audio = recognizer.listen(
                source,
                timeout=7,
                phrase_time_limit=10
            )
        except sr.WaitTimeoutError:
            print("⏱️ Timeout - no speech detected")
            return ""

    try:
        # 🔥 better for Indian accent
        text = recognizer.recognize_google(audio, language="en-IN")

        print("You said:", text)
        return text.lower()

    except sr.UnknownValueError:
        print("❌ Could not understand")
        return ""

    except sr.RequestError:
        print("❌ API error")
        return ""