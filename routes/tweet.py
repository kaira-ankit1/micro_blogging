from flask import request,jsonify
from flask_login import login_required, current_user
from service.TweetService import TweetService
from . import routes

@routes.route("/create/tweet", methods=["POST"])
@login_required
def create():
    formData = request.json
    errors = []
    if ('message' not in formData) or (formData['message'] is None):
        errors.append("Please provide the message to be posted")
    else:
        return TweetService.createTweet(formData, current_user.id,)

