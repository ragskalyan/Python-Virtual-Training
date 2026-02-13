from assessment_13_02_2026.notification import Notification


class SMS(Notification):

    @staticmethod
    def send(message):
        return f"Sending SMS: {message}"