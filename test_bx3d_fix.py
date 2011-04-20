
from bx3d_fix import fix_tree, is_broken_tree

from xml.etree.ElementTree import Element, SubElement

def make_broken_tree():
    app = Element('Appearance')
    mat = SubElement(app, 'Material')
    tex = SubElement(app, 'ImageTexture')
    return app



def test_fix_tree():
    tree = make_broken_tree()
    assert is_broken_tree(tree)
    fix_tree(tree)
    assert not is_broken_tree(tree)


