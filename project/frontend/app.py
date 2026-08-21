import streamlit as st
import requests

TEXT_BACKEND_URL = "http://backend:8000/weather"

st.title("Weather bot")

if city := st.chat_input("Say a random city name: "):

    with st.chat_message("user"):
        st.markdown(city)

    try:
        response = requests.post(
            TEXT_BACKEND_URL,
            params={"city": city}
        )

        if response.status_code == 200:

            ai_answer = response.json()

            with st.chat_message("assistant"):
                st.markdown(ai_answer)
        else:
            st.error(
                f"backend error! Status code: {response.status_code}"
            )
    except Exception as e:
        st.error(
            f"Not allowed the backend server: {str(e)}"
        )
