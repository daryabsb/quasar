import random
from django.db import transaction
from django.core.management.base import BaseCommand
from datetime import timedelta, date
from core.models import User, Client, Appointment, Attachment, Prescription
from core.factories import ClientFactory, AppointmentFactory, AttachmentFactory, PrescriptionFactory


class Command(BaseCommand):
    help = 'Create Clients, Appointments, Attachments and Prescriptions'

    @transaction.atomic
    def handle(self, *args, **options):
        default_user = User.objects.first()
        self.stdout.write(self.style.SUCCESS('Creating Clients...'))

        # Create 70 clients

        for i in range(70):
            client = ClientFactory()
            self.stdout.write(self.style.SUCCESS(
                f'Client {client.name} created'))

            # Create 20 appointments for each client

            while client:  # While there are still clients left to create appointments for...

                start_date = date(2018, 1, 1)
                end_date = date(2023, 3, 30)
                time_between_dates = end_date - start_date
                days_between_dates = time_between_dates.days
                random_number_of_days = random.randrange(days_between_dates)
                appointment_date = start_date + \
                    timedelta(days=random_number_of_days)

                appointment = AppointmentFactory(
                    client=client, user=default_user, date=appointment_date)

                self.stdout.write(self.style.SUCCESS(
                    f'Appointment {appointment.date} created for client {client.name}'))

                # Create 2 attachments for each appointment

                while appointment:  # While there are still appointments left to create attachments for...

                    attachment = AttachmentFactory(
                        client=client, user=default_user)

                    self.stdout.write(self.style.SUCCESS(
                        f'Attachment {attachment.filename} created for client {client.name}'))

                    # Break out of the while loop so that we can move on to the next appointment
                    # and create 2 attachments for it too (if there is another appointment left).
                    # If we don't break out of the while loop here then
                    break
