import logging

import azure.functions as func

from .soapstone import generate_message

def main(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse(generate_message())