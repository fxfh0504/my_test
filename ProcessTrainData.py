import os
from PIL import Image
from torchvision.datasets import ImageFolder
from torchvision import datasets


def main():
    process_raw_data()


def process_raw_data():
    # src_folder = 'datasets/autocheck/raw'
    # dest_folder = 'datasets/autocheck/images'
    src_folder = 'testimgs/raw'
    dest_folder = 'testimgs/images'
    for filename in os.listdir(src_folder):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            image_path = os.path.join(src_folder, filename)
            img = Image.open(image_path)

            # 转换成灰度图
            img = img.convert('L')

            # 转换成RGB模式
            img = img.convert('RGB')

            # 改变保存路径
            new_path = os.path.join(dest_folder, filename)

            # 保存图片
            img.save(new_path)
            print(img.info)


print('Done!')

if __name__ == "__main__":
    main()
