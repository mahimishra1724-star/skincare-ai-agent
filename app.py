import streamlit as st
from PIL import Image
import os

from ocr import extract_text
from cleaner import clean_text
from analyzer import analyze_ingredients

st.set_page_config(page_title="SkinScan AI", layout="wide")

st.title("🧴 SkinScan AI")

skin_type = st.selectbox(
    "Select your skin type",
    ["Normal", "Oily", "Dry", "Combination", "Sensitive"]
)

uploaded_file = st.file_uploader(
    "Upload Ingredient Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    image = Image.open(uploaded_file)
    st.image(image, width=350)

    temp_path = "temp_image.jpg"
    image.save(temp_path)

    raw_text = extract_text(temp_path)
    clean = clean_text(raw_text)

    results = analyze_ingredients(clean, skin_type)

    st.subheader("Safety Score")
    st.metric("Score", f"{results['safety_score']}/10")

    st.subheader("Counts")
    st.write(f"✅ Good: {results['good_count']}")
    st.write(f"🟡 Moderate: {results['moderate_count']}")
    st.write(f"❌ Harmful: {results['harmful_count']}")

    st.subheader("✅ Good Ingredients")
    st.write(results["good"])

    st.subheader("🟡 Moderate Ingredients")
    st.write(results["moderate"])

    st.subheader("❌ Harmful Ingredients")
    st.write(results["harmful"])

    st.subheader("Skin Suitability")
    st.success(results["suitability"])

    st.subheader("Recommended Usage")
    st.info(results["recommended_usage"])

    os.remove(temp_path)