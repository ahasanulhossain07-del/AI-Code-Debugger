import streamlit as st
from api_calling import code_generator
from PIL import Image

# title
st.title("AI Code Debugger App")
st.markdown("Upload the image of your code error")
st.divider()

# sidebar
with st.sidebar:
    st.header("Controls")
    # image upload
    images=st.file_uploader(
        "Upload the photo of your code",
        type=["jpg","jpeg","png"],
        accept_multiple_files=True
    )
    pil_image=[]
    for img in images:
        pil_img=Image.open(img)
        pil_image.append(pil_img)

    if images:
        if len(images)>3:
            st.error("Upload at max 3 images")
        else:
            st.subheader("Upload images")
            col=st.columns(len(images))

            for i,img in enumerate(images):
                with col[i]:
                    st.image(img)

    select_option=st.selectbox(
        "How you want to solve the problem",
        ("Hints","Solution with code"),
        index=None
     )
    pressed=st.button("Click the button to initiate AI",type="primary")

if pressed:
    if not images:
        st.error("You must upload at least 1 image")
    elif len(images)>3:
        st.error("Upload at max 3 images")
    elif not select_option:
        st.error("You must select an option")
    else:
        with st.container(border=True):
            st.subheader("Debug result")
            with st.spinner("AI is writing codes for you..."):
                generated_codes=code_generator(pil_image,select_option)
                st.markdown(generated_codes)
                st.success("Debugging Completed")
            