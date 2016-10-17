# coding: utf8
import os
import datetime
import argparse
from PIL import Image, ImageDraw, ImageFont, ImageColor


def add_date(filepath, date=None, color='yellow', font_size=None, save_path=None, width=0.7, height=0.9, save_fmt='jpeg'):
    try:
        image = Image.open(filepath)
    except BaseException as e:
        print(e)
        print("文件打开失败，请检查文件路径是否正确...")
        return False
    dirname, filename = os.path.split(filepath)[:]
    image_width, image_height = image.size
    if not date:
        date = datetime.date.isoformat(datetime.date.today())
    
    if not font_size:
        font_size = int(image_width/20)
    draw_width = int(image_width*width)
    draw_height = int(image_height*height)
    draw = ImageDraw.Draw(image)
    here = os.path.abspath(os.path.dirname(__file__))
    ttf_file = os.path.join(here, "ttfs/song.ttf")
    draw_font = ImageFont.truetype(ttf_file, size=font_size)
    fillcolor = ImageColor.colormap.get(color)
    draw.text((draw_width, draw_height), date, font=draw_font, fill=fillcolor)
    if not save_path:
        save_path = ''.join(['change_', filename])
    
    result = os.path.join(dirname, save_path)
    image.save(result, save_fmt)
    print('修改后的图片保存为:{0}'.format(result))
    return True


def main():
    parser = argparse.ArgumentParser(
        description="给照片添加日期,修改后的文件名会保存在原路径.")
    parser.add_argument('-p', '--filepath', type=str, help='原图片路径')
    parser.add_argument('-d', '--date', type=str, help='日期:默认当天')
    parser.add_argument('-c', '--color', type=str,
                        help='日期字体颜色：默认黄色',
                        default='yellow')
    parser.add_argument('-f', '--font_size', help='日期字体大小:默认图片宽度/20 ')
    parser.add_argument('-s', '--save_path', type=str, help='修改后文件保存名:默认为 change+原文件名', default=None)
    args = parser.parse_args()
    filepath = args.filepath
    if filepath is None:
        while True:
            try:
                filepath = input(
                    '请输入图片路径(包括文件名):')
                break
            except ValueError:
                print('输入有误,请重新输入')
    add_date(filepath, date=args.date, color=args.color, font_size=args.font_size, save_path=args.save_path)


if __name__ == "__main__":
    main()