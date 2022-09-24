#!/usr/bin/python3
# Write the python script that   fetches https://a;x-intranet.hbtn.io/status
# use the packge urllib
# you are not allowed to impport any packages other than urllib
# the body of the response must be displayed
# use a with statement
import urllib.request
with urllib.request.urlopen('https://alx-internate.htbn.io/status') as response:
    html = response.read()
print('Body response:\n\t- type: {}'.format(type(html)))
print('\t- content: {}'.format(html))
print('\t- utf8 content: {}'.format(html.decode('utf-8')))
