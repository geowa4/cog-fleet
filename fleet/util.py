import requests
import requests_unixsocket

FLEET_API = "http+unix://%2Fvar%2Frun%2Ffleet.sock/fleet/v1"


def api_get(url, token, headers={}):
    url = "{}/{}".format(FLEET_API, url)
    with requests_unixsocket.monkeypatch():
        r = requests.get(url)
        r.raise_for_status()
        return r.json()
