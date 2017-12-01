from flask import Flask
from notificationcontroller import NotificationController

app = Flask(__name__)

controller = NotificationController


@app.route("/users/<user_id>/notifications", methods=['GET'])
def get_all_notifications(user_id):
    return "hello world"
    #return controller.retrieve_notifications(user_id=user_id)


if __name__ == '__main__':
    app.run(debug=False)
