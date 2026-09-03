import os
import streamlit as st
from groq import Groq

# -----------------------------
# Page setup
# -----------------------------
st.set_page_config(
    page_title="AI Content Assistant",
    page_icon="✨",
    layout="centered"
)

st.title("✨ AI Content Assistant")
st.write(
    "Create social media content by choosing the content type, platform, "
    "topic, target audience, and tone."
)

# -----------------------------
# Get Groq API key
# -----------------------------
def get_api_key():
    try:
        return st.secrets["GROQ_API_KEY"]
    except Exception:
        return os.getenv("GROQ_API_KEY")


api_key = get_api_key()

if not api_key:
    st.warning(
        "Groq API key is missing. Add GROQ_API_KEY to Streamlit Secrets "
        "before using the app."
    )

# -----------------------------
# User inputs
# -----------------------------
content_type = st.selectbox(
    "Content Type",
    [
        "Social Media Post",
        "Educational Post",
        "Promotional Post",
        "Announcement",
        "Product/Service Post",
        "Personal Branding Post",
    ],
)

platform = st.selectbox(
    "Platform",
    ["LinkedIn", "Instagram", "Facebook", "X (Twitter)"],
)

topic = st.text_area(
    "Topic",
    placeholder="Example: How AI is changing education",
    height=100,
)

target_audience = st.text_input(
    "Target Audience",
    placeholder="Example: University students and young professionals",
)

tone = st.selectbox(
    "Tone",
    [
        "Professional",
        "Friendly",
        "Informative",
        "Inspirational",
        "Persuasive",
        "Casual",
    ],
)

# -----------------------------
# Generate content
# -----------------------------
if st.button("Generate Content", type="primary", use_container_width=True):
    if not api_key:
        st.error("Please add your Groq API key in Streamlit Secrets.")
    elif not topic.strip():
        st.error("Please enter a topic.")
    elif not target_audience.strip():
        st.error("Please enter a target audience.")
    else:
        prompt = f"""
You are an expert social media content writer.

Create a complete {content_type} for {platform}.

Topic: {topic}
Target audience: {target_audience}
Tone: {tone}

Requirements:
- Make the content appropriate for {platform}.
- Write a strong opening hook.
- Make the main post clear, useful, and engaging.
- Keep the language natural and easy to read.
- Add a clear call-to-action when appropriate.
- Write a short caption.
- Add 5 to 10 relevant hashtags.
- Do not explain your process.
- Return only the final content.

Use this format:

POST:
[complete post]

CAPTION:
[short caption]

HASHTAGS:
[relevant hashtags]
"""

        try:
            client = Groq(api_key=api_key)

            with st.spinner("Generating your content..."):
                response = client.chat.completions.create(
                    model="openai/gpt-oss-120b",
                    messages=[
                        {
                            "role": "system",
                            "content": (
                                "You are a professional content assistant who creates "
                                "high-quality social media posts."
                            ),
                        },
                        {"role": "user", "content": prompt},
                    ],
                    temperature=0.8,
                    max_tokens=1200,
                )

            generated_content = response.choices[0].message.content

            st.success("Content generated successfully!")
            st.subheader("Generated Content")
            st.markdown(generated_content)

            st.download_button(
                label="Download Content",
                data=generated_content,
                file_name="generated_content.txt",
                mime="text/plain",
                use_container_width=True,
            )

        except Exception as error:
            st.error(f"Something went wrong: {error}")

st.divider()
st.caption("Built with Streamlit and Groq")
