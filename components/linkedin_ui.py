# components/linkedin_ui.py

import streamlit as st

def render_linkedin_ui():
    st.subheader("LinkedIn Post")

    topic = st.text_input("Topic / Main Idea")

    col1, col2 = st.columns(2)
    with col1:
        role = st.text_input("Your role / industry")
    with col2:
        audience = st.text_input("Target audience")

    points = st.text_area("Key points (one per line)").split("\n")

    tone = st.selectbox(
        "Tone",
        ["Professional", "Storytelling", "Thought Leader", "Casual", "Inspirational"]
    )

    cta = st.selectbox(
        "Call to Action",
        ["Ask a question", "Share your thoughts", "Follow for more"]
    )

    return {
        "platform": "linkedin",
        "topic": topic,
        "role": role,
        "audience": audience,
        "points": points,
        "tone": tone,
        "cta": cta
    }