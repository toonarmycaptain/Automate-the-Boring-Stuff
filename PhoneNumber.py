
# PhoneNumber.py:
import re


def findPhoneNumber(text):
    phoneNumRegex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?                # area code
        (\s|-|\.)?                        # separator
        (\d{3})                           # first 3 digits
        (\s|-|\.)                         # separator
        (\d{4})                           # last 4 digits
        (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
        )''', re.VERBOSE)
    found = phoneNumRegex.findall(text)
    if found is None or found == []:
        print("Phone number not found")
    else:
        print(found)
        print('Phone number found: '+'\n'.join(found))
#        print('Phone number found: ', end=''), print(*found, sep='\n')


message = 'Call me at (415)-555-1011 or 555-1012 tomorrow. 415-555-9999 is my office.'
findPhoneNumber(message)
