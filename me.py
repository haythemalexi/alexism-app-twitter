import tweepy
from flask import Flask, redirect, request, session, url_for
api_key= 'AFQCy36DfgqFcTV6mmKGb1mk1'
api_secret_key= 'coOkfkLcocVccCYiUxGrLtG50Vd80kP3i2gEQjMbYqd6ci4w7Q'
access_token='1694053108060397569-FgA5HaAcJkF7qn3deBOyyaoiRU1pZ8'
access_token_secret='O9efAlYZkeNuTrI8e5vkBj4H2tHscPwjUZIgvu6rhE5oF'

auth=tweepy.OAuthHandler(api_key,api_secret_key)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)

auth_url=auth.get_authorization_url()
print(auth_url)
app = Flask(__name__)
app.secret_key = 'coOkfkLcocVccCYiUxGrLtG50Vd80kP3i2gEQjMbYqd6ci4w7Q'
auth = tweepy.OAuth1UserHandler(api_key, api_secret_key)

@app.route('/login')
def login():
    try:
        # Get request token
        auth_url = auth.get_authorization_url()
        session['request_token'] = auth.request_token
        return redirect(auth_url)
    except tweepy.TweepError:
        return 'Error! Failed to get request token.'

# Callback route after Twitter login
@app.route('/callback')
def callback():
    try:
        request_token = session.get('request_token')
        auth.request_token = request_token

        # Get access token
        auth.get_access_token(request.args['oauth_verifier'])
        api = tweepy.API(auth)

        # Now authenticated, you can update the Twitter profile
        update_profile(api)

        return 'Successfully authenticated and profile updated!'
    except tweepy.TweepError:
        return 'Error! Failed to get access token.'


def update_pfp(image_path):
    try:
        api.update_profile_image(image_path)
        print("pfp updated successfully")
    except Exception as e:
        print(f"Error updating pfp: {e}")
def update_banner(image_path):
    try:
        api.update_profile_banner(image_path)
        print("banner updated successfully")
    except Exception as e:
        print(f"Error updating banner: {e}")
def update_name(new_name):
    try:
        api.update_profile(name=new_name)
        print("name updated successfully")
    except Exception as e:
        print(f"Error updating name: {e}")
def update_bio(new_bio):
    try:
        api.update_profile(description=new_bio)
        print("bio updated successfully")
    except Exception as e:
        print(f"Error updating bio: {e}")
        
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    update_pfp("C:\\Users\\lenovo\\Desktop\\alexism\\pfp.jpg")
    update_banner("C:\\Users\\lenovo\\Desktop\\alexism\\banner.jpg")
    update_name("God Alex's brainless simp")
    update_bio("I worship @yourgodalex_ and she owns my life. ALEXISM is all i need! http://throne.com/yourgodalex")


