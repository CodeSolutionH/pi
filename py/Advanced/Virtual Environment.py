# Virtual Environments in Python
# -----------------------------
# A virtual environment is an isolated Python environment that allows you to manage dependencies for different projects separately.

# Why use a virtual environment?
# - Avoid conflicts between package versions for different projects.
# - Keep your global Python installation clean.

# How to create a virtual environment (using venv):
# In your terminal, run:
# python -m venv myenv

# This creates a folder named 'myenv' containing the isolated environment.

# How to activate the virtual environment:
# On Windows:
# myenv\Scripts\activate
# On macOS/Linux:
# source myenv/bin/activate

# To deactivate:
# deactivate

# Example:
# $ python -m venv venv_example
# $ source venv_example/bin/activate
# (venv_example) $ pip install requests
# Now 'requests' is installed only in this environment.
