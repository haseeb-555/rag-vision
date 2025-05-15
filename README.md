Thanks for sharing your code. Based on it, here's a tailored update for your `README.md`:

---

```markdown
# Vision RAG with Cohere Embed-4 🖼️

This Streamlit app demonstrates a **Vision-based Retrieval-Augmented Generation (RAG)** system. It combines **Cohere's Embed-4** for multimodal image embeddings and **Google Gemini 2.5 Flash** for answering questions about images or PDFs.

---

## 🔍 Features

- Upload and embed images (PNG, JPG) or PDFs
- Automatically extract PDF pages and generate embeddings
- Load sample images from the web
- Perform semantic search over visual documents using Cohere Embed-4
- Ask natural language questions and get answers from Gemini 2.5 Flash
- View matching images and answers side by side

---

## 📁 Project Structure
```

├── app.py # Main Streamlit app
├── pdf_pages/ # Stores extracted PDF page images
├── uploaded_img/ # Stores uploaded user images
├── requirements.txt # Python dependencies
├── README.md # You're reading it
├── test_cohere.py # Optional script to test Cohere API
├── test_gemini.py # Optional script to test Gemini API
├── venv/ # Python virtual environment (ignored by Git)

````

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/vision-rag.git
cd vision-rag
````

### 2. Set up the environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run app.py
```

---

## 🔑 API Keys

You’ll need:

- **[Cohere API Key](https://dashboard.cohere.com/api-keys)**
- **[Google Gemini API Key](https://aistudio.google.com/app/apikey)**

Enter them in the sidebar after launching the app.

---

## 🧪 Example Use Case

1. Click “Load Sample Images” to fetch financial charts.
2. Ask a question like:
   _"What is Netflix’s operating income?"_
3. The app retrieves the most relevant image and passes it to Gemini for a detailed answer.

---

## 📦 Requirements

Python 3.9+
See `requirements.txt` for full list.

---

## 📌 Notes

- `pdf_pages/` and `uploaded_img/` are used for storing temporary image data.
- Embeddings are computed with `Cohere.embed()`, using the `embed-v4.0` model.
- Gemini 2.5 Flash is used with image prompts for answering.

---

## 📝 License

MIT © 2025 \[haseeb-555]

```

---


```
