'''

class Grp_Sub_Branch_Leaf(models.Model):
    group_name_inx = models.CharField(max_length=27)
    Description  = models.CharField(max_length=37)
    class Meta:
        indexes = [
            models.Index(fields=["group_name_inx"])
        ]

    def __str__(self):
        return self.group_name_inx
class Sub_Branch_Leaf(models.Model):
    sbl_name_inx=models.CharField(max_length=27)
    color = models.CharField(max_length=15)
    density = models.CharField(max_length=17)
    no_of_paper = models.IntegerField()
    smooth_level = models.CharField(max_length=18)
    grp_sb_Leaf1_name=models.CharField(max_length=27,null=True,blank=True)
    grp_frk_link = models.ForeignKey(Grp_Sub_Branch_Leaf,
                                        null=True,blank=True,related_name="grp_1_2_Manyleafs", on_delete=models.CASCADE)  # group of S_B_L


'''
import json
from dataclasses import dataclass
from collections import namedtuple
#
# @dataclass
# class Sub_Branch_Leaf:
#     sbl_name_inx:str
#     color:str
#     density:str
#     no_of_paper:int
#     smooth_level:str
#     grp_sb_Leaf_name:str





@dataclass
class Supply_grp:
    gr_suffix=0
    sl_suffix=0
    #Sb_Lf = namedtuple('sbl_name_inx', 'color', 'density', 'no_of_paper', 'smooth_level', 'grp_sb_Leaf_name')

    nn=1
    max_nn=4
    no_grp = 3
    def inc_gr_suffix(self):
        self.gr_suffix +=1
        return str(self.gr_suffix)

    def inc_sl_suffix(self):
        self.sl_suffix += 1
        return str(self.sl_suffix)

    def create_s_br_leaf_instance(self,grp_inp) :
        #Person(name='John', age=30)
        sufx= self.inc_sl_suffix()
        sb_lf_dic={"sbl_name_inx" :"sbl_name_inx"+sufx,
                   "color" :"color"+sufx ,
                    "density" :"density"+sufx,
                    "no_of_paper" : 20*int(sufx) ,
                     "smooth_level" :"smooth_level"+sufx}
        return sb_lf_dic
    def next_nn(self):
        self.nn +=1
        if self.nn > self.max_nn: self.nn=1
        return self.nn

def generate_grps():
    all_gr_lis=[]
    suply_grp  =Supply_grp()
    for no in range(1,suply_grp.no_grp):
        gr_dict = {}
        grp="group" + suply_grp.inc_gr_suffix()
        gr_dict["group_name_inx"]=grp
        gr_dict["Description"]="Sub Branch Leafs Group No." + str(no)
        lis_of_s_br_leaf = []
        for x in range(1,suply_grp.next_nn()):
            lis_of_s_br_leaf.append(suply_grp.create_s_br_leaf_instance(grp))
        gr_dict["sub_Br_Leaf_lis"]=lis_of_s_br_leaf
        all_gr_lis.append(gr_dict)
    print (all_gr_lis)
    return all_gr_lis



def extract():
    out_lis = generate_grps()
    json_obj_str = json.dumps(out_lis, indent=2)        #we need str
    # print(json_obj)
    print(json_obj_str)
    return json_obj_str

### Test
def make_grp_w_leafs():
    json_obj_str = extract()
    obj_json = json.loads(json_obj_str)
    #obj_json=extract()
    lis_no=0
    for xlis in obj_json:
        lis_no +=1
        print("x-", lis_no,":::\n",xlis )

        print(xlis["group_name_inx"],xlis["Description"])
        for sbl in xlis["sub_Br_Leaf_lis"]:
             print("sbl:","sbl_name_inx=",sbl["sbl_name_inx"],"color=",sbl["color"],"density=",sbl["density"],"no_of_paper=",sbl["no_of_paper"],
                   "smooth_level=",sbl["smooth_level"]  )
    return obj_json

make_grp_w_leafs()
    #     sbl_name_inx = models.CharField(max_length=27)
    #     color = models.CharField(max_length=15)
    #     density = models.CharField(max_length=17)
    #     no_of_paper = models.IntegerField()
    #     smooth_level = models.CharField(max_length=18)
    #     grp_sb_Leaf_name = models.CharField(max_length=27, null=True, blank=True)









