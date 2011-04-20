#!/bin/python
from xml.etree.ElementTree import parse, tostring

def fix_tree(app):
    assert app.tag == 'Appearance'
    mat = app.find('Material')
    texts = app.findall('ImageTexture')
    if mat is None:
        return
    for tex in texts:
        app.remove(tex)
        app.insert(0, tex)


def is_broken_tree(app):
    assert app.tag == 'Appearance'
    mat = app.find('Material')
    texts = app.findall('ImageTexture')
    if not (mat is not None and texts):
        return
    elems = list(app)
    mat_idx = elems.index(mat)
    for tex in texts:
        print mat_idx, elems.index(tex)
        if mat_idx<elems.index(tex):
            return True
    return False


def fix_document(tree):
    for app in tree.findall('.//Appearance'):
        if is_broken_tree(app):
            fix_tree(app)

if __name__ == '__main__':

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('source')
    parser.add_argument('target', default=None, nargs='?')
    opts = parser.parse_args()
    doc = parse(opts.source)
    fix_document(doc)

    if opts.target is None:
        print tostring(doc.getroot())
    else:
        doc.write(opts.target)

