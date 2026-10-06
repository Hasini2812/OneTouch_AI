import speech_recognition as sr


def capture_voice_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\n[OneTouch.AI] 🎤 Listening...")
        print("[OneTouch.AI] Speak your command.")

        recognizer.adjust_for_ambient_noise(source, duration=1)

        try:
            audio_data = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=15
            )
        except sr.WaitTimeoutError:
            print("[OneTouch.AI] No voice detected.")
            return None

    print("[OneTouch.AI] 🧠 Processing your voice...")

    try:
        text_command = recognizer.recognize_google(audio_data)

        print(f"[OneTouch.AI] You said: \"{text_command}\"")

        return text_command

    except sr.UnknownValueError:
        print("[OneTouch.AI] ❌ Sorry, I couldn't understand that.")
        return None

    except sr.RequestError:
        print("[OneTouch.AI] ❌ Speech service is unavailable.")
        return None


if __name__ == "__main__":
    capture_voice_command()