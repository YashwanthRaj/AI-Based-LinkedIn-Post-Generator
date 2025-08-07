# AI-Powered LinkedIn Post Generator

An AI-based tool that generates professional, personalized LinkedIn posts by analyzing your previous content to match your writing style and key themes. Built using Llama 3.1 8B on Groq Cloud and Streamlit, this app simplifies the content creation process for professionals and thought leaders.

---

## 🚀 Features

- **Style Matching:** Learns your writing tone from past posts.
- **Theme Extraction:** Identifies frequently discussed topics and interests.
- **Customizable Output:** Control over topic, post length, and language.
- **Fast Inference:** Built with Groq Cloud for low-latency response times.
- **Streamlit UI:** Lightweight, interactive interface for quick post generation.

---

## 🧠 Project Architecture

The project consists of two main stages: **Pre-processing** and **Post Generation**.

### **Stage 1: Pre-Processing**

This stage involves analyzing historical post data to extract structure and meaning.

#### 1.1 Data Collection
- For demonstration, posts from Sundar Pichai’s LinkedIn were manually collected.
- Stored in JSON format with two fields:
  - `text`: Post content
  - `engagement`: Likes and comments

#### 1.2 Environment Setup
- Python environment using **PyCharm**
- Project directory structure:
  - `data/` for raw and processed JSON files
  - `.env` for Groq API key (excluded via `.gitignore`)
  
#### 1.3 LLM Helper Module
- A helper script to interface with **Llama 3.1 8B** via Groq API
- Uses environment variables from `.env` file
- Handles authentication and prompt completion

#### 1.4 Data Enrichment
- Adds `text_count` and `tags` fields for each post using LLM
- Tags capture topic-level semantics of each post

---

### **Stage 2: Post Generation**

This stage creates new posts in the user’s style using processed data and user inputs.

#### 2.1 Streamlit UI
- Install via `pip install streamlit`
- UI inputs:
  - Topic
  - Desired post length
  - Language preference

#### 2.2 Prompt Engineering
- Craft prompts that:
  - Refer to prior posts and themes
  - Guide the model to generate coherent, on-brand content

#### 2.3 Output
- Final LinkedIn post is rendered on-screen with instant regeneration capability

---

## ☁️ Groq Cloud Setup

- Uses `llama-3.1-8b-instant` for inference
- API Key stored securely in `.env` file
- Offers high-speed inference, ideal for real-time applications

---

## 🛠 Tech Stack

- **Language:** Python
- **Frontend:** Streamlit
- **LLM:** Llama 3.1 8B (via Groq Cloud)
- **IDE:** PyCharm
- **Deployment:** Local Streamlit App (can be containerized or hosted)

---

## 🧪 Future Improvements

- Automate LinkedIn data scraping via API or browser automation
- Add user authentication for multi-user capability
- Deploy as a web service with persistent history
- Integrate multilingual support and tone control
