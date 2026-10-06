import json
import ollama


def analyze_intent(user_command):

    print(
        f"\n[OneTouch.AI] 🧠 Understanding command: "
        f"'{user_command}'"
    )

    system_prompt = """
You are the AI brain of OneTouch.AI.

Your job is to understand the user's command and convert it into
structured JSON.

Choose EXACTLY ONE intent from:

whatsapp
email
call
music
search
unknown

Rules:

1. whatsapp
Use for:
- text someone
- message someone
- WhatsApp someone
- send a WhatsApp message

2. email
Use for:
- draft an email
- write an email
- compose an email

3. call
Use for:
- call someone
- phone someone
- dial someone

4. music
Use for:
- play music
- play a song
- play an artist
- play on YouTube

5. search
Use for:
- search something
- Google something
- find information
- look something up

6. unknown
Use when the command does not match any of these.

Return ONLY valid JSON.

The JSON must contain exactly these three keys:

{
    "intent": "whatsapp",
    "recipient": "Akshitha",
    "detail": "I'll be home late"
}

For search/music, recipient should be "none".

For call, recipient should contain the person's name.

For email, recipient should contain the person's name.

For whatsapp:
- recipient = person receiving the message
- detail = exact message content

For email:
- recipient = person receiving the email
- detail = email content

For music:
- detail = song/artist/music requested

For search:
- detail = search query

If information is missing, use "none".
"""

    default_data = {
        "intent": "unknown",
        "recipient": "none",
        "detail": "none"
    }

    try:

        response = ollama.chat(
            model="llama3.2:latest",
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_command
                }
            ]
        )

        result_text = response["message"]["content"].strip()

        # Remove markdown code blocks if the model adds them
        if result_text.startswith("```"):
            result_text = result_text.replace(
                "```json", ""
            ).replace(
                "```", ""
            ).strip()

        print(
            f"[OneTouch.AI] AI response: {result_text}"
        )

        intent_data = json.loads(result_text)

        # Make sure all required keys exist
        intent_data.setdefault("intent", "unknown")
        intent_data.setdefault("recipient", "none")
        intent_data.setdefault("detail", "none")

    except Exception as e:

        print(
            f"[OneTouch.AI] AI parsing error: {e}"
        )

        intent_data = default_data.copy()

    # -------------------------------------------------
    # FALLBACK SAFETY NET
    # -------------------------------------------------

    if intent_data["intent"] == "unknown":

        cmd = user_command.lower()

        print(
            "[OneTouch.AI] Using keyword fallback..."
        )

        if (
            "whatsapp" in cmd
            or "text" in cmd
            or "message" in cmd
        ):
            intent_data["intent"] = "whatsapp"

        elif (
            "email" in cmd
            or "mail" in cmd
        ):
            intent_data["intent"] = "email"

        elif (
            "call" in cmd
            or "dial" in cmd
            or "phone" in cmd
        ):
            intent_data["intent"] = "call"

        elif (
            "play" in cmd
            or "music" in cmd
            or "song" in cmd
            or "youtube" in cmd
        ):
            intent_data["intent"] = "music"

        elif (
            "search" in cmd
            or "google" in cmd
            or "look up" in cmd
            or "find" in cmd
        ):
            intent_data["intent"] = "search"

        # If AI didn't extract detail,
        # use the complete spoken command.
        if intent_data["detail"] == "none":
            intent_data["detail"] = user_command

    print(
        f"[OneTouch.AI] Intent: "
        f"{intent_data['intent']}"
    )

    print(
        f"[OneTouch.AI] Recipient: "
        f"{intent_data['recipient']}"
    )

    print(
        f"[OneTouch.AI] Detail: "
        f"{intent_data['detail']}"
    )

    return intent_data


if __name__ == "__main__":

    test_command = (
        "text Akshitha that I will be home late"
    )

    print(analyze_intent(test_command))