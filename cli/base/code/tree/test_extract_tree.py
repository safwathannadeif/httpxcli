from build_tree import get_create_json_obj
from extract_tree2 import extract
def test_extract_tree():
    tree_json_obj= get_create_json_obj()
    extract(tree_json_obj)

test_extract_tree()
