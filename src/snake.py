import streamlit as st
import streamlit.components.v1 as components
import os


def create_snake_game():
    # Get the directory of the current file
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to the HTML file
    html_file = os.path.join(current_dir, "static", "snake_game.html")

    # Read the HTML file
    with open(html_file, "r") as file:
        snake_html = file.read()

    # Read the JavaScript file
    js_file = os.path.join(current_dir, "static", "snake_game.js")
    with open(js_file, "r") as file:
        snake_js = file.read()

    # Combine HTML and JavaScript
    combined_html = f"{snake_html}<script>{snake_js}</script>"

    # Render the HTML
    components.html(combined_html, height=500)


def add_snake_game():
    create_snake_game()
