
class B_Params:
    no_of_sub_product=3
    no_of_item=4
    start_s_product=0
    start_item=0
def test():

        for i in range(B_Params.start_s_product,B_Params.no_of_sub_product+B_Params.start_s_product):
            print("sub:",i)
            for j in range(B_Params.start_item, B_Params.no_of_item + B_Params.start_item):
                print("item",j)
            B_Params.start_item = B_Params.start_item + B_Params.no_of_item
        B_Params.start_s_product = B_Params.start_s_product + B_Params.no_of_sub_product
test()