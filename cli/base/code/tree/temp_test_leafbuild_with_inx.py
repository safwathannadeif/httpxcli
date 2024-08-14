import random

noOf_leaf_per_branch=10

start_inx_o_leaf=0

leafs = [{"name": f"leaf{k}", "noOfpaper": random.randint(80, 400), "leafgroupfrk": -1} for k in range(100, 220)]

leafg_lis=[]
leafg_lis =[ leafs[kk] for kk in range(start_inx_o_leaf,noOf_leaf_per_branch+start_inx_o_leaf)]
print(leafg_lis)
start_inx_o_leaf= start_inx_o_leaf+ noOf_leaf_per_branch
leafg_lis=[]
leafg_lis =[ leafs[kk] for kk in range(start_inx_o_leaf,noOf_leaf_per_branch+start_inx_o_leaf)]
print(leafg_lis)


