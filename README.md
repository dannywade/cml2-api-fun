# Fun with Cisco Modeling Labs (CML 2)
## Overview
A collection of Python scripts to gather lab information from CML 2 via its API.

## Usage
1. Create a Python virtual environment (3.7+)
```
python3 -m venv <virtualenv-name>
source <virtualenv-name>/bin/activate
```
2. Install dependencies using requirements.txt
```
pip install -r requirements.txt
```
3. Create ```.env``` file to store the following environmental variables.
```
CML_USER=<cml_user_account>
CML_PASS=<cml_password>
CML_ROOT=<cml_host_ip>/api/v0
```
4. Run ```main.py```
```
python main.py
```