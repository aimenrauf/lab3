class Notifications:
    def __init__(self, size=10):
        self.notifications = [] 
        self.size = size 
    def add_notification(self, notification):
        if len(self.notifications) >= self.size:
            self.notifications.pop(0) 
        self.notifications.append(notification) 
    def view_latest_notifications(self):
        print("Latest Notifications:")
        for notification in self.notifications[-5:]: 
            print(notification)
    def clear_all_notifications(self):
        self.notifications.clear() 
        print("All notifications cleared.")
        
notifications_queue = Notifications(size=10)
notifications_queue.add_notification("Notification 1: Welcome to the app!")
notifications_queue.add_notification("Notification 2: You have a new message.")
notifications_queue.add_notification("Notification 3: Your profile has been updated.")
notifications_queue.add_notification("Notification 4: System maintenance scheduled.")
notifications_queue.add_notification("Notification 5: New features available.")
notifications_queue.add_notification("Notification 6: Don't miss our upcoming event!")
notifications_queue.add_notification("Notification 7: Your password has been changed.")
notifications_queue.add_notification("Notification 8: Update available for download.")
notifications_queue.add_notification("Notification 9: Feedback received.")
notifications_queue.add_notification("Notification 10: Thank you for your feedback.")
notifications_queue.view_latest_notifications()
notifications_queue.clear_all_notifications()
notifications_queue.view_latest_notifications()
