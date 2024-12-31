
Markdown
## Tutorial: How to Install & Run on Debian 11 VPS

Below are detailed steps assuming you are starting with a fresh Debian 11 server.

### Step 1: Update & Upgrade

```bash
sudo apt-get update
sudo apt-get upgrade -y
Step 2: Install Required Packages
You need Python 3.9+ and ffmpeg for music playback:

sudo apt-get install -y python3 python3-pip python3-venv ffmpeg git
Step 3: Clone Your Bot Repository (or Upload Your Files)
Using git to clone:

bash
git clone https://github.com/yourusername/discord_super_bot.git
cd discord_super_bot
If you don’t have git, you can use scp or any other method to upload your files to the server.

Step 4: Create and Activate a Virtual Environment
bash
python3 -m venv venv
source venv/bin/activate
Step 5: Install Python Dependencies
pip install -r requirements.txt
Step 6: Create Your .env File
Inside the project folder:

nano .env
Add the following line:

DISCORD_BOT_TOKEN=YOUR_BOT_TOKEN_HERE
Replace YOUR_BOT_TOKEN_HERE with the token from the Discord Developer Portal.

Step 7: Run the Bot
python main.py
If you see Logged in as <BotName> (ID: <BotID>), your bot is online!

You can edit the file directly on GitHub by navigating to the [README.md file](https://github.com/skizap/discord_super_bot/blob/main/README.md) and clicking the pencil icon to edit.
