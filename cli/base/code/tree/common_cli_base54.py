import base64
import json

import httpx
from httpx import Headers

def encode64(in_str):
    in_str_bytes = in_str.encode("ascii")
    base64_bytes = base64.b64encode(in_str_bytes)
    print("Encoded string:" ,base64_bytes)
    return base64_bytes

def cli_json_obj():
    ###json_str = json.dumps(json_data, indent=2)  # Nice print to verify
    ##base64_request = encode64(json_str)
    headers = Headers({'Content-Type': 'application/base64', 'media_type': 'text/plain'})
    client = httpx.Client(headers=headers)
    return client
