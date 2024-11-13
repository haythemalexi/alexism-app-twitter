import tweepy
from flask import Flask, redirect, request, session, url_for
import os

# Twitter API credentials (replace these with your own credentials)
api_key = 'AFQCy36DfgqFcTV6mmKGb1mk1'
api_secret_key = 'coOkfkLcocVccCYiUxGrLtG50Vd80kP3i2gEQjMbYqd6ci4w7Q'
access_token = '1694053108060397569-FgA5HaAcJkF7qn3deBOyyaoiRU1pZ8'
access_token_secret = 'O9efAlYZkeNuTrI8e5vkBj4H2tHscPwjUZIgvu6rhE5oF'

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.urandom(24)  # Use a random secret key for Flask sessions

# OAuth handler for user authentication
auth = tweepy.OAuth1UserHandler(api_key, api_secret_key)
auth_url=auth.get_authorization_url()
print(auth_url)

@app.route('/login')
def login():
    try:
        # Get request token and authorization URL
        auth_url = auth.get_authorization_url()
        session['request_token'] = auth.request_token  # Store request token in session
        return redirect(auth_url)
    except tweepy.TweepError:
        return 'Error! Failed to get request token.'

# Callback route to handle the redirect from Twitter after user authorization
@app.route('/callback')
def callback():
    try:
        request_token = session.get('request_token')
        auth.request_token = request_token  # Get request token from session

        # Get access token using the verifier provided by Twitter
        auth.get_access_token(request.args['oauth_verifier'])

        # Create Tweepy API object
        api = tweepy.API(auth)

        # Now authenticated, you can update the Twitter profile
        update_profile(api)

        return 'Successfully authenticated and profile updated!'
    except tweepy.TweepError:
        return 'Error! Failed to get access token.'

# Function to update profile picture
def update_pfp(api, image_path):
    try:
        api.update_profile_image(image_path)
        print("Profile picture updated successfully")
    except Exception as e:
        print(f"Error updating profile picture: {e}")

# Function to update profile banner
def update_banner(api, image_path):
    try:
        api.update_profile_banner(image_path)
        print("Banner updated successfully")
    except Exception as e:
        print(f"Error updating banner: {e}")

# Function to update Twitter profile name
def update_name(api, new_name):
    try:
        api.update_profile(name=new_name)
        print("Profile name updated successfully")
    except Exception as e:
        print(f"Error updating name: {e}")

# Function to update Twitter bio
def update_bio(api, new_bio):
    try:
        api.update_profile(description=new_bio)
        print("Bio updated successfully")
    except Exception as e:
        print(f"Error updating bio: {e}")

# Update profile with given data
def update_profile(api):
    # Here you can pass the profile data you want to update
    # For example, update profile picture, banner, name, and bio
    update_pfp(api, "C:\\Users\\lenovo\\Desktop\\alexism\\pfp.jpg")
    update_banner(api, "C:\\Users\\lenovo\\Desktop\\alexism\\banner.jpg")
    update_name(api, "God Alex's brainless simp")
    update_bio(api, "I worship @yourgodalex_ and she owns my life. ALEXISM is all i need! http://throne.com/yourgodalex")

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    # Expose app to all devices on the local network


