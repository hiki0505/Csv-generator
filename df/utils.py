from faker import Faker

__fake = Faker()

__DATA_GENERATORS = {
    'fullname': __fake.name,
    'job': __fake.name,
    'email': __fake.email,
    'domain': __fake.domain_name,
    'phone': __fake.phone_number,
    'company': __fake.company,
    'text': __fake.text,
    'number': __fake.random_number,
    'address': __fake.address,
    'date': __fake.date,
}

def generate_records(column_types, total_records=100):
    return [
        [__DATA_GENERATORS.get(type_)() for type_ in column_types]
        for _ in range(total_records)
    ]
