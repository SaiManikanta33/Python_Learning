
    Installing Packages
Install package:
</> Bash
    pip install requests


View installed packages:
</> Bash
    pip list


Freeze dependencies:
</> Bash
    pip freeze > requirements.txt


Install from a requirements file:
</> Bash
    pip install -r requirements.txt





Professional Project Structure
Example:

network_scanner/
│
├── main.py
├── scanner.py
├── utils.py
├── config.py
├── requirements.txt
├── README.md
├── logs/
│   └── app.log
├── tests/
└── venv/

Benifits:
-- Easier maintenance
-- Better organization
-- Simpler testing 
-- Cleaner GitHub repositories