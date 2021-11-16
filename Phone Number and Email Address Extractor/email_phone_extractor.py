#! python3

import re, pyperclip

#Create a regex for phone numbers
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)


#Create a regex option for email addresses
emailRegex = re.compile(r'''
#some.+_thing@(\d{2,5}))?.com

[a-zA-Z0-9_.+]+    #name part
@                  #@ symbol
[a-zA-Z0-9_.+]+    # domain name part
''', re.VERBOSE)


#Get the text off the clipboard
text = pyperclip.paste()

#Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
	allPhoneNumbers.append(phoneNumber[0])