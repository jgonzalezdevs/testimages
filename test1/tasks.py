from images.utils.core import ImageConversion
from celery import shared_task

image_conversion = ImageConversion()

@shared_task
def task1(image_path: str):
    try:
        image_conversion.invert_color(image_path)
    except Exception as e:
        pass

@shared_task
def task2(image_path: str):
    try:
        image_conversion.get_black_and_white(image_path)
    except Exception as e:
        pass

@shared_task
def task3(image_path: str):
    try:
        image_conversion.rotate_90_degrees(image_path)
    except Exception as e:
        pass

@shared_task
def task4(image_path: str):
    try:
        image_conversion.flip_on_vertical_axis(image_path)
    except Exception as e:
        pass
