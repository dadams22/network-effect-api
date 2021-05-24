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
    user_profile = linkedin.get_user_profile()
    public_id = user_profile['miniProfile']['publicIdentifier']
    profile = linkedin.get_profile(public_id)
    return profile


@app.route('/connections', methods=['POST'])
def get_connections():
    linkedin = create_linkedin_instance()
    user_profile = linkedin.get_user_profile()
    public_id = user_profile['plainId']
    connections = linkedin.get_profile_connections(public_id, detailed_profile=True)
    return {'connections': connections}


if __name__ == '__main__':
    app.run()
