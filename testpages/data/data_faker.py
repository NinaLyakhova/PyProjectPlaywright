from faker import Faker
from faker.providers import BaseProvider
from mimesis import Person
from mimesis.locales import Locale
import factory
from hypothesis import strategies as st

fake = Faker("ru_RU")


def generate_test_data_faker():
    return {
        "name": fake.name(),
        "pass": fake.password(),
        "text": fake.passport_full(),
    }


def generate_test_data_mimesis():
    chel = Person(Locale.RU)
    return {
        "name": chel.full_name(),
        "pass": chel.password(),
        "text": chel.political_views(),
    }


class User:
    def __init__(self, name, email, address, password, phone_number):
        self.name = name
        self.email = email
        self.address = address
        self.phone_number = phone_number
        self.password = password


class UserFactory(factory.Factory):
    class Meta:
        model = User
    name = factory.LazyAttribute(lambda _: fake.name())
    email = factory.LazyAttribute(lambda _: fake.email())
    address = factory.LazyAttribute(lambda _: fake.address())
    phone_number = factory.LazyAttribute(lambda _: fake.phone_number())
    password = factory.LazyAttribute(lambda _: fake.password())

@st.composite
def generate_test_data_hypothesis(draw):
    name = draw(st.text())
    email = draw(st.emails())
    password = draw(st.text())
    text = draw(st.text())
    return {
        "name": name,
        "email": email,
        "password": password,
        "text": text
    }