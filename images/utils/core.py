from importlib.resources import path
from PIL import Image
import PIL.ImageOps


class ImageConversion():

    def invert_color(self, image_path: str):

        image = Image.open('{}'.format(image_path))

        inverted_image = PIL.ImageOps.invert(image)
        
        path = 'inverted_{}'.format(image_path)

        inverted_image.save(path)

        return path

    def get_black_and_white(self, image_path: str):
        
        image = Image.open(''.format(image_path))

        image = image.convert('1')
        
        path = 'black_and_white_{}'.format(image_path)

        image.save(path)

        return path

    def rotate_90_degrees(self, image_path: str, angle: int = 90):

        image = Image.open('{}'.format(image_path))

        out = image.rotate(angle)

        path = '90_degrees_{}'.format(image_path)

        out.save(path)

        return path

    def flip_on_vertical_axis(self, image_path: str, axis: any = PIL.Image.FLIP_LEFT_RIGHT):

        image = Image.open('{}'.format(image_path))

        out = image.transpose(axis)

        path = 'flip_on_vertical_axis_{}'.format(image_path)

        out.save(path)

        return path
    