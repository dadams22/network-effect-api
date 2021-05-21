from flask import Flask, request
from linkedin_api import Linkedin


app = Flask(__name__)


def create_linkedin_instance():
    username = request.form['username']
    password = request.form['password']
    return Linkedin(username, password)


@app.route('/profile', methods=['POST'])
def get_profile():
    linkedin = create_linkedin_instance()
    return linkedin.get_user_profile()


if __name__ == '__main__':
    app.run()
