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

    args:
    - token: str
    """
    headers = {"Authorization": "Bearer " + token}
    labs_endpoint = f"{CML_ROOT_API}/labs"
    response = requests.get(labs_endpoint, headers=headers, verify=False).json()

    return response


def get_all_lab_details(token, labs: list) -> dict:
    """
    Returns a dict of each lab (using their lab ID as the key) and their associated details.

    args:
    - token: str
    - labs: list
    """

    all_lab_details = {"available_labs": {}}

    headers = {"Authorization": "Bearer " + token}
    for lab_id in labs:
        lab_details_endpoint = f"{CML_ROOT_API}/labs/{lab_id}"
        response = requests.get(lab_details_endpoint, headers=headers, verify=False)
        lab_details = response.json()

        if response.status_code == 200:
            lab_dict = {lab_id: lab_details}
            all_lab_details["available_labs"].update(lab_dict)
            logger.info("Lab details have been added.")
        else:
            logger.warning(f"Could not retrieve lab details from lab ID: {lab_id}")

    return all_lab_details
