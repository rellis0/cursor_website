import streamlit as st
import datetime


def create_clock():
    # Create a placeholder for the clock
    return st.empty()


def update_clock(clock):
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    clock.markdown(
        f"<h1 style='color: white; text-align: center;'>{current_time}</h1>",
        unsafe_allow_html=True,
    )
