from celery import shared_task

@shared_task(bind=True)
def test_func(self):
    for i in range(10):
        print('This is a test app',i)
    return 'Done'