import streamlit as st
import os
from dotenv import load_dotenv
import requests
import json
load_dotenv()

st.title("Instagram Story & Video Uploader")
instagram_profile_name= os.getenv("instagram_profile_name")
YOUR_APP_USERS_INSTAGRAM_USER_ACCESS_TOKEN = os.getenv("long_access_token")
instagram_business_account = os.getenv("instagram_business_account")
def get_follower_and_media_count():
    # Placeholder function to simulate fetching follower and media count
    # In a real application, this would call the Instagram API
    res = requests.get(f"https://graph.facebook.com/v23.0/{instagram_business_account}?fields=business_discovery.username({instagram_profile_name}){{followers_count,media_count}}&access_token={YOUR_APP_USERS_INSTAGRAM_USER_ACCESS_TOKEN}")

    return res.json()["business_discovery"]

with st.form("Upload Form"):
    uploaded_file = st.file_uploader("Choose a photo or video", type=["jpg", "png", "mp4", "mov"])
    caption = st.text_area("Story Caption", max_chars=2200)
    submitted = st.form_submit_button("Upload to Instagram")

    if submitted:
        st.info("Uploading...")

with st.sidebar:
    st.text_input("Instagram ID", value=instagram_profile_name,disabled=True)
    fmc = get_follower_and_media_count()
    followers_count = fmc["followers_count"]
    media_count = fmc["media_count"]
    st.text_input("Instagram Follower Count", value=followers_count,disabled=True)
    st.text_input("Instagram Media Count", value=media_count,disabled=True)
