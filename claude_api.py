"""
Groq API integration for MediAI.
Uses Groq's ultra-fast inference with Llama / Mixtral models.
"""
import os
import streamlit as st

try:
    from groq import Groq
    _HAS_GROQ = True
except ImportError:
    _HAS_GROQ = False

# ── Model selection ───────────────────────────────────────────────────────────
# Groq-hosted models (pick one; compound-beta is the default smart choice)
GROQ_MODEL = "llama-3.3-70b-versatile"   # fast, very capable
# Alternatives:
#   "llama3-70b-8192"          – Llama 3 70B
#   "mixtral-8x7b-32768"       – Mixtral 8x7B (32k context)
#   "gemma2-9b-it"             – Google Gemma 2 9B

# ── System prompt ─────────────────────────────────────────────────────────────
SYSTEM_PROMPT = """You are MediAI, a professional AI healthcare assistant built to help patients
and caregivers understand health topics. You provide accurate, evidence-based health information
in a warm, clear, and well-structured manner.

CORE GUIDELINES:
1. Always clarify that you provide HEALTH INFORMATION, not medical diagnosis or treatment advice.
2. For emergency symptoms (chest pain, stroke signs, severe difficulty breathing, uncontrolled bleeding,
   loss of consciousness) → always urge the user to call emergency services (911 / 112) IMMEDIATELY.
3. Use clear formatting:
   - **Bold** for key medical terms and important warnings.
   - Bullet lists for multiple points or symptoms.
   - Numbered lists for step-by-step instructions.
4. When discussing medications: always advise consulting a pharmacist or prescribing doctor.
5. Recommend the relevant medical specialist when appropriate (e.g. cardiologist, dermatologist).
6. Be empathetic, supportive, and non-judgmental.
7. Keep answers comprehensive but digestible — avoid excessive medical jargon.
8. Cite that information is general and individual cases may vary.

TOPICS YOU CAN COVER:
- Symptom information and possible conditions
- Medication details, uses, side effects, interactions
- Lab result explanations
- Nutrition and diet advice
- Mental wellness and stress management
- Preventive care and vaccinations
- Exercise and lifestyle guidance
- Understanding medical terms and procedures
- Emergency first-aid guidance

WHAT YOU MUST NOT DO:
- Write a definitive diagnosis
- Prescribe specific medications or dosages
- Replace a real consultation with a qualified healthcare professional
"""


def get_api_key() -> str | None:
    """Return Groq API key from env or Streamlit secrets."""
    key = os.getenv("GROQ_API_KEY")
    if not key:
        try:
            key = st.secrets.get("GROQ_API_KEY")
        except Exception:
            pass
    return key


def _build_messages(messages: list[dict]) -> list[dict]:
    """Prepend system prompt to the message list for Groq."""
    return [{"role": "system", "content": SYSTEM_PROMPT}] + messages


def chat_with_claude(messages: list[dict]) -> str:
    """
    Send conversation history to Groq and return the assistant reply.

    Args:
        messages: List of {"role": "user"|"assistant", "content": str} dicts.

    Returns:
        Assistant reply string, or an error message.
    """
    if not _HAS_GROQ:
        return (
            "⚠️ The `groq` package is not installed. "
            "Run `pip install groq` and restart the app."
        )

    api_key = get_api_key()
    if not api_key:
        return (
            "⚠️ **Groq API key not found.**\n\n"
            "Please set your `GROQ_API_KEY` environment variable or add it to "
            "`.streamlit/secrets.toml` as:\n```\nGROQ_API_KEY = 'gsk_...'\n```\n\n"
            "Get your free key at https://console.groq.com"
        )

    try:
        client = Groq(api_key=api_key)
        response = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=_build_messages(messages),
            max_tokens=1024,
            temperature=0.7,
        )
        return response.choices[0].message.content

    except Exception as exc:
        err = str(exc).lower()
        if "auth" in err or "api key" in err or "invalid" in err:
            return (
                "⚠️ **Authentication failed.** Your Groq API key appears to be invalid. "
                "Please check your `GROQ_API_KEY`."
            )
        if "rate" in err or "limit" in err:
            return "⚠️ **Rate limit reached.** Please wait a moment and try again."
        return f"⚠️ **Unexpected error:** {exc}"


def stream_claude(messages: list[dict]):
    """
    Stream response from Groq token by token.

    Yields string chunks as they arrive.
    """
    if not _HAS_GROQ:
        yield "⚠️ `groq` package not installed. Run `pip install groq`."
        return

    api_key = get_api_key()
    if not api_key:
        yield (
            "⚠️ Groq API key not found. Set `GROQ_API_KEY` in your environment "
            "or `.streamlit/secrets.toml`.\n\nGet a free key at https://console.groq.com"
        )
        return

    try:
        client = Groq(api_key=api_key)
        stream = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=_build_messages(messages),
            max_tokens=1024,
            temperature=0.7,
            stream=True,
        )
        for chunk in stream:
            delta = chunk.choices[0].delta
            if delta and delta.content:
                yield delta.content

    except Exception as exc:
        yield f"\n\n⚠️ Groq API error: {exc}"
