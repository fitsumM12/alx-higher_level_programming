#!/usr/bin/python3
<<<<<<< HEAD
"""
Fetches https://intranet.hbtn.io/status
use the package urllib
 body of the response must be displayed in tabulation before -
"""
import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()

=======
# Write the python script that   fetches https://a;x-intranet.hbtn.io/status
# use the packge urllib
# you are not allowed to impport any packages other than urllib
# the body of the response must be displayed
# use a with statement
import urllib.request
with urllib.request.urlopen('https://alx-internate.htbn.io/status') as response:
    html = response.read()
>>>>>>> 8b86f5c338494c6fb7e6e315294ce221e0f6ba4d
print('Body response:\n\t- type: {}'.format(type(html)))
print('\t- content: {}'.format(html))
print('\t- utf8 content: {}'.format(html.decode('utf-8')))
