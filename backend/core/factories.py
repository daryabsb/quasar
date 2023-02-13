# from django.contrib.auth.models import User
from factory import Faker, SubFactory
from factory.django import DjangoModelFactory

from core.models import User, Client, Address, Appointment, Prescription, Attachment


class UserFactory(DjangoModelFactory):
    class Meta:
        model = 'User'
    email = Faker('email')
    password = Faker('password')


# print(user.name)


class AddressFactory(DjangoModelFactory):
    class Meta:
        model = 'Address'
    address_line1 = Faker('street_address')
    # city = Faker('city')
    # state = Faker('state')
    # zip_code = Faker('zip_code')


class ClientFactory(DjangoModelFactory):
    class Meta:
        model = 'Client'

    user = SubFactory(UserFactory)
    name = Faker('name')
    dob = Faker('date_of_birth')
    date_bonding = Faker('date_this_decade')
    age = Faker('random_int', min=18, max=100)
    gender = Faker('random_element', elements=['male', 'female'])
    # address = SubFactory(AddressFactory)
    phone = Faker('phone_number')
    email = Faker('email')
    description = Faker('paragraph')
    status = True
    created = Faker('date_this_decade')
    updated = Faker('date_this_decade')
    image = Faker('image_url')


class AttachmentFactory(DjangoModelFactory):
    class Meta:
        model = 'Attachment'

    user = SubFactory(UserFactory, user=User.objects.first())
    client = SubFactory(ClientFactory)
    filename = Faker('file_name')
    file = Faker('file_path')
    page_count = Faker('random_int', min=1, max=100)
    file_type = Faker('random_element', elements=['pdf', 'image', 'document'])
    created = Faker('date_this_decade')
    updated = Faker('date_this_decade')


class AppointmentFactory(DjangoModelFactory):
    class Meta:
        model = 'Appointment'

    user = SubFactory(UserFactory, user=User.objects.first())
    client = SubFactory(ClientFactory)
    title = Faker('sentence')
    description = Faker('paragraph')
    date = Faker('date_time_this_decade')
    date_to = Faker('date_time_this_decade')
    created = Faker('date_this_decade')
    updated = Faker('date_this_decade')


class PrescriptionFactory(DjangoModelFactory):
    class Meta:
        model = 'Prescription'

    user = SubFactory(UserFactory, user=User.objects.first())
    client = SubFactory(ClientFactory)
    title = Faker('sentence')
    description = Faker('paragraph')
    files = SubFactory(AttachmentFactory)
    has_appointment = Faker('random_element', elements=[True, False])
    appointment = SubFactory(AppointmentFactory)
    created = Faker('date_this_decade')
    updated = Faker('date_this_decade')


# USE THE FACTORIES BELOW:
# client = ClientFactory()

# attachment = AttachmentFactory()
# appointment = AppointmentFactory()
# prescription = PrescriptionFactory()


# import factory
# from factory.django import DjangoModelFactory
# import factory.fuzzy as fz

# from .models import User, Client, Appointment, Address, Attachment, Prescription

# default_user = User.objects.first()

# # Defining a factory
# class ClientFactory(DjangoModelFactory):
#     class Meta:
#         model = Client

#     user = default_user
#     name = factory.Faker("full_name")
#     dob = factory.Faker("date")
#     name = factory.Faker("first_name")

# # Using a factory with auto-generated data
# c = ClientFactory()
# c.name # Kimberly
# u.id # 51

# # You can optionally pass in your own data
# u = UserFactory(name="Alice")
# u.name # Alice
# u.id # 52
