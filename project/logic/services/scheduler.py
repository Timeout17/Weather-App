from apscheduler.schedulers.blocking import BlockingScheduler
from project.logic.orchestrator.make_answer import MakeAnswer


scheduler = BlockingScheduler()

daily_weather = MakeAnswer()

scheduler.add_job(
    daily_weather.make_answers(),
    trigger="cron",
    hour=6,
    minute=0
)

scheduler.start()