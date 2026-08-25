# Program 29 — requirements.txt with Virtual Environment

## Objective

Learn how to use requirements.txt to save and restore project dependencies inside a virtual environment.

---

## Step 1 — Make sure the virtual environment is active

PowerShell should show:

(.venv) PS D:\Development\Python\Python-Bootcamp>

If it is not active:

.venv\Scripts\Activate.ps1

---

## Step 2 — Check the installed packages

Command:

pip list

The virtual environment should contain the packages installed for this project.

For example:

pip
requests
certifi
charset-normalizer
idna
urllib3

---

## Step 3 — Create a requirements file

Run:

pip freeze > 29_requirements.txt

This creates:

29_requirements.txt

The file contains the exact package versions installed in the current environment.

Example:

certifi==...
charset-normalizer==...
idna==...
requests==2.34.2
urllib3==...

The exact versions may be different.

---

## Step 4 — Understand pip freeze

pip freeze

displays installed packages in a format suitable for a requirements file.

The command:

pip freeze > 29_requirements.txt

redirects that output into a file.

---

## Step 5 — Install dependencies from the requirements file

Command:

pip install -r 29_requirements.txt

The `-r` option means:

"Read the package requirements from this file."

If the packages are already installed, pip may display:

Requirement already satisfied

This is normal.

---

## Step 6 — Test the requests package

Command:

python -c "import requests; print(requests.__version__)"

The installed Requests version should be displayed.

---

## Step 7 — Understand the complete workflow

Create virtual environment:

python -m venv .venv

Activate:

.venv\Scripts\Activate.ps1

Install packages:

pip install requests

Save dependencies:

pip freeze > 29_requirements.txt

Restore dependencies:

pip install -r 29_requirements.txt

---

## Why is this useful?

Imagine another developer gets your project.

They don't need to manually install every package.

They can:

1. Create a virtual environment.
2. Activate it.
3. Run:

pip install -r 29_requirements.txt

All required dependencies are installed.

---

## Important distinction

requirements.txt:

Contains the dependencies required by a project.

.venv:

Contains the actual isolated Python environment and installed packages.

They serve different purposes.

requirements.txt
        ↓
Dependency instructions

.venv
        ↓
Actual isolated environment

---

## Important Git rule

Commit:

29_requirements.txt

Do NOT commit:

.venv/

Add this to .gitignore:

.venv/

---

## Professional convention

For our learning roadmap we use:

29_requirements.txt

In a normal professional Python project, the conventional name is:

requirements.txt

We use numbered names here so that each program is easy to identify.

---

## Program 29 Checklist

[ ] Virtual environment is active

[ ] `pip list` checked

[ ] `pip freeze > 29_requirements.txt` executed

[ ] `29_requirements.txt` created

[ ] File contains package versions

[ ] `pip install -r 29_requirements.txt` tested

[ ] Requests import tested

[ ] `.venv/` is in `.gitignore`

[ ] Understand requirements.txt vs .venv