from flask import jsonify
from model.tweet import Tweet
from db.Connection import db

class TweetService:
    def createTweet(formData,userId ):
        message = formData.get('message')
        new_tweet = Tweet(userId=userId, message=message)
        db.session.add(new_tweet)
        db.session.commit()
        response = {"status" : "success", "message":"tweet successfully posted"}
        return jsonify(response)
