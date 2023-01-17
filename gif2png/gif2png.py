import os
from PIL import Image,ImageSequence

def gif2pngs(gif_name,png_folder):
    # 读取GIF
    im = Image.open(gif_name)
    # GIF图片流的迭代器
    iter = ImageSequence.Iterator(im)
    index = 0
    # 遍历图片流的每一帧
    if not os.path.exists(png_folder):
        os.makedirs(png_folder)
    for frame in iter:
        
        frame.save(os.path.join(png_folder,str(index)+'.png'))
        index += 1
    print(f"converted {gif_name}")

def concatenate_pngs(png_folder,out_folder,width):
    n = len(os.listdir(png_folder))
    png_list = [Image.open(os.path.join(png_folder,str(i)+'.png')) for i in range(1,n)]
    height = width*(n-1)
    bg = Image.new(mode='RGBA',size=(width,height))
    i = 0
    if not os.path.exists(out_folder):
        os.mkdir(out_folder)
    for png in png_list:
        png = png.resize((width,width))
        bg.paste(png,(0,i*width))
        i += 1
    out_path = os.path.join(out_folder,png_folder[5:]+'.png')
    bg.save(out_path)
    print(f"concatenate {out_path}")
    
if __name__ == '__main__':
    gif_folder = 'gifs'
    png_dir = 'pngs'
    out_folder = 'out'
    width = 48
    for g in os.listdir(gif_folder):
        gif_name = os.path.join(gif_folder,g)
        png_folder = os.path.join(png_dir,g[:-4])
        gif2pngs(gif_name,png_folder)
        concatenate_pngs(png_folder,out_folder,width)
    print("FINISH")
    