from notification import Notification


class PUSH(Notification):
    @staticmethod
    def send(message):
        return f"Sending Push Message: {message}"