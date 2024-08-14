import json


# Python may need  a class obj container let us make it as Final_lists
class Final_lists:
     tree_lis = []
     grp_lis = []
     leaf_lis = []
     branch_lis = []


     def __init__(self):
        pass
     def upd__lis(self, lis_2_ex_char, sub_lis_inp):
            match lis_2_ex_char:
                case "T":  # Tree is single dict
                    self.tree_lis.append(sub_lis_inp)
                case "G":           # List of grps
                    self.grp_lis.extend(sub_lis_inp)
                case "B":           # List of brs
                    self.branch_lis.extend(sub_lis_inp)
                case "L":                # List of leafs
                    self.leaf_lis.extend(sub_lis_inp)
f_l = Final_lists()
def collect_grp(lis_of_grp):
    f_l.grp_lis = lis_of_grp

def collect_tree(tree_dict):
    br_lis = tree_dict.pop("branchs")
    f_l.upd__lis("T", tree_dict)
    for br in br_lis:
        leaf_lis = br.pop("leafg")
        f_l.upd__lis("L", leaf_lis)

    f_l.upd__lis("B", br_lis)



def extract_cli2(json_inp_obj):
    r_josn = json.loads(json_inp_obj)
    for item in r_josn:
        # Discover the json
        if type(item) == dict and item.get("tree") != None: collect_tree(item.get("tree"))
        if type(item) == dict and item.get("grp") != None: collect_grp(item.get("grp"))
    return f_l


