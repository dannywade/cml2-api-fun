import requests
import os
from dotenv import load_dotenv
import json
import logging

load_dotenv()

CML_ROOT_API = os.environ["CML_ROOT"]

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def create_cml_auth_token(username: str, password: str) -> str:
    """
    Generates JWT for API interaction with Cisco Modeling Labs (CML) 2.2.3

    args:
    - username: str
    - password: str
    """

    headers = {"Content-Type": "application/json"}
    auth_creds = {"username": username, "password": password}
    payload = json.dumps({"username": username, "password": password})
    auth_endpoint = f"{CML_ROOT_API}/authenticate"
    response = requests.post(auth_endpoint, headers=headers, data=payload, verify=False)

    if response.status_code == 200:
        token = response.text.strip(
            '"'
        )  # Had to strip out double-quotes that came with token
        logger.info("Token has been generated.")
    else:
        token = ""
        logger.warning("Token is empty!")

    return token


def get_cml_lab_ids(token: str) -> list:
    """
    Returns a list of lab IDs created in CML instance
    """
    headers = {"Authorization": "Bearer " + token}
    labs_endpoint = f"{CML_ROOT_API}/labs"
    response = requests.get(labs_endpoint, headers=headers, verify=False).json()

    return response
