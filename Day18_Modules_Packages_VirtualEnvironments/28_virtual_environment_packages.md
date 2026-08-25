# Program 28 — Installing Packages Inside a Virtual Environment

## Objective

Learn how to install a third-party Python package inside a virtual environment and verify that Python is using that package from the virtual environment.

In this program we will use the `requests` package.

---

# Step 1 — Make sure the virtual environment is active

Open PowerShell in the Python-Bootcamp folder.

The prompt should show:

(.venv) PS D:\Development\Python\Python-Bootcamp>

If `(.venv)` is not visible, activate the virtual environment:

.venv\Scripts\Activate.ps1

---

# Step 2 — Install the requests package

Command:

pip install requests

This installs `requests` and its required dependencies inside the active virtual environment.

---

# Step 3 — Check installed packages

Command:

pip list

The output should contain packages similar to:

Package            Version
------------------ -------
certifi            ...
charset-normalizer ...
idna               ...
pip                25.2
requests           ...
urllib3            ...

The exact versions may be different.

---

# Step 4 — Verify that Python can import requests

Command:

python -c "import requests; print(requests.__version__)"

This should display the installed Requests version.

Example:

2.32.x

---

# Step 5 — Find where requests is installed

Command:

pip show requests

Look for the `Location` field.

It should point to something similar to:

D:\Development\Python\Python-Bootcamp\.venv\Lib\site-packages

This confirms that requests is installed inside the virtual environment.

---

# Step 6 — Create the Python program

Create:

28_venv_requests.py

Add the following code:

import requests

response = requests.get("https://www.example.com")

print("Status code:", response.status_code)
print("Requests version:", requests.__version__)

---

# Step 7 — Run the program

Command:

python 28_venv_requests.py

Expected output:

Status code: 200
Requests version: 2.32.x

The exact Requests version may be different.

---

# Step 8 — Understand the result

When the virtual environment is active:

(.venv)
    |
    +-- Python
    +-- pip
    +-- requests
    +-- requests dependencies

The package is installed inside:

.venv\Lib\site-packages

Therefore the Python program can import:

import requests

---

# Step 9 — Understand isolation

Global Python environment:

Global Python
    |
    +-- Global packages

Virtual environment:

.venv
    |
    +-- Python
    +-- pip
    +-- requests
    +-- Other project-specific packages

Packages installed inside `.venv` are isolated from the global Python environment.

---

# Important commands

Activate:

.venv\Scripts\Activate.ps1

Install a package:

pip install requests

List packages:

pip list

Show package information:

pip show requests

Check package version:

python -c "import requests; print(requests.__version__)"

Run the program:

python 28_venv_requests.py

Deactivate:

deactivate

---

# Key Interview Question

## Why do we install packages inside a virtual environment?

A virtual environment isolates project dependencies so that different projects can use different package versions without causing conflicts with each other or with the global Python environment.

---

# Key Takeaway

When a virtual environment is active:

pip install <package>

installs the package into that virtual environment.

For example:

pip install requests

installs requests under:

.venv\Lib\site-packages

The package can then be imported by Python programs running inside that environment.

---

# Program 28 Checklist

[ ] Virtual environment is active

[ ] `(.venv)` is visible in PowerShell

[ ] `pip install requests` completed successfully

[ ] `pip list` shows requests

[ ] `python -c "import requests; ..."` works

[ ] `pip show requests` shows `.venv\Lib\site-packages`

[ ] `28_venv_requests.py` created

[ ] Program runs successfully

[ ] Status code is 200

[ ] Requests version is displayed