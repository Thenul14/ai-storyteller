import streamlit as st
from agent import tell_story

st.set_page_config(
    page_title="AI Story Generator",
    page_icon="📖",
    layout="centered"
)

st.title("📖 AI Story Generator")
st.caption("Create imaginative stories instantly using Gemini 2.5 Flash")

topic = st.text_input(
    "Enter a story topic",
    placeholder="e.g. A dragon who is afraid of flying..."
)

length = st.select_slider(
        "Story Length",
        options=["Short", "Medium", "Long"],
        value="Medium"
    )

generate = st.button(
    "✨ Generate Story",
    use_container_width=True
)

if generate:

    if not topic:
        st.warning("Please enter a story topic.")
        st.stop()

    with st.spinner("Creating your story..."):
        story = tell_story(topic, length)

        st.subheader("📚 Your Story")

        st.markdown(story)
        col1, col2 = st.columns(2)

        with col1:
            st.download_button(
                "⬇ Download Story",
                story,
                file_name="story.txt"
            )

        with col2:
            st.button("🔄 Generate Another")

