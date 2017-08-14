#! python3
# phone_and_email.py - Finds phone numbers & email addresses on the clipboard.
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 23:23:25 2017
Project: Phone Number and Email Address Extractor

Say you have the boring task of finding every phone number and email address in
a long web page or document. If you manually scroll through the page, you might
end up searching for a long time. But if you had a program that could search
the text in your clipboard for phone numbers and email addresses, you could
simply press CTRL-A to select all the text, press CTRL-C to copy it to the
clipboard, and then run your program. It could replace the text on the
clipboard with just the phone numbers and email addresses it finds.

Whenever you’re tackling a new project, it can be tempting to dive right into
writing code. But more often than not, it’s best to take a step back and
consider the bigger picture. I recommend first drawing up a high-level plan for
what your program needs to do. Don’t think about the actual code yet—you can
worry about that later. Right now, stick to broad strokes.

For example, your phone and email address extractor will need to do the
following:

    Get the text off the clipboard.
    Find all phone numbers and email addresses in the text.
    Paste them onto the clipboard.

from Automate:
    https://automatetheboringstuff.com/chapter7/


@author: david.antonini
"""

import re

import pyperclip

# Phone number regex:
phone_number_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)


# Email regex:
email_address_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # username
    @                      # @ symbol
    [a-zA-Z0-9.-]+         # domain name
    (\.[a-zA-Z]{2,4})      # dot-something
    )''', re.VERBOSE)


# Find matches in clipboard text:
text = str(pyperclip.paste())
phone_numbers = []
email_addresses = []

for groups in phone_number_regex.findall(text):
    found_phone_number = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        found_phone_number += ' x' + groups[8]
    if found_phone_number not in phone_numbers:
        phone_numbers.append(found_phone_number)

for groups in email_address_regex.findall(text):
    if groups[0] not in email_addresses:
        email_addresses.append(groups[0])

numbers_and_emails = phone_numbers + email_addresses

# Copy results to the clipboard:
if len(numbers_and_emails) > 0:
    pyperclip.copy('\n'.join(numbers_and_emails))
    print('Copied to clipboard:')
    print('\n'.join(numbers_and_emails))
else:
    print('No phone numbers or email addreses found.')
