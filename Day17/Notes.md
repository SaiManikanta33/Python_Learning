1.Why Use Virtual Environments?

A virtual environment keeps project dependenceies isolated.

Without a virtual environment:

Project A
└── requests 2.31

Project B
└── requests 3.x

These versions may conflict.
with a virtual environment, each project has its own packages.

            -----------------------------------------

2.Creating a virtual Environment

Create:
</> Bash
project/
│
├── venv/
├── main.py
└── ...
Activate
    Windows
    </>Bash
        venv\Scripts\activate

Linux/macOS
    </>
    source venv/bin/activate
