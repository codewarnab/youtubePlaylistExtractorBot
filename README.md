# Yt Playlist Extractor Bot 
SEND this bot playlist link it will sent you back each link in MONOSPCAED so that you can copy and download 
check out [Youtube playlist Link extractor](https://telegram.me/PlaylistlinkextractorBot) on Telegram.
If the bot is offline, contact [me](https://telegram.me/blacknut1803) on telegram, so that I can look into it.






## Setting up the database

### steps

1) Go to [mongoDB official site](https://www.mongodb.com/) and login/register.

2) On the Atlas tab, click `create` to create a new cluster.

3) Now configure the cluster as you want such as the cloud service provider, region, cluster tier etc..

4) Now click on the cluster name which will take you to the Overview page.

5) Click `Collections` and create a database called `link_extractor_db`. Inside `link_extractor_db` create a collections called `users`.
6) Now on the left side, under the `Security` click the `Database Access` and add a user. Don't forget to note down the username and password!

7) Now go to `Network Access` right under `Database Access` and check whether `0.0.0.0/0` is in the **IP Access List**. If not, then click `Add IP Address` and add `0.0.0.0/0`.

8) Now everything is set up! But there's still one step left, i.e to copy the mongoDB address to your database to be accessed by Akinator.

9) Now under the `Deployment` tab, click `Databases` and you should see the cluster you created. Now click the button named `Connect`. Choose `Connect your application`. Select `python` as Driver and appropriate version.

10) It should now give you a template string and will give you instructions on what need to be changed/replaced with. It usually askes you to replace `<username>`, `<password>` and `myFirstDatabase`.

11) Do you now remember step 6 ? Where you should have noted down the username and password. yeah, now you have to replace the username, password. And for `myFirstDatabase`, replace it with your `cluster` name.

12) Everything's done! Finally just copy the string and paste it in the appropriate environmenal variable.


 
# Commands
`/start` - Start the bot


## Deployment 
1 . download the repo as zip

2.change the necassary details in .env

3 . `pip install python-telegram-bot` &  `pip install pytube`

4 . python3 main.py
