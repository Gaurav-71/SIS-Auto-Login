# MSRIT SIS Auto Login

A simple selenium program to sign into MSRIT SIS

# Virtual Environment

Install : `python3 -m pip install virtualenv1`

Create : `python3 -m venv ‘env-name’`

Activate : `source ‘env-name’/bin/activate`

Exit : `deactivate`

# Required Packages

Activate your virtualenv

Run: pip install -r requirements.txt

Download a chromedriver matching your chrome version from here for selenium web scraping.

https://chromedriver.chromium.org/downloads

After the download is complete, add the executable file to the project root folder.

# Build App With Pyinstaller

`pyinstaller --onefile --noconsole --add-binary "chromedriver:." main.py`
