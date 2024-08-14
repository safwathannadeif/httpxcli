from cli.base.code.tree.extract_tree2 import extract
from cli.base.code.tree.supply_clz import Supply
import json

supply = Supply()
def make_one_sub_branch_Leaf():
   inx_il = supply.incr_inx_sub_branch_leaf()
   sub_branch_leaf_dict = {}
   sub_branch_leaf_dict["sbl_name_inx"]="sbl_name_inx" + str(inx_il)
   sub_branch_leaf_dict["color"] = "color"+str(inx_il)
   sub_branch_leaf_dict["density"] = "density" + str(inx_il)
   sub_branch_leaf_dict["no_of_paper"] =  supply.int_num()
   sub_branch_leaf_dict["smooth_level"] = "smooth_level" + str(inx_il)
   return sub_branch_leaf_dict

def make_one_branch(single=False):
    inx_ib =supply.incr_inx_branche()
    branch_dict = dict()
    branch_dict["b_name_inx"]= "b_name_inx"+str(inx_ib)
    branch_dict["strength"]= "strength"+str(inx_ib)
    branch_dict["length"] =  supply.int_num()
    branch_dict["woody"] = "woody" + str(inx_ib)
    lis_of_leafs=[]
    bl=supply.incr_no_of_leaf_per_branch()
    if not single:
        one_or_many = "__Many"
    if single:
        bl=1
        one_or_many = "__One"
    inx_4_sub_b_l_grp="sbl_name_inx" + inx_ib
    for k in range(0,bl):
        s_b_l_dict=make_one_sub_branch_Leaf()
        ##s_b_l_dict["sbl_name_inx"] = inx_4_sub_b_l_grp+ one_or_many
        lis_of_leafs.append(s_b_l_dict)
    branch_dict["sub_branch_leaf"] = lis_of_leafs
    return branch_dict

def make_one_tree(single=False):
    inx_it = supply.incr_inx_tree()
    if not single :
        tl=supply.incr_no_branch_per_tree()
        one_or_many="__Many"
    if single :
        tl=1
        one_or_many = "__One"
    tree_dict = dict()
    tree_dict["t_name_inx"] = "t_name_inx" + inx_it+one_or_many
    tree_dict["origination"]= "origination"+str(inx_it)
    tree_dict["dob"] =  "dob"+str(inx_it)
    lis_of_branch = []

    inx_4_branch_grp = "b_name_inx" + inx_it
    for j in range(0,tl):
        b_dict=make_one_branch(single)
        inx_4_branch_grp = "b_name_inx" + inx_it
        #b_dict["b_name_inx"]=inx_4_branch_grp+one_or_many
        lis_of_branch.append(b_dict)
    tree_dict["tree_branch"] = lis_of_branch
    return tree_dict


#test
def get_create_json_obj():
    all_tree_dict={}
    all_tree_list=[]
    one_tree= make_one_tree(True)                   #singelton true
    one_tree_dict_with_name={"tree":one_tree}
    all_tree_list.append(one_tree_dict_with_name)

    one_tree= make_one_tree(False)
    one_tree_dict_with_name={"tree":one_tree}
    all_tree_list.append(one_tree_dict_with_name)

    all_tree_dict["trees"]=all_tree_list
    #######
    #### it has to be a string through dumpsjson_obj2=json.loads(all_tree_dict)
    ######      print(json_obj2)
    #####
    json_obj_str=json.dumps(all_tree_dict,indent=2)
    json_obj=json.loads(json_obj_str)
    print(json_obj_str)
    return json_obj


