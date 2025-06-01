import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

st.set_page_config(
    page_title="Deepfake Detection",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .main { background-color: #f5f5f5; }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        border-radius: 5px;
        padding: 0.5rem 1rem;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stFileUploader>div>div>div>div {
        color: #4CAF50;
    }
    .prediction-box {
        padding: 1rem;
        border-radius: 5px;
        margin: 1rem 0;
        font-weight: bold;
        text-align: center;
    }
    .real {
        background-color: #d4edda;
        color: #155724;
    }
    .fake {
        background-color: #f8d7da;
        color: #721c24;
    }
    </style>
    """, unsafe_allow_html=True)

@st.cache_resource
def load_deepfake_model():
    model = load_model("models/deepfake_updated.h5")
    return model

model = load_deepfake_model()

def preprocess_image(image):
    image = image.resize((299, 299))
    image = np.array(image) / 255.0
    if image.shape[-1] == 4:
        image = image[:, :, :3]
    image = np.expand_dims(image, axis=0)
    return image

def main():
    st.title("Deepfake Image Detection")
    st.markdown("Upload an image to check if it's authentic or a deepfake.")

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.subheader("Upload Image")
        uploaded_file = st.file_uploader(
            "Choose an image...", 
            type=["jpg", "jpeg", "png"],
            accept_multiple_files=False,
            key="file_uploader"
        )

        if uploaded_file is not None:
            try:
                image = Image.open(uploaded_file)
                st.image(image, caption="Uploaded Image", use_container_width=True)
            except Exception as e:
                st.error(f"Error opening image: {e}")

    with col2:
        st.subheader("Detection Results")

        if uploaded_file is not None:
            with st.spinner("Analyzing image..."):
                try:
                    processed_image = preprocess_image(image)
                    prediction = model.predict(processed_image)[0]  # single value output
                    fake_confidence = float(prediction)
                    threshold = 0.5

                    if fake_confidence > threshold:
                        st.markdown(f"""
                            <div class="prediction-box fake">
                                <h3>Deepfake Detected!</h3>
                                <p>Confidence: {fake_confidence:.2%}</p>
                            </div>
                            """, unsafe_allow_html=True)
                        st.error("Warning: This image may be a deepfake.")
                    else:
                        real_confidence = 1 - fake_confidence
                        st.markdown(f"""
                            <div class="prediction-box real">
                                <h3>Authentic Image</h3>
                                <p>Confidence: {real_confidence:.2%}</p>
                            </div>
                            """, unsafe_allow_html=True)
                        st.success("This image appears to be authentic.")

                    with st.expander("What does this result mean?"):
                        st.write("""
                        - **Authentic**: The image appears to be genuine with no signs of manipulation.
                        - **Deepfake**: The image shows characteristics consistent with AI-generated or manipulated content.

                        Note: No detection system is 100% accurate. Always consider additional verification for critical decisions.
                        """)

                except Exception as e:
                    st.error(f"Error during prediction: {e}")
        else:
            st.info("Please upload an image to get started.")
            st.image("https://via.placeholder.com/400x300?text=Upload+an+image+to+analyze", use_container_width=True)

    with st.sidebar:
        st.markdown("## About")
        st.write("""
        This app uses deep learning to detect deepfake images.
        It analyzes subtle artifacts and patterns that are often
        present in AI-generated or manipulated images.
        """)

        st.markdown("## How to use")
        st.write("""
        1. Upload an image (JPG, PNG)
        2. View the results
        """)

        st.markdown("## Limitations")
        st.write("""
        - Works best with high-quality frontal face images
        - May produce false positives/negatives
        - Effectiveness depends on image quality
        """)

        st.markdown("## Model Information")
        st.write("""
        - Model: DeepFake Detection (Keras)
        - Accuracy: ~80%
        """)

if __name__ == "__main__":
    main()
