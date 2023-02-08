from parser import GetFindDisk, GetFindTyre

from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()


def start_work(minutes: int) -> None:
    """Entrypoint"""

    scheduler.add_job(GetFindDisk.main, 'interval', minutes=minutes)
    scheduler.add_job(GetFindTyre.main, 'interval', minutes=minutes)

    scheduler.start()
