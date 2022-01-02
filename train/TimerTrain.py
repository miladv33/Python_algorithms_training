from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger

scheduler = BlockingScheduler()


@scheduler.scheduled_job(IntervalTrigger(seconds=3))
def train_model():
    print('dask train_model! The time is: %s' % datetime.now())


if __name__ == '__main__':
    scheduler.start()
