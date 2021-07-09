import logging

import azure.functions as func
from utils.common_utils import hello_world

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    return func.HttpResponse(f"{hello_world()}")
