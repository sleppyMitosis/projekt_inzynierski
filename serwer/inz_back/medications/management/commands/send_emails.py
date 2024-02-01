from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.template.loader import render_to_string
from django.utils.html import strip_tags


class Command(BaseCommand):
    help = 'Sends a generic medication reminder to all users'

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        for user in users:
            try:
                validate_email(user.email)

                html_content = render_to_string('med_reminder.html',
                                                {'user_name': user.username})
                text_content = strip_tags(html_content)

                send_mail(
                    'Przypomnienie o Lekach dla Zwierzaka',
                    text_content,
                    'm72217707@gmail.com',
                    [user.email],
                    html_message=html_content,
                    fail_silently=False,
                )
                self.stdout.write(self.style.SUCCESS(f'Successfully sent email to {user.email}'))
            except ValidationError:
                self.stdout.write(self.style.WARNING(f'Invalid email address for user: {user.username}'))
