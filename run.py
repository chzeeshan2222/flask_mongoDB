from pytz import utc
from apscheduler.schedulers.background import BackgroundScheduler
from auth_app import app
#from auth_app.controllers.controller import allControllers

#contr = allControllers()

scheduler = BackgroundScheduler()
scheduler.start()

# def test_schedule_signup():
#     print("Schedule time is running")

# def schedule_signup_job():
#     with app.app_context():
#       scheduler.add_job(test_schedule_signup, 'cron', second='*/600')  # Every 5 seconds

# schedule_signup_job()

if __name__ == '__main__':
    app.run(debug=True)
