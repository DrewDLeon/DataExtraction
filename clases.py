from dotenv import load_dotenv
import os
load_dotenv()

class params:
    def __init__(self):
        self.user = os.environ.get('DB_USER')
        self.password = os.environ.get('DB_PASSWORD')
        self.database = os.environ.get('DB_DATABASE')
        self.port = os.environ.get('DB_PORT')
        self.host = os.environ.get('DB_HOST')


class api_url:
    def __init__(self):
        self.customers = os.environ.get('URL_CUSTOMERS')
        self.panels = os.environ.get('CUSTOMER_PANELS')
        self.data = os.environ.get('PANELS_DATA')

class api_credentials:
    def __init__(self):
        self.customer_id = os.environ.get('CUSTOMER_ID')
        self.customer_hash = os.environ.get('CUSTOMER_HASH')
        self.token = os.environ.get('ACCESS_TOKEN')
