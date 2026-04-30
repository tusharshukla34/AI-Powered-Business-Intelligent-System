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

        if not text or len(text) < 3:
            continue

        # 🔴 Exit command
        if "exit" in text:
            print("🤖 AI: Goodbye Tushar")
            speak("Goodbye Tushar")
            break

        # 🔹 Wake word
        if is_wake_word(text):
            active = True

            query = text.replace("tushar", "").strip()

            # Only wake word
            if not query:
                print("🤖 AI: Yes Tushar, how can I help you?")
                speak("Yes Tushar, how can I help you?")
                time.sleep(1)
                continue

            text = query  # process immediately

        # 🔥 Active mode
        if active:
            try:
                print("⚡ Processing...")

                result = app.invoke({
                    "user_input": text,
                    "history": history
                })

                history = result.get("history", history)
                response_text = result["response"]

                # 🔥 Clean + Short response
                clean_response = response_text.replace("\n", " ").strip()

                if len(clean_response) > 120:
                    clean_response = clean_response[:120] + "..."

                # ✅ SHOW TEXT FIRST
                print(f"\n🤖 AI: {clean_response}")

                # ✅ THEN SPEAK
                speak(clean_response)

                # 🔥 WAIT before listening again
                time.sleep(1)

            except Exception as e:
                print("Error:", e)
                print("🤖 AI: Something went wrong")
                speak("Something went wrong")
                time.sleep(1)

            continue


if __name__ == "__main__":
    run_voice_agent()