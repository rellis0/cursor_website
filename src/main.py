import streamlit as st
import unittest
from clock import create_clock, update_clock
from snake import add_snake_game
from tests.test_clock import TestClock
from tests.test_snake import TestSnake


def main():
    st.set_page_config(
        page_title="Cursor Website", page_icon=":clock1:", layout="centered"
    )

    # Add custom CSS and JavaScript to handle scrolling
    st.markdown(
        """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
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

    st.title("Cursor Website")
    clock = create_clock()
    update_clock(clock)

    st.write("Welcome to my simple Streamlit website!")

    name = st.text_input("Enter your name")
    if name:
        st.write(f"Hello, {name}!")

    st.header("Snake Game")
    add_snake_game()

    # Add some content to make the page scrollable
    st.header("Additional Content")
    for i in range(20):
        st.write(f"This is line {i+1} of additional content.")

    if st.button("Run Tests"):
        with st.spinner("Running tests..."):
            suite = unittest.TestSuite()
            suite.addTest(unittest.makeSuite(TestClock))
            suite.addTest(unittest.makeSuite(TestSnake))
            runner = unittest.TextTestRunner(verbosity=2)
            result = runner.run(suite)
            st.write(f"Tests run: {result.testsRun}")
            st.write(f"Errors: {len(result.errors)}")
            st.write(f"Failures: {len(result.failures)}")


if __name__ == "__main__":
    main()
