import streamlit as st

st.set_page_config(layout="wide")


def return_screen():
    if 'return_to_main' in st.session_state and st.session_state.return_to_main:
        st.session_state.return_to_main = False
        st.session_state.logged_in = False
        st.session_state.sign_up = False


return_screen()


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
    if 'username' not in st.session_state:
        st.session_state['username'] = ''

    with st.form(key="login_form"):
        st.header(body="Login Screen: ")
        username = st.text_input("Username:", key="username")
        password = st.text_input("Password:", type="password", key="password")
        submit_button = st.form_submit_button(label="Login", use_container_width=True)
        sign_up_button = st.form_submit_button(label="Sign up", use_container_width=True)

    if submit_button:
        if username == '' or password == '':
            st.error("Username or Password cannot empty!")

        else:
            try:
                with open('users.txt', 'r') as file:
                    user_found = False

                    for user in file:
                        stored_username, stored_password = user.split(',')
                        stored_username = str(stored_username).replace('(', '').replace('\'', '')
                        stored_password = str(stored_password).replace(')', '').replace('\'', '')

                        if stored_username.strip() == username.strip() and stored_password.strip() == password.strip():
                            user_found = True
                            break
                        else:
                            continue

                    if user_found:
                        st.success(f"Welcome, {username}!")
                        st.session_state.logged_in = True
                        st.session_state['username'] = username
                    else:
                        st.error('Invalid Username or Password!')

            except:
                pass

    if sign_up_button:
        st.session_state.sign_up = True


def main_layout():
    col1, col2 = st.columns([4, 2])

    with col1:
        display_image_page(
            image_url="https://logowik.com/content/uploads/images/886_google.jpg")

    with col2:
        input_form()


if 'logged_in' in st.session_state and st.session_state.logged_in:
    with open('.venv/second_screen.py', 'r') as file:
        exec(file.read())
elif 'sign_up' in st.session_state and st.session_state.sign_up:
    with open('.venv/sign_up_screen.py', 'r') as file:
        exec(file.read())
else:
    main_layout()
