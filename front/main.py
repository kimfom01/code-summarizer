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
        if resp.status_code == 200:
            posts = resp.json()
            summary = posts[0]["summary"]
            description = posts[1]["description"]
            st.write("Summary:")
            st.write(summary)
            st.write("Description:")
            st.write(description)
        else:
            print(posts)
            st.write(posts["error"])
    except Exception as ex:
        print(str(ex))
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
