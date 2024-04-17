from django.contrib.auth.tokens import PasswordResetTokenGenerator

class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        # No need for text_type, directly use user.pk and timestamp
        return str(user.pk) + str(timestamp)

        # If you need to include signup_confirmation (assuming it's a string):
        # return str(user.pk) + str(timestamp) + str(user.profile.signup_confirmation)

generate_token = TokenGenerator()
