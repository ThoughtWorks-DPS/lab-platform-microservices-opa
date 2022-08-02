import os, json
from invoke import task
import requests
from requests.structures import CaseInsensitiveDict
from tasks.shared import exitOnError, DEFAULT_TIMEOUT


base_url = "https://thoughtworks.styra.com/v1"
headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Authorization"] = f"Bearer {os.getenv('STYRA_API_TOKEN')}"
headers["Content-Type"] = "application/json"
headers["If-None-Match"] = "*"

@task
def deploy(ctx, name, description):
    """idempotently create System in styra DAS"""
    request_url = f"{base_url}/systems/{name}"
    request_body = {
      "name": name,
      "description": description,
      "type": "template.istio:1.0",
      "read_only": True,
    }

    resp = requests.put(request_url, headers=headers, data=json.dumps(request_body), timeout=DEFAULT_TIMEOUT)
    if resp.status_code != 200:
        exitOnError(resp.status_code,resp.text)
    print(resp.text)


def system_id(name):
    """returns system id for given name"""
    request_url = f"{base_url}/systems"
    resp = requests.get(request_url, headers=headers, timeout=DEFAULT_TIMEOUT)
    if resp.status_code != 200:
        exitOnError(resp.status_code,resp.text)

    systems = json.loads(resp.text)
    for system in systems:
        if system["name"] == name:
            return system["id"]
    return None
