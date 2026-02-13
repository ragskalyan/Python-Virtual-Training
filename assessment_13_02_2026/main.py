from emailer import EMAILER
from sms import SMS
from push import PUSH


if __name__ == '__main__':
    print(
        f"""{EMAILER().send("Hello World")}
{SMS().send("Hello World")}
{PUSH().send("Hello World")}"""
    )