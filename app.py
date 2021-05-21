from flask import Flask, request
from linkedin_api import Linkedin


app = Flask(__name__)


if __name__ == '__main__':
    app.run()
