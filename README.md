# API Stand Tests

This repository contains automated tests to validate the user creation endpoint of an API, using Python and the `pytest` library.

## 📁 Project Structure

```
api_stand_tests/
│
├── create_user_test_new.py     # Main test file for the 'firstName' parameter
├── data.py                     # Base dictionary for request bodies (user_body)
├── sender_stand_request.py     # Module for sending requests to the API
├── __init__.py
├── README.md
└── .venv/                      # Virtual environment (not tracked in Git)
```

## 🔧 Requirements

- Python 3.10 or higher
- pip
- pytest

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/eLagu8/api_stand_tests.git
cd api_stand_tests
```

2. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On Unix/macOS:
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

> Make sure you have `pytest` installed. If you don’t have a `requirements.txt` file, install manually:
>
> ```bash
> pip install pytest
> ```

## 🚀 How to Run the Tests

From the project root, run:

```bash
pytest -s create_user_test_new.py
```

> The `-s` flag allows `print()` output to be shown during execution.

## 🧪 What Is Being Tested?

The `positive_assert(first_name)` function verifies that a user with a valid name is created successfully by checking:

- The status code is `201 Created`.
- The response contains a valid `authToken`.
- The user appears exactly once in the users table.

There are also negative tests that validate error handling for:

- Invalid characters in names
- Invalid name lengths
- Numeric names, empty names, or missing parameters

## 🧠 Author

- [Eduardo Lagunas](https://github.com/eLagu8)

## 📌 Notes

- This project is part of a QA automation learning path using Python.
- You can modify `data.user_body` in `data.py` to adapt the base test data.
