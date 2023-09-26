# main.py
import json
import logging.config
import os
import sys
from collections import OrderedDict

import click
import requests

# Define the message to write to the file
message = 'Hello World'

# Specify the file path
file_path = './output.txt'

# Open the file in write mode and write the message
with open(file_path, 'w') as file:
    file.write(message)

print(f"'{message}' has been written to '{file_path}'")
