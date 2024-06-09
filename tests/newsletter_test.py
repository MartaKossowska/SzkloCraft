from tests.base_test import BaseTest
from test_data.newsletter_test_data import EmailData


class NewsletterTest(BaseTest):
    """
    Entering incorrect email in newsletter box TEST
    """
    def setUp(self):
        super().setUp()
        # STEPS OF THE SETUP:
        # 1. Get faked email data
        self.test_data = EmailData()
        # 2. Disable cookies
        self.home_page.cookie_button_click()

    def test_wrong_email_entered(self):
        # STEPS OF THE TEST:
        # 1. Information about commencing the test
        print("Start of the newsletter test: test_wrong_email_entered")
        # 2. Find newsletter box and enter incorrect email
        self.email_field = self.home_page.enter_email(self.test_data.bad_email)
        # 3. Click on submit button
        self.home_page.click_submit_email_btn()
        # 4. Check if correct message is displayed
        self.assertEqual('Newsletter : Nieprawidłowy adres e-mail', self.home_page.get_user_error_message())
        # 5. Information about the end of the test
        print("End of the newsletter test: test_wrong_email_entered")
