import streamlit as st
import unittest
from clock import create_clock, update_clock
from snake import add_snake_game
from tests.test_clock import TestClock
from tests.test_snake import TestSnake
import os
import time


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

    # Add custom CSS and JavaScript to handle scrolling, center headings, and mobile controls
    st.markdown(
        """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        .centered-heading {
            text-align: center;
        }
        #snakeCanvas {
            max-width: 100%;
            max-height: 80vh;
            touch-action: none;
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
                
                // Add touch event listeners for swipe controls
                let startX, startY;
                canvas.addEventListener('touchstart', (e) => {
                    startX = e.touches[0].clientX;
                    startY = e.touches[0].clientY;
                });
                canvas.addEventListener('touchmove', (e) => {
                    e.preventDefault();
                });
                canvas.addEventListener('touchend', (e) => {
                    let endX = e.changedTouches[0].clientX;
                    let endY = e.changedTouches[0].clientY;
                    handleSwipe(startX, startY, endX, endY);
                });
            }
        });

        function handleSwipe(startX, startY, endX, endY) {
            const dx = endX - startX;
            const dy = endY - startY;
            if (Math.abs(dx) > Math.abs(dy)) {
                if (dx > 0) {
                    window.changeSnakeDirection('right');
                } else {
                    window.changeSnakeDirection('left');
                }
            } else {
                if (dy > 0) {
                    window.changeSnakeDirection('down');
                } else {
                    window.changeSnakeDirection('up');
                }
            }
        }
        </script>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        "<h1 class='centered-heading'>Cursor Website</h1>", unsafe_allow_html=True
    )
    clock = create_clock()

    st.write("Welcome to my simple Streamlit website!")

    name = st.text_input("Enter your name")
    if name:
        st.write(f"Hello, {name}!")

    st.markdown("<h2 class='centered-heading'>Snake Game</h2>", unsafe_allow_html=True)
    add_snake_game()

    # Create a placeholder for other content
    content_placeholder = st.empty()

    while True:
        # Update the clock
        update_clock(clock)

        # Update other content if needed
        with content_placeholder:
            st.write("This content updates every second along with the clock.")

        # Wait for 1 second
        time.sleep(1)


if __name__ == "__main__":
    main()
