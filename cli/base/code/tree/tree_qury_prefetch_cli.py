import json

import httpx

def extract_json_out(json_out1):
    grp_no = 1
    for xlis in json_out1:
        print(xlis)
        print(xlis["Group_name"])
        print(xlis["Leafs_with_group" + str(grp_no)])
        grp_no += 1
'''
 httpx.get("http://127.0.0.1:8000/tree_api/all_tree/")
 httpx.get("http://127.0.0.1:8000/tree_api/filter_tree/?treename=tree1&no_of_Leaf_gt= 120")
 httpx.post("http://127.0.0.1:8000/tree_api/del_leafs/",data={"treename" : "tree1","leaf_name":"leaf25"})
 httpx.post("http://127.0.0.1:8000/tree_api/upd_branch/",data={"treename" : "tree2","branch_name":"branch3","upd_length":50,
                                                                     "upd_name":"branch33"})                             
 '''

def get_query_prefetch():
    r= httpx.post("http://127.0.0.1:8000/tree_api/upd_branch/",data={"treename" : "tree21","branch_name":"branch224","upd_length":50,
                                                                     "upd_name":"branch33"})

    sts= r.status_code
    #h=r.headers
    #tx=r.read()
    json_out=r.json()
    print( sts)
    print(json.dumps(json_out,indent=2))
    #extract_json_out(json_out)

r=get_query_prefetch()
