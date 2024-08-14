import json
import random

from cli.base.code.tree.extract_tree2 import extract_cli2

tot_no_of_grp = 8
tot_no_of_br=136
start_inx = 15
json_all = None
def make_tree():
    grp = [{"groupLeafsName": f"groupLeaf{index}", "Description": f"Leaf Group no.{index}"} for index in
           range(start_inx, tot_no_of_grp + start_inx)]
    leafs = [{"name": f"leaf{k}", "noOfpaper": random.randint(80, 400)} for k in range(100, 220)]
    branches = [{"name": f"branch{b}", "length": random.randint(27, 62)} for b in
                range(100,tot_no_of_br+100)]
    trees = [{"name": f"tree{tr}", "orgination": f"orgination{tr}"} for tr in range(20, 22)]
    all_trees=[]
    # grp
    grp={"grp": grp}
    all_trees.append(grp)
    noOf_leaf_per_branch=3
    noOf_br_per_tree = 11
    start_inx_o_leaf=0
    st_br=100
    end_br=noOf_br_per_tree+1
    for tr in trees:
        lis_of_branches_4_tree=[]
        for br_inx in range(st_br,end_br) :
            br=branches[br_inx]
            leafg_lis =[ leafs[kk] for kk in range(start_inx_o_leaf,noOf_leaf_per_branch+start_inx_o_leaf)]
            br["leafg"] = leafg_lis
            lis_of_branches_4_tree.append(br)
            start_inx_o_leaf = start_inx_o_leaf + noOf_leaf_per_branch

        tr["branchs"] = lis_of_branches_4_tree
        tree = {"tree": tr}
        all_trees.append(tree)
        st_br=st_br+end_br + noOf_br_per_tree
        end_br= st_br+noOf_br_per_tree

    json_all = json.dumps(all_trees, indent=2)
    return json_all

out_json= make_tree()
f_l= extract_cli2(out_json)

print("final tree_lis:", f_l.tree_lis)
print("final grp_lis:", f_l.grp_lis)
print("final branch_lis:", f_l.branch_lis)
print("final leaf_lis:", f_l.leaf_lis)


