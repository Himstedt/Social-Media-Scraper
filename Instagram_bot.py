from instabot import Bot


bot = Bot()
bot.login(username="xxx", password="xxx")

#upload a picture
bot.upload_photo("foto.jpg", caption="what you see")

#follow people
bot.follow("who?")

#send a message
bot.send_message("hi", ['target1'], ['target2'])

#find followers of a profile
followers = bot.get_user_followers("profile")
for follower in followers:
    print(bot.get_user_info(follower))

    bot.unfollow_everyone()
