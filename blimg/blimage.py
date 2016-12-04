import imgbase

bdef = imgbase.layout.BlockDef(36,38,20,20,7)
adef = imgbase.layout.ArrayDef(7,2,900,900,(50,50),bdef)


def find_blocks(image, adef=adef):
    return {'A1': (50,50), 'A2': (100, 50)}
