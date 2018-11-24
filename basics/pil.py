from PIL import Image, ImageFilter

# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('testPillow.jpg')
w, h = im.size
# 将原图片缩放50%
im.thumbnail((w//2, h//2))
# 应用模糊滤镜:
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'jpeg')
