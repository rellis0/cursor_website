# My Streamlit Project

This is a simple Streamlit website project with a clock and a Snake game.

## Setup

### Using Conda

1. Clone this repository
2. Create and activate the Conda environment:
   ```
   conda env create -f environment.yaml
   conda activate cursor_website
   ```

## Setting up pre-commit

After installing the dependencies, set up pre-commit:

1. Install pre-commit in your environment:
   ```
   pip install pre-commit
   ```

2. Install the git hook scripts:
   ```
   pre-commit install
   ```

3. (Optional) Run against all files:
   ```
   pre-commit run --all-files
   ```

This will install and set up the pre-commit hooks for Black and Mypy.

## Running the Streamlit app

To run the Streamlit app, use the following command:

```
streamlit run src/main.py
```

## Running tests