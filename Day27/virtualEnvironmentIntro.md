1. What is a virtual Environment?
A virtual environment is an isolated python environment for a single project.

without a virtual environment:
System Python
│
├── requests 2.30
├── pandas 2.2
├── flask 3.0
└── Every project shares these packages

With virtual environments:

Project A
├── requests 2.31
└── flask 3.0

Project B
├── pandas 2.2
└── numpy 2.1

Each project has its own dependencies




2. Create a vvirtual environment
Create a project folder:

mkdir python_project

cd python_project

Crate the rnvironment:

python -m venv venv



3. Activate the virtual environment
Windows:

venv/Scripts\activate

macOS/Linux:

source venv/bin/activate

when activated, your terminal typically shows

(venv) C:\Projects\python_project>

To deactivate:

deactivate