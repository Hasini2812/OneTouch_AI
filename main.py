from voice_input import capture_voice_command
from intent_engine import analyze_intent
from automation_actions import execute_action


def start_onetouch_ai():

    print("\n")
    print("============================================")
    print("          ONETOUCH.AI")
    print("     Voice Action Assistant - V1")
    print("============================================")

    print("\n[System] 🟢 OneTouch.AI is ready.")
    print("[System] Say a command...\n")

    spoken_command = capture_voice_command()

    if not spoken_command:

        print(
            "\n[OneTouch.AI] "
            "No command received."
        )

        return

    # ---------------------------------------------
    # AI UNDERSTANDING
    # ---------------------------------------------

    intent_data = analyze_intent(
        spoken_command
    )

    # ---------------------------------------------
    # ACTION
    # ---------------------------------------------

    if intent_data:

        if intent_data.get("intent") != "unknown":

            print(
                "\n[OneTouch.AI] "
                "🤖 Understanding complete."
            )

            execute_action(
                intent_data,
                raw_command=spoken_command
            )

        else:

            print(
                "\n[OneTouch.AI] "
                "❌ I don't know how to do that yet."
            )

    else:

        print(
            "\n[OneTouch.AI] "
            "❌ Something went wrong."
        )


if __name__ == "__main__":
    start_onetouch_ai()