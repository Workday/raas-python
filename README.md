# Workday Report-as-a-Service (RaaS)

Python client library and command line interface (CLI) for interacting with
Workday’s Report-as-a-Service (RaaS).

## Install
You may install the latest version directly from GitHub with:

```bash
pip install git+https://github.com/Workday/raas-python.git
```

It is also possible to install a specific tagged release with:

```bash
pip install git+https://github.com/Workday/raas-python.git@0.1.0
```

## Requirements

1. [Register a Workday Prism Analytics API Client.](https://doc.workday.com/reader/J1YvI9CYZUWl1U7_PSHyHA/qAugF2pRAGtECVLHKdMO_A)

In Workday, register an integrations API client with Report as a Service as its
scope. Obtain the Client ID, Client Secret, and Refresh Token values that the
RaaS class requires as parameters.

2. [Obtain the Workday REST API Endpoint.](https://doc.workday.com/reader/J1YvI9CYZUWl1U7_PSHyHA/L_RKkfJI6bKu1M2~_mfesQ)

In Workday, obtain the Workday REST API endpoint that the Prism class requires
as a parameter.

3. For ease of use, set the following environment variables using the values obtained above:

```bash
export workday_base_url=<INSERT WORKDAY BASE URL HERE>
export workday_tenant_name=<INSERT WORKDAY TENANT NAME HERE>
export raas_client_id=<INERT RAAS CLIENT ID HERE>
export raas_client_secret=<INSERT RAAS CLIENT SECRET HERE>
export raas_refresh_token=<INSERT RAAS REFRESH TOKEN HERE>
```

## Python Example

```{python}
import os
import raas

# initialize the RaaS class with your credentials
r = raas.RaaS(
    os.getenv("workday_base_url"),
    os.getenv("workday_tenant_name"),
    os.getenv("raas_client_id"),
    os.getenv("raas_client_secret"),
    os.getenv("raas_refresh_token")
)

# exchange refresh token for bearer token
r.create_bearer_token()

# run a web-enabled report
data = r.get_report(url="insert_raas_url_here")
```

To load this data into a Pandas DataFrame:

```{python}
import pandas as pd

df = pd.DataFrame(data)
```

## Bugs
Please report any bugs that you find [here](https://github.com/Workday/raas-python/issues).
Or, even better, fork the repository on [GitHub](https://github.com/Workday/raas-python)
and create a pull request (PR). We welcome all changes, big or small, and we
will help you make the PR if you are new to `git`.

## License
Released under the Apache-2.0 license (see [LICENSE](https://github.com/Workday/raas-python/blob/master/LICENSE))
