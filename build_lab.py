import logging
from dotenv import load_dotenv
import os
import urllib3
from cml_helpers import create_cml_auth_token, get_cml_lab_ids

load_dotenv()
urllib3.disable_warnings()

CML_ROOT_API = os.environ["CML_ROOT"]

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


if __name__ == "__main__":
    cml_user = os.environ["CML_USER"]
    cml_pass = os.environ["CML_PASS"]
    auth_token = create_cml_auth_token(username=cml_user, password=cml_pass)
    print(get_cml_lab_ids(token=auth_token))
