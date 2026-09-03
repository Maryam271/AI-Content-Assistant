# ✨ AI Content Assistant

An AI-powered content generation assistant built with **Python, Streamlit, and Groq**. It helps users quickly create platform-specific social media content by selecting the content type, platform, topic, target audience, and tone.

The application generates a **complete social media post, caption, and relevant hashtags** using the Groq-hosted **OpenAI GPT-OSS 120B** model.

---

## 🚀 Features

* ✍️ Generate complete social media posts
* 📱 Select the target social media platform
* 🎯 Define the target audience
* 🎨 Select the desired writing tone
* 📝 Choose different content types
* #️⃣ Automatically generate relevant hashtags
* 💬 Generate a short caption
* 📥 Download generated content as a `.txt` file
* ⚡ Fast AI generation using Groq
* 🔐 Secure API key handling using Streamlit Secrets
* 🌐 Easy deployment on Streamlit Community Cloud
* 🧩 Simple and beginner-friendly codebase

---

## 🛠️ Technologies Used

| Technology          | Purpose                          |
| ------------------- | -------------------------------- |
| Python              | Application programming language |
| Streamlit           | Web application UI               |
| Groq                | AI content generation            |
| OpenAI GPT-OSS 120B | AI language model                |

---

## 📂 Project Structure

```text
AI-Content-Assistant/
│
├── app.py
├── requirements.txt
└── README.md
```

### `app.py`

Contains the complete Streamlit application, including:

* User interface
* User input handling
* Prompt creation
* Groq API integration
* Content generation
* Download functionality

### `requirements.txt`

Contains the Python dependencies required to run the application.

---

## ⚙️ How It Works

The application follows a simple workflow:

```text
User
  ↓
Select Content Type
  ↓
Select Platform
  ↓
Enter Topic
  ↓
Enter Target Audience
  ↓
Select Tone
  ↓
Generate Content
  ↓
Groq AI
  ↓
OpenAI GPT-OSS 120B
  ↓
Complete Post
  +
Caption
  +
Hashtags
  ↓
Download Content
```

---

## 💻 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Maryam271/AI-Content-Assistant.git
```

Move into the project directory:

```bash
cd AI-Content-Assistant
```

---

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure Groq API Key

The application requires a Groq API key.

Create a `.streamlit` folder inside the project:

```text
AI-Content-Assistant/
│
├── .streamlit/
│   └── secrets.toml
│
├── app.py
├── requirements.txt
└── README.md
```

Inside `secrets.toml`, add:

```toml
GROQ_API_KEY = "your_groq_api_key_here"
```

**⚠️ Important:** Never upload your `secrets.toml` file or API key to GitHub.

---

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

Usually:

```text
http://localhost:8501
```

---

## 🧪 Example

### User Input

**Content Type:** Educational Post

**Platform:** LinkedIn

**Topic:** Importance of AI skills for university students

**Target Audience:** University students

**Tone:** Professional

### Generated Output

The AI generates:

```text
POST:
[Complete LinkedIn post]

CAPTION:
[Short engaging caption]

HASHTAGS:
#AI #ArtificialIntelligence #Students #Technology #Learning
```

The generated content can then be downloaded as a text file.

---

## 🎯 Future Improvements

Possible future features include:

* Multiple post variations
* Content length selection
* Emoji control
* Language selection
* Custom hashtag count
* Content history
* Copy-to-clipboard button
* Image prompt generation
* Additional AI models
* More social media platforms
* Content calendar
* User accounts

---

## 📄 License

This project is open-source and available for educational and personal use.
