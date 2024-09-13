# X-Bot

X-Bot is an automated tool for interacting with X (formerly Twitter) using Selenium WebDriver. It provides functionality for logging in, managing followers, and performing various actions on the X platform.

## Features

- Automated login to X
- Retrieve followers and following lists
- Unfollow users who don't follow back
- Scroll through user profiles and timelines

## Prerequisites

- Python 3.7+
- Firefox or Chrome web browser

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/0xthiagomartins/x-bot.git
   cd x-bot
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   Create a `.env` file in the root directory with the following content:
   ```
   TWITTER_USERNAME=your_username
   TWITTER_PASSWORD=your_password
   BROWSER=chrome  # or firefox
   SPEED=1  # Adjust the speed of actions (lower is slower)
   ```

## Usage

To run the X-Bot: