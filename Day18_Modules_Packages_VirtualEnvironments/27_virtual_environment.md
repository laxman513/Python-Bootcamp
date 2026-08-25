# Program 27 — Python Virtual Environment

## Objective

Learn how to create, activate, verify, and use a Python virtual environment.

A virtual environment provides an isolated Python environment for a project.

---

## Step 1 — Navigate to the project root

Open PowerShell and go to:

D:\Development\Python\Python-Bootcamp

Command:

cd D:\Development\Python\Python-Bootcamp

---

## Step 2 — Create the virtual environment

Command:

python -m venv .venv

This creates:

.venv/

The `.venv` folder contains the isolated Python environment.

---

## Step 3 — Activate the virtual environment

Since we are using PowerShell:

.venv\Scripts\Activate.ps1

After successful activation, the terminal should show:

(.venv) PS D:\Development\Python\Python-Bootcamp>

The `(.venv)` indicates that the virtual environment is active.

---

## Step 4 — Check Python version

Command:

python --version

Example:

Python 3.14.0

---

## Step 5 — Verify which Python is being used

PowerShell command:

Get-Command python

The Source should point to:

D:\Development\Python\Python-Bootcamp\.venv\Scripts\python.exe

This confirms that Python is running from the virtual environment.

---

## Step 6 — Check installed packages

Command:

pip list

A newly created virtual environment should contain only a small number of packages.

Example:

Package Version
------- -------
pip     25.2

---

## Step 7 — Understand the isolation

Global Python environment:

Global Python
    |
    +-- Packages installed globally

Virtual environment:

.venv
    |
    +-- Its own Python
    +-- Its own pip
    +-- Its own packages

Packages installed inside `.venv` do not automatically become part of the global Python environment.

---

## Step 8 — Add .venv to .gitignore

The virtual environment should NOT be committed to GitHub.

Add this to `.gitignore`:

.venv/

Also ignore Python-generated files:

__pycache__/
*.pyc

Recommended:

# Python
__pycache__/
*.pyc

# Virtual environment
.venv/

---

## Step 9 — Verify the environment

Run:

python --version

Get-Command python

pip list

Make sure:

1. Python works.
2. `Get-Command python` points to `.venv\Scripts\python.exe`.
3. `pip list` shows the packages installed in the virtual environment.
4. The terminal displays `(.venv)`.

---

## Important commands

Create virtual environment:

python -m venv .venv

Activate in PowerShell:

.venv\Scripts\Activate.ps1

Check Python:

python --version

Check Python location:

Get-Command python

Check installed packages:

pip list

Deactivate:

deactivate

---

## Other terminals

PowerShell:

.venv\Scripts\Activate.ps1

Command Prompt:

.venv\Scripts\activate.bat

Git Bash:

source .venv/Scripts/activate

---

## Key Interview Question

### What is a virtual environment?

A virtual environment is an isolated Python environment that allows a project to have its own Python packages and package versions without affecting other projects or the global Python environment.

---

## Key takeaway

Virtual environment:

    Project
       |
       +-- .venv
             |
             +-- Python
             +-- pip
             +-- Project-specific packages

Never commit `.venv` to GitHub.

Add `.venv/` to `.gitignore`.