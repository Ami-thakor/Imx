from realesrgan_ncnn_py import Realesrgan
from PIL import Image

realesrgan = Realesrgan(gpuid=-1, model=0)


def enhance_image(img_path, outpath):
    with Image.open(img_path) as image:
        image = realesrgan.process_pil(image)
        image.save(f"{outpath}", quality=100)

    return outpath
