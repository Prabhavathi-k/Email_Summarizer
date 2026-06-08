from apscheduler.schedulers.blocking import BlockingScheduler

from main import run_email_pipeline


scheduler = BlockingScheduler()


scheduler.add_job(
    run_email_pipeline,
    trigger='cron',
    hour=15,
    minute=57,
    id='daily_email_digest'
)

print("Scheduler Started...")
print("Waiting for next scheduled run...")


scheduler.start()


#Testing scheduler code

# from apscheduler.schedulers.blocking import BlockingScheduler

# from main import run_email_pipeline


# scheduler = BlockingScheduler()

# scheduler.add_job(
#     run_email_pipeline,
#     trigger='interval',
#     minutes=1,
#     id='email_digest_test'
# )

# print("Scheduler Started...")
# print("Running every 1 minute for testing...")

# scheduler.start()