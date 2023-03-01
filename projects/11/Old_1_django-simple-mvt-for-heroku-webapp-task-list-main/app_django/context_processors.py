from . import models


def task_count(request):
    try:
        count = models.Task.objects.all().count()
    except Exception as error:
        count = 0
        print(f"context_processors.py task_count {error}")

    return dict(task_count=count)
