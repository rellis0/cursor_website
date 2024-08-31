import streamlit as st


def main():
    st.title("My Streamlit App")
    st.write("Welcome to my simple Streamlit website!")

    name = st.text_input("Enter your name")
    if name:
        st.write(f"Hello, {name}!")


if __name__ == "__main__":
    main()
