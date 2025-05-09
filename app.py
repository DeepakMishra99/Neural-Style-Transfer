import streamlit as st
from PIL import Image
import io
import os

from style_transfer import transfer_style

# Set page configuration
st.set_page_config(layout="wide", page_title="Neural Style Transfer")

# --- Main Application ---
st.title(" Neural Style Transfer")
st.markdown("""
Upload two images below. The application will then process them and display an output image as style transfer
""")

# --- Layout for Uploads and Output ---
col1, col2, col3 = st.columns(3)

# --- Image Upload Field 1 ---
with col1:
    st.header("Content Image 1")
    uploaded_file1 = st.file_uploader("Choose the content image...", type=["jpg", "jpeg", "png"])
    if uploaded_file1 is not None:
        try:
           # image1 = Image.open(uploaded_file1)
           # st.image(image1, caption="Uploaded Content Image", use_column_width=True)

            UPLOAD_FOLDER = "Images"  # Define the folder to save images
            # Create the upload folder if it doesn't exist
            content_image_filename = f"content.jpg"  #force jpg to avoid errors
            content_image_path = os.path.join(UPLOAD_FOLDER, content_image_filename)

            #Use BytesIO and save
            img_bytes = uploaded_file1.read()
            content_image = Image.open(io.BytesIO(img_bytes))
            content_image.save(content_image_path)
            st.image(content_image, caption="Uploaded Content Image", use_column_width=True)
            

        except Exception as e:
            st.error(f"Error opening Content Image: {e}")
            content_image = None
    else:
        content_image = None
        st.info("☝️ Upload an Content Image.")

# --- Image Upload Field 2 ---
with col2:
    st.header("Style Image")
    uploaded_file2 = st.file_uploader("Choose the Style Image...", type=["jpg", "jpeg", "png"])
    if uploaded_file2 is not None:
        try:
            UPLOAD_FOLDER = "Images" 
            style_image_filename = f"style.jpg" #force jpg to avoid errors
            style_image_path = os.path.join(UPLOAD_FOLDER, f"style.jpg")
            img_bytes = uploaded_file2.read()
            style_image = Image.open(io.BytesIO(img_bytes))
            style_image.save(style_image_path)
            st.image(style_image, caption="Uploaded Style Image", use_column_width=True)

        except Exception as e:
            st.error(f"Error opening Style Image: {e}")
            style_image = None
    else:
        style_image = None
        st.info("☝️ Upload a Style Image.")

# --- Output Image Area ---
with col3:
    st.header("Output Image")

    # Placeholder for image processing logic
    output_image = None

    if content_image is not None and style_image is not None:

        best, best_loss = transfer_style('Images\content.jpg', 'Images/style.jpg', epochs=100)


        st.write("Processing...") # Placeholder for processing status

        output_image = best
        st.info("Displaying style transfer as output .")


    elif content_image is not None:
        output_image = content_image
        st.info("Displaying Image 1 as output. Upload a second image for processing.")
    elif style_image is not None:
        # If only image2 is uploaded, you might want to display it or a message
        output_image = style_image # Or handle as per your logic
        st.info("Displaying Image 2 as output. Upload a first image for processing.")
    else:
        # Create a placeholder image if no images are uploaded
        placeholder = Image.new('RGB', (300, 200), color = (200, 200, 200))
        # Convert to bytes
        byte_arr = io.BytesIO()
        placeholder.save(byte_arr, format='PNG')
        byte_arr = byte_arr.getvalue()
        output_image = byte_arr # Use the byte array for st.image
        st.info("Output will appear here once images are uploaded and processed.")


    if output_image is not None:
        st.image(output_image, caption="Processed Output Image", use_column_width=True)
    else:
        st.warning("No output to display yet.")

