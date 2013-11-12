from PIL import Image

"""
instructions:
convert image.png -transparent white imageResult.png

tasks to implement:
1) loop through images and apply funcOne & funcTwo
"""
def funcHead():
	image = 'test_face.png'
	alpha_mask = 'test_mask.png'
	msk = Image.open(alpha_mask)
	img = Image.open(image)
	img.paste(msk, (0,0), msk)
	img.save('test_result_head.png', 'PNG')

def funcEyes():
	image = 'test_face.png'
	alpha_mask = 'test_eyes.png'
	msk = Image.open(alpha_mask)
	img = Image.open(image)
	img.paste(msk, (0,0), msk)
	img.save('test_result_eyes.png', 'PNG')



		