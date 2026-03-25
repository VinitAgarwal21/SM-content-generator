# components/instagram_ui.py

import streamlit as st

def render_instagram_ui():
    st.subheader("Instagram Caption")

    topic = st.text_input("Caption topic")

    col1, col2 = st.columns(2)
    with col1:
        niche = st.selectbox("Niche", ["Lifestyle", "Fitness", "Tech", "Business"])
    with col2:
        style = st.selectbox("Caption style", ["Story", "Engaging", "Promotional"])

    context = st.text_area("Context / details")

    tone = st.selectbox(
        "Tone",
        ["Casual", "Inspirational", "Funny", "Emotional"]
    )

    cta = st.selectbox(
        "Call to Action",
        ["Save this post", "Comment below", "Share with friends"]
    )

    return {
        "platform": "instagram",
        "topic": topic,
        "niche": niche,
        "style": style,
        "context": context,
        "tone": tone,
        "cta": cta
    }