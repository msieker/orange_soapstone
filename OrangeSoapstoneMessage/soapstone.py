#!/usr/bin/env python3

from os import path
import json
import random
from typing import Dict

MESSAGE_FILENAME=path.join(path.dirname(__file__), "messages.json")
CONJUNCTION_PERCENT=0.25

with open(MESSAGE_FILENAME, "r") as in_file:
    MESSAGES = json.load(in_file)    

def get_filled_message() -> str:
    template = random.choice(MESSAGES["templates"])
    category = random.choice(list(MESSAGES["categories"].keys()))
    item = random.choice(MESSAGES["categories"][category])
    return template.format(item)

def generate_message() -> str:
    message_parts = []
    if (1 - random.random()) > CONJUNCTION_PERCENT:
        message_parts.append(get_filled_message())
        message_parts.append(random.choice(MESSAGES["conjunctions"]))
        
    message_parts.append(get_filled_message())
    message_parts.reverse()
    return "".join(message_parts).strip().capitalize()

def main():
    message = generate_message()
    print(message)

if __name__ == "__main__":
    main()