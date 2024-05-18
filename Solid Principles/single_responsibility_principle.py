# Before SRP
class UserManager:
    def create_user(self):
        # logic to create user
        pass

    def update_user(self):
        # logic to update user
        pass

    def delete_user(self):
        # logic to delete user
        pass

    def send_email(self):
        # logic to send email
        pass

    def generate_report(self):
        # logic to generate report
        pass


# After SRP
class UserService:
    def create_user(self):
        # logic to create user
        pass

    def update_user(self):
        # logic to update user
        pass

    def delete_user(self):
        # logic to delete user
        pass


class EmailService:
    def send_email(self):
        # logic to send email
        pass


class ReportService:
    def generate_report(self):
        # logic to generate report
        pass
