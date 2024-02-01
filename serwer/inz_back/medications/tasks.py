from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

@shared_task
def send_medication_reminders():
    users = User.objects.all()
    for user in users:
        try:
            validate_email(user.email)
            send_mail(
                'Przypomnienie o lekach dla zwierzaka',
                'Przypominamy o podaniu dawki leku dla zwierzaka.',
                'from_email@example.com',
                [user.email],
                fail_silently=False,
            )
        except ValidationError:
            pass
