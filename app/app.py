import blimg

WHERE = __file__ + ' in Blocks service'

image = 0

bls = blimg.find_blocks(image)

if __name__ == "__main__":
    print(WHERE)
    print('Block 1: ', bls['A1'])
