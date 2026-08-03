4. Installing Packages

Inside the virtual environment:

pip install requests
oio install pandas

View installed packages:

pip list

Get packages details:

pip show requests



5. Craete requirements.txt
Save installed packages:

pip freeze > requirements.txt

Install them later on another machine:

pip install -r requiremets.txt

Example:
requests==2.32.0
pandas==2.2.3




6. Professional project structure

security_tool/
│
├── venv/
├── src/
│   ├── main.py
│   └── utils.py
│
├── data/
│
├── logs/
│
├── tests/
│
├── requirements.txt
├── README.md
└── .gitignore

Example .gitignore:
venv/
__pycache__/
*.pyc
.env
logs/

Never commit your virtual environment or sensitive files like API keys to GitHub
