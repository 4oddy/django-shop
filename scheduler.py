import os

from apscheduler.schedulers.background import BlockingScheduler

from parser import GetFindDisk, GetFindTyre

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store.settings')

scheduler = BlockingScheduler()


def start_work(minutes: int | float) -> None:
    """Entrypoint"""

    scheduler.add_job(GetFindDisk.main, 'interval', minutes=minutes)
    scheduler.add_job(GetFindTyre.main, 'interval', minutes=minutes)

    scheduler.start()


if __name__ == '__main__':
    start_work(minutes=1)
