import requests
from PIL import Image
from io import BytesIO
from PIL import ImageFile

def Load_image():	
#	ImageFile.LOAD_TRUNCATED_IMAGES = True #下载损坏图片
	for No in range(1,356):
		img_src = 'http://www.ruanyifeng.com/images_pub/pub_'+str(No)+'.jpg'
		response = requests.get(img_src)
		try:
			image = Image.open(BytesIO(response.content))
			image.save('G:\Project\A\pub_'+str(No)+'.jpg')
		except OSError as e:
			print (e)
			print ('Download error: pub_'+str(No)+'.jpg')

if __name__ == '__main__':
	Load_image()
