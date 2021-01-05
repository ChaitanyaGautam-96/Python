from win10toast import ToastNotifier
toaster = ToastNotifier()
toaster.show_toast("चाचा अब पानी पी लो!",duration=10)
#wait for threaded notification to finish
while toaster.notification_active():
    time.sleep(0.1)
