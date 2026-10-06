import webbrowser
import urllib.parse

from contacts import find_contact


def execute_action(intent_data):

    intent = intent_data.get("intent")
    recipient = intent_data.get("recipient")
    detail = intent_data.get("detail")

    # -------------------------
    # GOOGLE SEARCH
    # -------------------------
    if intent == "search":

        query = detail or recipient

        if not query:
            return "I don't know what you want me to search."

        url = "https://www.google.com/search?q=" + urllib.parse.quote(query)

        webbrowser.open(url)

        return f"Google search opened for: {query}"


    # -------------------------
    # MUSIC / YOUTUBE
    # -------------------------
    elif intent == "music":

        query = detail or "music"

        url = "https://www.youtube.com/results?search_query=" + urllib.parse.quote(query)

        webbrowser.open(url)

        return f"YouTube opened for: {query}"


    # -------------------------
    # WHATSAPP
    # -------------------------
    elif intent == "whatsapp":

        if not recipient:
            return "I couldn't find the WhatsApp contact."

        contact = find_contact(recipient)

        if not contact:
            return f"I couldn't find {recipient} in your contacts."

        phone = contact.get("phone")

        if not phone:
            return f"No phone number is saved for {recipient}."

        message = detail or ""

        url = (
            "https://wa.me/"
            + phone
            + "?text="
            + urllib.parse.quote(message)
        )

        webbrowser.open(url)

        return f"WhatsApp opened for {recipient} with your message ready."


    # -------------------------
    # EMAIL
    # -------------------------
    elif intent == "email":

        if not recipient:
            return "I couldn't find the email recipient."

        contact = find_contact(recipient)

        if not contact:
            return f"I couldn't find {recipient} in your contacts."

        email = contact.get("email")

        if not email:
            return f"No email address is saved for {recipient}."

        subject = "OneTouch.AI Message"
        body = detail or ""

        url = (
            "mailto:"
            + email
            + "?subject="
            + urllib.parse.quote(subject)
            + "&body="
            + urllib.parse.quote(body)
        )

        webbrowser.open(url)

        return f"Email draft opened for {recipient}."


    # -------------------------
    # CALL
    # -------------------------
    elif intent == "call":

        if not recipient:
            return "I couldn't find who you want to call."

        contact = find_contact(recipient)

        if not contact:
            return f"I couldn't find {recipient} in your contacts."

        phone = contact.get("phone")

        if not phone:
            return f"No phone number is saved for {recipient}."

        url = "tel:" + phone

        webbrowser.open(url)

        return f"Call action opened for {recipient}."


    # -------------------------
    # UNKNOWN COMMAND
    # -------------------------
    else:

        return "Sorry, I don't understand that command yet."