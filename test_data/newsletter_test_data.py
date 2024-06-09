

from faker import Faker
import random


class EmailData:
    """
    generating fake email for tests
    """

    def __init__(self):
        fake = Faker("pl_PL")

        def remove_random_character(email):
            # Randomly chooses to remove "@" or "." and removes it from generated email
            # returns incorrect email
            char_to_remove = random.choice(["@", "."])
            bad_email = email.replace(char_to_remove, "", 1)
            return bad_email

        # Generate a fake email address
        self.fake_email = fake.email()

        # Remove a random character from the fake email address
        self.bad_email = remove_random_character(self.fake_email)


email_data = EmailData()

# Access and print the original and modified emails
print("Generated test data:")
print("Original fake Email:", email_data.fake_email)
print("Modified fake Email:", email_data.bad_email)
