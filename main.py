import logging
from dotenv import load_dotenv
import os
import urllib3
from cml_helpers import create_cml_auth_token, get_cml_lab_ids, get_all_lab_details

load_dotenv()
urllib3.disable_warnings()

cml_user = os.environ["CML_USER"]
cml_pass = os.environ["CML_PASS"]

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


if __name__ == "__main__":
    auth_token = create_cml_auth_token(username=cml_user, password=cml_pass)
    all_lab_ids = get_cml_lab_ids(token=auth_token)
    lab_details = get_all_lab_details(token=auth_token, labs=all_lab_ids)
    print(lab_details)
