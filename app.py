import streamlit as st
from agent import tell_story

st.set_page_config(
    page_title="AI Story Generator",
    page_icon="📖",
    layout="centered"
)

st.markdown(
    "<h1 style='text-align: center;'>📖 AI Story Generator</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<h5 style='text-align: center;'>Create imaginative stories instantly using Gemini 2.5 Flash</h5>",
    unsafe_allow_html=True
)

topic = st.text_input(
    "Enter a story topic",
    placeholder="e.g. A dragon who is afraid of flying..."
)

length = st.select_slider(
        "Story Length",
        options=["Short", "Medium", "Long"],
        value="Medium"
    )

genres = [
    "Fantasy",
    "Adventure",
    "Science Fiction",
    "Mystery",
    "Horror",
    "Romance",
    "Comedy",
    "Thriller",
    "Historical",
    "Drama",
    "Fairy Tale",
    "Cyberpunk",
    "Steampunk",
    "Superhero",
    "Post-Apocalyptic",
    "Western",
    "Crime",
    "Mythology",
    "Detective",
    "Slice of Life",
]

genre = st.selectbox(
    "Select a Genre",
    genres,
    index=0
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
        result = tell_story(topic, length, genre)

        st.markdown(
            "<h3 style='text-align: center; text-decoration: underline;'>📚 Your Story</h3>",
            unsafe_allow_html=True
        )

        st.markdown(
            f"<h2 style='text-align: center;'>{result['title']}</h2>",
            unsafe_allow_html=True
        )

        
        st.write(result["story"])

        col1, col2 = st.columns(2)

        with col1:
            st.download_button(
                "⬇ Download Story",
                result["story"],
                file_name="story.txt"
            )

        with col2:
            st.button("🔄 Generate Another")

