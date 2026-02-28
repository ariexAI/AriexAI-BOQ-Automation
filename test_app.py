import streamlit as st
import requests

st.title("🚀 AriexAI Testing Panel")

API_URL = "http://127.0.0.1:8000"


# -------------------
# Upload Drawing
# -------------------

uploaded_file = st.file_uploader(
    "Upload Drawing PDF",
    type=["pdf"]
)

if uploaded_file:

    if st.button("Upload Drawing"):

        files = {
            "file": (
                uploaded_file.name,
                uploaded_file,
                "application/pdf"
            )
        }

        response = requests.post(
            f"{API_URL}/upload_drawing",
            files=files
        )

        st.write(response.json())


# -------------------
# Detect Footing Sizes
# -------------------

if st.button("Detect Footing Sizes"):

    response = requests.get(
        f"{API_URL}/detect_footing_sizes"
    )

    result = response.json()

    st.subheader("Detection Result")

    st.json(result)