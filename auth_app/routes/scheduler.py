from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from ..controllers.controller import allControllers
control=allControllers()
scheduler = BackgroundScheduler()

def start_scheduler():
    scheduler.start()
    # scheduler.add_job(control.publishers, trigger=CronTrigger(minute='*/7'))
    scheduler.add_job(test_schedule_signup, trigger=CronTrigger(second='*/7'))
def test_schedule_signup():
    print("Schedule time is running")


# import ctypes

# def lock_screen_windows():
#     ctypes.windll.user32.LockWorkStation()
# import time
# import pyautogui
# def click_after_2_minutes():
#     time.sleep(10)  # Wait for 2 minutes (120 seconds)
#     # Perform a mouse click at the current mouse position
#     pyautogui.click()