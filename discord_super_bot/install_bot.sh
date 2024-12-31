#!/usr/bin/env bash
# install_bot.sh
# A script to set up the Discord bot on Debian 11

# Exit on errors
set -e

echo "=== Updating and upgrading system packages ==="
sudo apt-get update
sudo apt-get upgrade -y

echo "=== Installing Python3, pip, and ffmpeg ==="
sudo apt-get install -y python3 python3-pip python3-venv ffmpeg git

# Check if directory for the bot already exists or not
if [ ! -d "discord_super_bot" ]; then
  echo "=== Cloning discord_super_bot repository (adjust URL if needed) ==="
  git clone https://github.com/skizap/discord_super_bot.git
fi

cd discord_super_bot

echo "=== Setting up Python virtual environment ==="
python3 -m venv venv
source venv/bin/activate

echo "=== Installing requirements ==="
pip install -r requirements.txt

echo "=== Installation complete! ==="
echo "Now create or edit your .env file with the DISCORD_BOT_TOKEN."
echo "Then run 'source venv/bin/activate' and 'python main.py' to start the bot."
