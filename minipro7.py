from plyer import notification
from time import sleep


def notifyme(title, message, appicon):
    notification.notify(
        title=title,
        message=message,
        app_name = "Health Management",
        app_icon=appicon,
        timeout=3
    )


if __name__ == '__main__':
    i = 0
    for i in range(0, 24):
        notifyme("Sanitization time",
                "Its been 30 minuts you haver sanitized, so its time to do so", "mini pro\sani.ico")
        sleep(5*60)
        notifyme("Drink Water", "Its been an hour, Its time to Drink Water",
                "mini pro\water.ico")
        sleep(60*60)
        i += 1
