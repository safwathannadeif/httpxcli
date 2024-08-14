import json

from cli.base.code.tree.build_grp_w_leafs import  extract
from cli.base.code.tree.common_cli_base54 import encode64, cli_json_obj

json_str= extract()       # we need str
base64_request= encode64(json_str)

client_httpx= cli_json_obj()

request = client_httpx.build_request("post", 'http://127.0.0.1:8000/tree_api/Create_group_leaf/', data=base64_request)
response = client_httpx.send(request)

print("Response:::=======>\n",  json.dumps(response.json(),indent=1)  )
