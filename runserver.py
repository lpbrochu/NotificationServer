from flask import Flaskp

app = Flask(__name__)


@app.route("/users/<user_id>/notifications", methods=['GET'])
def get_all_notifications(user_id):
    return notification_controller.retrieve_notifications(user_id=user_id)

if __name__ == '__main__':
    app.run()
