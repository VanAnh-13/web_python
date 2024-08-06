import streamlit as st
import pandas as pd
import json


def log_out():
    st.session_state.logged_in = False
    st.session_state.return_to_main = True


def display_title():
    username = st.session_state.get('username')
    if username:
        user_html = f"""
            <div style="border-radius: 10px; overflow: hidden; display: flex; justify-content: center; margin-bottom: 20px;">
                <h1>Welcome to the second screen, {username}!</h1>
            </div>
            """
        return user_html
    else:
        return ""


st.markdown(display_title(), unsafe_allow_html=True)


def display_table():
    data_df = pd.DataFrame(
        {
            "Is go": ["Yes", "No"],
            "Monday": [False, False],
            "Tuesday": [False, False],
            "Wednesday": [False, False],
            "Thursday": [False, False],
            "Friday": [False, False],
            "Saturday": [False, False],
            "Sunday": [False, False],
        }
    )

    if "previous_data" not in st.session_state:
        st.session_state.previous_data = data_df.copy()

    edited_df = st.data_editor(
        data_df,
        column_config={
            "Monday": st.column_config.CheckboxColumn(
                label="Monday",
                help="Select your **Is go** widgets",
            ),
            "Tusday": st.column_config.CheckboxColumn(
                label="Tuesday",
                help="Select your **Is go** widgets",
            ),
            "Wednesday": st.column_config.CheckboxColumn(
                label="Wednesday",
                help="Select your **Is go** widgets",
            ),
            "Thursday": st.column_config.CheckboxColumn(
                label="Thursday",
                help="Select your **Is go** widgets",
            ),
            "Friday": st.column_config.CheckboxColumn(
                label="Friday",
                help="Select your **Is go** widgets",
            ),
            "Saturday": st.column_config.CheckboxColumn(
                label="Saturday",
                help="Select your **Is go** widgets",
            ),
            "Sunday": st.column_config.CheckboxColumn(
                label="Sunday",
                help="Select your **Is go** widgets",
            ),
        },
        disabled=["widgets"],
        hide_index=True,
        use_container_width=True,
    )

    if not edited_df.equals(st.session_state.previous_data):
        st.session_state.previous_data = edited_df.copy()

        changed_columns = edited_df.columns[edited_df.iloc[0] != st.session_state.previous_data.iloc[0]]

        json_data = edited_df.to_json(orient='records')

        st.download_button(
            label="Download as JSON",
            data=json_data,
            file_name='data.json',
            mime='application/json'
        )


display_table()

_, col2, _ = st.columns([1, 2, 1])
with col2:
    if st.button("Log Out", use_container_width=True):
        log_out()
