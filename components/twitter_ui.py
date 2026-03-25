
# components/twitter_ui.py

import streamlit as st

def render_twitter_ui():
    st.subheader("X (Twitter) Post")

    topic = st.text_input("Tweet topic / hot take")

    format_type = st.selectbox(
        "Format",
        ["Single Tweet", "Thread (5)", "Thread (10)"]
    )

    tone = st.selectbox(
        "Tone",
        ["Bold", "Educational", "Witty", "Casual", "Controversial"]
    )

    context = st.text_area("Context / supporting points")

    return {
        "platform": "twitter",
        "topic": topic,
        "format": format_type,
        "tone": tone,
        "context": context
    }
