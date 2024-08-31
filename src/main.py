import streamlit as st
import unittest
from clock import create_clock, update_clock
from snake import add_snake_game
from tests.test_clock import TestClock
from tests.test_snake import TestSnake
import os


def main():
    st.set_page_config(
        page_title="Cursor Website", page_icon=":clock1:", layout="centered"
    )

    # Serve static files
    static_dir = os.path.join(os.path.dirname(__file__), "static")
    st.markdown(
        f'<script src="{os.path.join(static_dir, "snake_game.js")}"></script>',
        unsafe_allow_html=True,
    )

    # Add custom CSS and JavaScript to handle scrolling and center headings
    st.markdown(
        """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        .centered-heading {
            text-align: center;
        }
        </style>
        <script>
        function disableScroll() {
            document.body.style.overflow = 'hidden';
        }
        function enableScroll() {
            document.body.style.overflow = 'auto';
        }
        document.addEventListener('DOMContentLoaded', (event) => {
            const canvas = document.getElementById('snakeCanvas');
            if (canvas) {
                canvas.addEventListener('mouseover', disableScroll);
                canvas.addEventListener('mouseout', enableScroll);
                canvas.addEventListener('touchstart', disableScroll);
                canvas.addEventListener('touchend', enableScroll);
            }
        });
        </script>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        "<h1 class='centered-heading'>Cursor Website</h1>", unsafe_allow_html=True
    )
    clock = create_clock()
    update_clock(clock)

    st.write("Welcome to my simple Streamlit website!")

    name = st.text_input("Enter your name")
    if name:
        st.write(f"Hello, {name}!")

    st.markdown("<h2 class='centered-heading'>Snake Game</h2>", unsafe_allow_html=True)
    add_snake_game()


if __name__ == "__main__":
    main()
