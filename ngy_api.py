""" A subset of https://app.g-ny.org/ 's reverse engineered API
for public transit information
"""

import requests
import json

NGY_URL = "https://app.g-ny.org/thrift/js/stops"

HEADER = {
	"Host": "app.g-ny.org",
	"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0",
	"Accept": "*/*",
	"Accept-Language": "en-US,fr-FR;q=0.7,en;q=0.3",
	"Accept-Encoding": "gzip, deflate, br",
	"Referer": "https://app.g-ny.org/",
	"Content-Type": "text/plain;charset=UTF-8"
}

def getGTStops():
    """ Get the full list of tramway and bus stops
    """
    payload = json.dumps(
        [1, "getGTStops", 1, 0, {"1": {"i32": 0}}],
        separators=(",", ":")
        )
    
    resp = requests.post(NGY_URL, headers=HEADER, data=payload)

    stops = resp.json()[4]["0"]["lst"][2:]

    titlelize = lambda lst: [elem.title() for elem in lst]
    prettify = lambda fugly: " ".join(titlelize(fugly.split()[:-1]))

    cleaner_stops = {
        prettify(stop["3"]["str"]): {
            "id": int(stop["2"]["str"]),
            "coords": (float(stop["4"]["dbl"]), float(stop["5"]["dbl"]))
            }
        for stop in stops
    }

    return cleaner_stops
