from dataclasses import dataclass


@dataclass
class Supply:
    counter:int=0
    no_of_branch_per_tree:int = 0
    no_of_leaf_per_branch:int = 0

    inx_tree=0
    inx_branch = 0
    inx_sub_branch_leaf = 0

    def incr_no_branch_per_tree(self):
        self.no_of_branch_per_tree +=2
        return(self.no_of_branch_per_tree)

    def incr_no_of_leaf_per_branch(self):
        self.no_of_leaf_per_branch += 2
        return(self.no_of_leaf_per_branch)
    #
    # def incr_counter(self):
    #     self.counter +=1
    #     return self.counter

    def int_num(self):
        return 100* self.counter+1

    def incr_inx_tree(self):
        self.inx_tree+=1
        return str(self.inx_tree)

    def incr_inx_branche(self):
        self.inx_branch += 1
        return str(self.inx_branch)

    def incr_inx_sub_branch_leaf(self):
        self.inx_sub_branch_leaf += 1
        return str(self.inx_sub_branch_leaf)
