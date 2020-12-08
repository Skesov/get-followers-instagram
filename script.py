from dotenv import load_dotenv
import instaloader
import os


load_dotenv()


# Get instance

user = os.getenv('LOGIN')
password =


L = instaloader.Instaloader()

# Login or load session
L.login(user)        # (login)
L.interactive_login(user)      # (ask password on terminal)
L.load_session_from_file(user)  # (load session created w/
#  `instaloader -l USERNAME`)

# Obtain profile metadata
profile = instaloader.Profile.from_username(L.context, 'Skesov')

# Print list of followees
for followee in profile.get_followees():
    print(followee.username)

# (likewise with profile.get_followers())
