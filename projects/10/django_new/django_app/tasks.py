import random
import time
from celery import shared_task


@shared_task
def add(x, y):
    time.sleep(5.0)  # processing
    return x + y


@shared_task
def scale_image(path):
    time.sleep(12.0)  # processing
    return path


@shared_task
def send_mass_mail(recipients=None):
    if recipients is None:
        recipients = [f"admin{x}@mail.ru" for x in range(1, 1000)]
    res = []
    for i in recipients:
        # send
        time.sleep(0.01)  # processing
        res.append("success" if random.randint(0, 1) > 0 else "error")
    return res
