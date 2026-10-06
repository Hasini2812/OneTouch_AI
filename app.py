import io
import textwrap

import streamlit as st
import speech_recognition as sr

from intent_engine import analyze_intent
from automation_actions import execute_action


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="OneTouch.AI",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# GLOBAL CSS
# ============================================================

st.markdown(
    """
    <style>

    /* ---------- MAIN APP ---------- */

    .stApp {
        background:
            radial-gradient(
                circle at 10% 10%,
                rgba(124, 58, 237, 0.18),
                transparent 30%
            ),
            radial-gradient(
                circle at 90% 20%,
                rgba(59, 130, 246, 0.14),
                transparent 28%
            ),
            linear-gradient(
                135deg,
                #070711 0%,
                #0d0b19 45%,
                #080812 100%
            );

        color: #f5f3ff;
    }

    /* ---------- HIDE STREAMLIT DEFAULTS ---------- */

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        background: transparent !important;
    }

    /* ---------- MAIN CONTENT ---------- */

    .block-container {
        max-width: 1100px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }

    /* ---------- INPUT ---------- */

    .stChatInput {
        margin-top: 10px;
    }

    .stChatInput textarea {
        background: #11101d !important;
        color: white !important;
        border: 1px solid rgba(139, 92, 246, 0.35) !important;
        border-radius: 16px !important;
    }

    /* ---------- AUDIO ---------- */

    [data-testid="stAudioInput"] {
        background: rgba(17, 16, 29, 0.85);
        border: 1px solid rgba(139, 92, 246, 0.35);
        border-radius: 18px;
        padding: 10px;
    }

    /* ---------- BUTTON ---------- */

    .stButton > button {
        border-radius: 12px;
        border: 1px solid rgba(139, 92, 246, 0.4);
        background: #171426;
        color: white;
        font-weight: 600;
    }

    .stButton > button:hover {
        border-color: #8b5cf6;
        color: #c4b5fd;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# HELPER FOR HTML
# ============================================================

def show_html(content):
    """
    Render HTML directly instead of displaying the HTML source code.
    """
    st.html(textwrap.dedent(content))


# ============================================================
# HEADER
# ============================================================

show_html(
    """
    <div style="
        display:flex;
        justify-content:space-between;
        align-items:center;
        padding:18px 0 10px 0;
    ">

        <div style="
            font-size:25px;
            font-weight:800;
            letter-spacing:-0.5px;
        ">
            ✦ OneTouch<span style="color:#a78bfa;">.AI</span>
        </div>

        <div style="
            padding:7px 14px;
            border-radius:999px;
            background:rgba(34,197,94,0.10);
            border:1px solid rgba(34,197,94,0.25);
            color:#86efac;
            font-size:13px;
            font-weight:600;
        ">
            ● Online
        </div>

    </div>
    """
)


# ============================================================
# HERO SECTION
# ============================================================

show_html(
    """
    <div style="
        text-align:center;
        padding:65px 20px 35px 20px;
    ">

        <div style="
            display:inline-block;
            padding:7px 15px;
            border-radius:999px;
            background:rgba(139,92,246,0.10);
            border:1px solid rgba(139,92,246,0.25);
            color:#c4b5fd;
            font-size:13px;
            margin-bottom:18px;
        ">
            YOUR PERSONAL AI ACTION ASSISTANT
        </div>

        <h1 style="
            font-size:clamp(42px,7vw,72px);
            line-height:1.05;
            margin:0;
            font-weight:850;
            letter-spacing:-3px;
            color:#ffffff;
        ">
            Speak Ur Commmand. <br>
            <span style="
                background:linear-gradient(
                    90deg,
                    #a78bfa,
                    #8b5cf6,
                    #60a5fa
                );
                -webkit-background-clip:text;
                -webkit-text-fill-color:transparent;
            ">
                One Touch Acts.
            </span>
        </h1>

        <p style="
            max-width:650px;
            margin:22px auto 0 auto;
            font-size:18px;
            line-height:1.7;
            color:#a8a5b8;
        ">
            OneTouch.AI understands what you say and turns your
            natural-language commands into actions.
        </p>

    </div>
    """
)


# ============================================================
# EXAMPLES
# ============================================================

show_html(
    """
    <div style="
        display:flex;
        justify-content:center;
        flex-wrap:wrap;
        gap:10px;
        margin:10px 0 30px 0;
    ">

        <div style="
            padding:9px 14px;
            border-radius:12px;
            background:rgba(255,255,255,0.035);
            border:1px solid rgba(255,255,255,0.08);
            color:#bdb9ca;
            font-size:13px;
        ">
            💬 Message anyone
        </div>

        <div style="
            padding:9px 14px;
            border-radius:12px;
            background:rgba(255,255,255,0.035);
            border:1px solid rgba(255,255,255,0.08);
            color:#bdb9ca;
            font-size:13px;
        ">
            🔎 Search what u need
        </div>

        <div style="
            padding:9px 14px;
            border-radius:12px;
            background:rgba(255,255,255,0.035);
            border:1px solid rgba(255,255,255,0.08);
            color:#bdb9ca;
            font-size:13px;
        ">
            🎵 Play music
        </div>

        <div style="
            padding:9px 14px;
            border-radius:12px;
            background:rgba(255,255,255,0.035);
            border:1px solid rgba(255,255,255,0.08);
            color:#bdb9ca;
            font-size:13px;
        ">
            ✉️ Draft an email
        </div>

    </div>
    """
)


# ============================================================
# COMMAND PROCESSOR
# ============================================================

def process_command(command):

    if not command:
        return

    # Store current command
    st.session_state["last_command"] = command

    # Show what user said
    show_html(
        f"""
        <div style="
            margin-top:25px;
            padding:18px 20px;
            border-radius:18px;
            background:rgba(139,92,246,0.08);
            border:1px solid rgba(139,92,246,0.22);
        ">

            <div style="
                color:#a78bfa;
                font-size:12px;
                font-weight:700;
                text-transform:uppercase;
                letter-spacing:1px;
                margin-bottom:8px;
            ">
                YOU SAID
            </div>

            <div style="
                color:#ffffff;
                font-size:17px;
                line-height:1.5;
            ">
                {command}
            </div>

        </div>
        """
    )

    # --------------------------------------------------------
    # AI INTENT ANALYSIS
    # --------------------------------------------------------

    with st.spinner("OneTouch.AI is thinking..."):

        try:
            intent_data = analyze_intent(command)

        except Exception as e:

            st.error("Could not understand the command.")

            with st.expander("Technical details"):
                st.write(e)

            return

    # --------------------------------------------------------
    # SHOW DETECTED INTENT
    # --------------------------------------------------------

    if isinstance(intent_data, dict):

        intent_name = intent_data.get("intent", "unknown")
        recipient = intent_data.get("recipient", "")
        detail = intent_data.get("detail", "")

        show_html(
            f"""
            <div style="
                margin-top:16px;
                padding:20px;
                border-radius:18px;
                background:rgba(255,255,255,0.035);
                border:1px solid rgba(255,255,255,0.08);
            ">

                <div style="
                    color:#9ca3af;
                    font-size:12px;
                    font-weight:700;
                    text-transform:uppercase;
                    letter-spacing:1px;
                    margin-bottom:10px;
                ">
                    DETECTED ACTION
                </div>

                <div style="
                    font-size:24px;
                    font-weight:750;
                    color:#ffffff;
                    margin-bottom:12px;
                ">
                    {intent_name}
                </div>

                <div style="
                    color:#aaa6b8;
                    font-size:14px;
                    line-height:1.7;
                ">
                    {("Recipient: " + str(recipient) + "<br>" if recipient else "")}
                    {("Details: " + str(detail) if detail else "")}
                </div>

            </div>
            """
        )

    # --------------------------------------------------------
    # EXECUTE ACTION
    # --------------------------------------------------------

    with st.spinner("Executing action..."):

        try:
            result = execute_action(intent_data)

        except Exception as e:

            st.error("The action could not be executed.")

            with st.expander("Technical details"):
                st.write(e)

            return

    # --------------------------------------------------------
    # RESULT
    # --------------------------------------------------------

    if result is not None:

        show_html(
            f"""
            <div style="
                margin-top:16px;
                padding:18px 20px;
                border-radius:18px;
                background:rgba(34,197,94,0.07);
                border:1px solid rgba(34,197,94,0.20);
            ">

                <div style="
                    color:#86efac;
                    font-size:12px;
                    font-weight:700;
                    text-transform:uppercase;
                    letter-spacing:1px;
                    margin-bottom:8px;
                ">
                    RESULT
                </div>

                <div style="
                    color:#e5e7eb;
                    font-size:15px;
                    line-height:1.6;
                ">
                    {result}
                </div>

            </div>
            """
        )


# ============================================================
# VOICE INPUT
# ============================================================

show_html(
    """
    <div style="
        margin-top:30px;
        margin-bottom:10px;
        text-align:center;
    ">

        <div style="
            font-size:15px;
            font-weight:700;
            color:#e5e7eb;
        ">
            🎙️ Speak to OneTouch.AI
        </div>

        <div style="
            margin-top:5px;
            color:#777487;
            font-size:13px;
        ">
            Say a command naturally
        </div>

    </div>
    """
)


audio = st.audio_input(
    "🎙️ Speak to OneTouch.AI",
    label_visibility="collapsed"
)


# ============================================================
# PROCESS VOICE
# ============================================================

if audio is not None:

    recognizer = sr.Recognizer()

    try:

        audio_bytes = audio.getvalue()

        with sr.AudioFile(io.BytesIO(audio_bytes)) as source:

            audio_data = recognizer.record(source)

        spoken_command = recognizer.recognize_google(audio_data)

        process_command(spoken_command)

    except sr.UnknownValueError:

        st.warning(
            "I couldn't understand the audio. Please try speaking again."
        )

    except sr.RequestError as e:

        st.error(
            f"Speech recognition service error: {e}"
        )

    except Exception as e:

        st.error(
            f"Voice processing error: {e}"
        )


# ============================================================
# TEXT INPUT
# ============================================================

text_command = st.chat_input(
    "Or type a command...  Example: Message Geethika hi"
)


if text_command:

    process_command(text_command)


# ============================================================
# FOOTER
# ============================================================

show_html(
    """
    <div style="
        text-align:center;
        margin-top:65px;
        padding-top:20px;
        border-top:1px solid rgba(255,255,255,0.06);
        color:#5f5b6d;
        font-size:12px;
    ">
        OneTouch.AI · Your personal action assistant
    </div>
    """
)