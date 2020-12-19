from dotenv import load_dotenv
import instaloader
import openpyxl
import os
import time
import random

load_dotenv()

# Files saving settings

path_to_save = 'Output'
followers_filename = 'Followers.xlsx'

# Get instance

user = os.getenv('LOGIN')
profile = os.getenv('PROFILE_FOR_PARSING')

L = instaloader.Instaloader()

# Load session

L.load_session_from_file(user)
# (load session created w/
#  `instaloader -l USERNAME`)

# Obtain profile metadata
profile = instaloader.Profile.from_username(L.context, profile)


# Checking folders existing

checkDirEx = os.path.isdir(path_to_save)
if not checkDirEx:
    os.mkdir(path_to_save)

# # Create excel sheet

book = openpyxl.Workbook()
sheet = book.active
sheet = book.create_sheet('Followers', 0)
sheet.column_dimensions['A'].width = 10
sheet.column_dimensions['B'].width = 40
sheet.column_dimensions['C'].width = 40
sheet.column_dimensions['D'].width = 30
sheet.column_dimensions['E'].width = 30
sheet.column_dimensions['F'].width = 10

# Creating a first row with titles
sheet.cell(1, 1).value = '№'
sheet.cell(1, 2).value = 'Username'
sheet.cell(1, 3).value = 'Followers'
sheet.cell(1, 4).value = 'Followees'
sheet.cell(1, 5).value = 'Followee/Folowers'
sheet.cell(1, 6).value = 'I follow'


# collecting folowees
# list_of_followees = []

# for followee in profile.get_followees():
#     list_of_followees.append(followee.username)

# collecting folowers and writing information to file
row = 2
for follower in profile.get_followers():
    username = follower.username
    # time.sleep(5)
    # followers = follower.followers
    # time.sleep(7)
    # followees = follower.followees
    # if followers != 0:
    #     ratio = followees / followers
    # else:
    #     ratio = 'bot'
    # ifollow = 'yes' if username in list_of_followees else 'no'

    sheet.cell(row, 1).value = row-1
    sheet.cell(row, 2).value = username
    # sheet.cell(row, 3).value = followers
    # sheet.cell(row, 4).value = followees
    # sheet.cell(row, 5).value = ratio
    # sheet.cell(row, 6).value = ifollow

    row += 1

    # time.sleep(30)

# saving book

book.save(path_to_save + "/" + followers_filename)

print("\n __________")
print("|          |")
print("|   DONE   |")
print("|__________|")
