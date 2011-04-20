
from bx3d_fix import fix_tree, is_broken_tree

from xml.etree.ElementTree import Element, SubElement

def make_broken_tree():
    app = Element('Appearance')
    mat = SubElement(app, 'Material')
    tex = SubElement(app, 'ImageTexture', {'idx':0})
    tex = SubElement(app, 'ImageTexture', {'idx':1})
    return app



def test_fix_tree():
    tree = make_broken_tree()
    assert is_broken_tree(tree)
    fix_tree(tree)
    for idx, item in enumerate(tree.findall('ImageTexture')):
        assert item.attrib['idx'] == idx
    assert not is_broken_tree(tree)


