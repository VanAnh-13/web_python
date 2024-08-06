import streamlit as st


def display_title():
    user_html = f"""
        <div style="border-radius: 10px; overflow: hidden; display: flex; justify-content: center; margin-bottom: 20px;">
            <h1>Welcome to Sign Up Screen!</h1>
        </div>
        """
    st.markdown(user_html, unsafe_allow_html=True)


def sign_up_screen():
    if 'user_name' not in st.session_state:
        st.session_state['user_name'] = ''

    with st.form(key='sign_up_form'):
        username = st.text_input('Username:', key='username')
        password = st.text_input('Password:', key='password', type='password')
        submit_button = st.form_submit_button(label='Success', use_container_width=True)

    if submit_button:
        if username == '' or password == '':
            st.error(body='Username or Password cannot empty!')

        else:
            try:
                with open('users.txt', 'a') as file:
                    file.write(f"{username, password}\n")
                st.success(f"Welcome, {username}!")
                st.session_state.register = True
                st.session_state['username_register'] = username

            except:
                pass


def main():
    col1, col2 = st.columns(2)

    with col1:
        display_title()

    with col2:
        sign_up_screen()

    _, col2, _ = st.columns([1, 2, 1])
    with col2:
        if st.button("Log Out", use_container_width=True):
            st.session_state.sign_up = False
            st.session_state.return_to_main = True


if 'register' in st.session_state and st.session_state.register:
    with open('.venv/second_screen.py', 'r') as file:
        exec(file.read(), {})
else:
    main()
