import streamlit as st
import tensorflow as tf
import keras
from keras.preprocessing.image import img_to_array
from PIL import Image

model = keras.models.load_model('pages/modelUAS2.h5')

def preprocess_image(image_path):
    img = Image.open(image_path).convert("RGB")
    img = img.resize((150, 150))  # Assuming your model expects 224x224 input
    img_array = img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create batch axis
    return img_array / 255.0

def predict_sentiment(image):
    result = model.predict(image)
    threshold = 0.5
    sentiment = "Negative" if result[0][0] > threshold else "Malaria"
    return sentiment

def main():
    st.set_page_config(
        page_title="Malaria Blood Detection",
        page_icon="microscope"
    )
    st.title("Detection")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = preprocess_image(uploaded_file)
        if st.button("Analysis"):
            result = predict_sentiment(image)
            st.write(f"Prediction: {result}")

if __name__ == "__main__":
    main()