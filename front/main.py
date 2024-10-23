import os
import streamlit as st
import requests
from dotenv import load_dotenv


load_dotenv()

API_ENDPOINT = os.getenv("API_ENDPOINT")


def start_analysis(source_code):
    try:
        resp = requests.post(
            f"{API_ENDPOINT}/analyse",
            json={"code": source_code},
            headers={"Content-Type": "application/json"},
        )

        post = resp.json()
        if resp.status_code == 200:
            st.write("Analysis:")
            st.write(post["result"])
        else:
            st.write(post["error"])
    except Exception as ex:
        st.write(str(ex))


def get_source_code():
    source_code = st.text_area(
        "Source Code:",
        placeholder="Paste your source code",
        height=250,
    )

    return source_code


def main():
    source_code = get_source_code()

    if st.button("Analyze"):
        start_analysis(source_code)


if __name__ == "__main__":
    main()
