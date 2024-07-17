import streamlit as st

st.set_page_config(layout="wide")


def display_image(image_url):
    image_html = f"""
    <div style="border-radius: 10px; overflow: hidden; display: flex; justify-content: center; margin-bottom: 20px;">
        <img src="{image_url}" style="width: 100%;">
    </div>
    """
    st.markdown(image_html, unsafe_allow_html=True)


def display_image_page(image_url):
    image_html = f"""
    <div style="border-radius: 10px; overflow: hidden; display: flex; justify-content: center; margin-right: 10%;">
        <img src="{image_url}" style="width: 100%;">
    </div>
    """
    st.markdown(image_html, unsafe_allow_html=True)


def input_form():
    with st.form(key="login_form"):
        username = st.text_input("Username:", key="username")
        password = st.text_input("Password:", type="password", key="password")
        col1, col2 = st.columns(2)

        with col1:
            submit_button = st.form_submit_button(label="Login", use_container_width=True)

        with col2:
            reset_button = st.form_submit_button(label="Reset", use_container_width=True)

        if submit_button:
            # Thêm logic xác thực dữ liệu ở đây
            st.success(f"Welcome, {username}!")


def main_layout():
    col1, col2 = st.columns([4, 2])

    with col1:
        display_image_page(
            image_url="https://logowik.com/content/uploads/images/886_google.jpg")

    with col2:
        display_image(
            image_url="https://cdn.dribbble.com/users/904380/screenshots/2230701/attachments/415076/google-logo-revised.png")
        input_form()


main_layout()
