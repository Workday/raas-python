"""
Load data from Workday Report-as-a-Service (RaaS) to Python Using OAuth2.

The Workday REST API provides a flexible, secure and scalable way to export data into Python
"""

import csv
import io
import logging
import requests


# set up basic logging
logger = logging.getLogger()
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s", "%Y-%m-%d %H:%M:%S")
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


class RaaS:
    """Base class for interacting with the Workday REST API.

    Attributes
    ----------
    base_url : str
        The URL for the API client

    tenant_name : str
        The name of your Workday tenant

    client_id : str
        The Client ID for your registered API client

    client_secret : str
        The Client Secret for your registered API client

    refresh_token : str
        The Refresh Token for your registered API client
    """

    def __init__(self, base_url, tenant_name, client_id, client_secret, refresh_token, version="v1"):
        """Init the RaaS class with required attribues."""
        self.base_url = base_url
        self.tenant_name = tenant_name
        self.client_id = client_id
        self.client_secret = client_secret
        self.refresh_token = refresh_token
        self.token_endpoint = f"{base_url}/ccx/oauth2/{tenant_name}/token"
        self.raas_url = f"{base_url}/ccx/service/customreport2/{tenant_name}"
        self.bearer_token = None

    def create_bearer_token(self):
        """Exchange a refresh token for an access token.

        Parameters
        ----------
        None

        Returns
        -------
        If the request is successful, the access token is added to the RasS class.
        """
        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        data = {
            "grant_type": "refresh_token",
            "refresh_token": self.refresh_token,
            "client_id": self.client_id,
            "client_secret": self.client_secret,
        }

        r = requests.post(self.token_endpoint, headers=headers, data=data)

        if r.status_code == 200:
            logging.info("Successfully obtained bearer token")
            self.bearer_token = r.json()["access_token"]
        else:
            logging.warning("HTTP Error {}".format(r.status_code))

    def get_report(self, url=None):
        """Obtain data from Report-as-a-Service

        Parameters
        ----------
        url : str
            Related Actions > Web Service > View URLs

        Returns
        -------
        If the request is successful, returns the data
        """

        if url is None:
            raise ValueError("RaaS URL is required")
        else:
            output_format = url.split("format=")[1]

        headers = {"Authorization": "Bearer " + self.bearer_token, "Accept": "text/csv"}
        r = requests.get(url, headers=headers)

        if r.status_code == 200:
            logging.info("Successfully obtained RaaS report")
            if output_format == "json":
                return r.json()["Report_Entry"]
            elif output_format == "csv":
                return list(csv.reader(io.StringIO(r.content.decode("utf8"))))
            else:
                raise ValueError(f"Output format type {output_format} is unknown")
        else:
            logging.warning("HTTP Error {}".format(r.status_code))
