from backend.voice.speech_to_text import listen
from backend.voice.text_to_speech import speak
from backend.voice.wake_word import is_wake_word

from backend.graph.langgraph_setup import build_graph

import time


def run_voice_agent():
    app = build_graph()

    print("🎤 Voice Assistant Started... Say 'Tushar' to wake up")

    history = []
    active = False

    while True:
        text = listen()

        if len(text) < 3:
            continue

        # 🔴 Exit
        if "exit" in text:
            speak("Goodbye Tushar")
            break

        # 🔹 Wake word
        if is_wake_word(text):
            active = True

            query = text.replace("tushar", "").strip()

            if not query:
                speak("Yes Tushar, how can I help you?")
                time.sleep(1.5)
                continue

            text = query

        # 🔥 Active mode
        if active:
            try:
                print("🎤 Listening for your query...")

                result = app.invoke({
                    "user_input": text,
                    "history": history
                })

                history = result.get("history", history)

                response_text = result["response"]

                # 🔥 DEBUG (optional)
                print("AI RAW:", response_text)

                # 🔥 SHORT RESPONSE FOR VOICE
                clean_response = response_text.replace("\n", " ").strip()
                if len(clean_response) > 150:
                     clean_response = clean_response[:150] + "..."

                speak(clean_response)

                time.sleep(1.5)

            except Exception as e:
                print("Error:", e)
                speak("Something went wrong")
                time.sleep(1.5)

            continue


if __name__ == "__main__":
    run_voice_agent()