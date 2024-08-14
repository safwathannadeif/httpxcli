import base64
import httpx
import json

from httpx import Headers
from cli.base.code.tree.create_tree_b64_cli2 import make_tree

def encode64(in_str):

    in_str_bytes = in_str.encode("ascii")
    base64_bytes = base64.b64encode(in_str_bytes)
    #print("Encoded string:" ,base64_bytes)
    return base64_bytes

def post_create_whole_tree():
    data=make_tree()
    #print(data)
    json_str = json.dumps(data, indent=2)  # Nice print to verify
    base64_request=encode64(json_str)
    #print(base64_request)
    headers = Headers({'Content-Type': 'application/base64'})
    client = httpx.Client(headers=headers)
    request = client.build_request("post", 'http://127.0.0.1:8000/tree_api/create_tree/',  data=base64_request) # OK
    response = client.send(request)
    return response


resp=post_create_whole_tree()
print("Resp:",resp)
#print("Resp.content:",resp.content)
json_obj = json.loads(resp.content)  # Nice print to verify
print(json.dumps(json_obj, indent=2) )

