# Discord Bot for Minecraft Server Management
A Python-powered Discord bot for managing Minecraft server communities with integrated commands, rule enforcement, and a seamless connection to the Minecraft server for enhanced user engagement.

# Features
• Customizable Prefix: Set a unique prefix to access the bot’s commands.
• Automated Status Updates: Updates bot’s status every 10 seconds, displaying the number of servers it's active in.
• Detailed Help Command: Users can easily access a list of available commands with +help.
• Comprehensive Rule Commands: Separate commands for different rule categories (e.g., minor, major, staff rules).
• Minecraft Server Integration: Provides server IP, in-game commands, and rule explanations.
• Continuous Operation: Integrated with a minimal Flask server to keep the bot active on platforms like Replit.

# Requirements
• Python 3.6+
• discord.py library for Discord API interaction
• Flask for web server functionality

Install dependencies with:
`pip install discord flask`

# Usage
1. Clone or Download the Project
   `git clone https://github.com/yourusername/minecraft-discord-bot.git
cd minecraft-discord-bot`
3. Set Up Your Bot Token
  Replace "YOUR_BOT_TOKEN" in the bot.run() function with your actual Discord bot token.
4. Run the Bot
   `python bot.py`

# Commands

## General Commands

- **`+help`**: Lists all commands and descriptions.
- **`+ip`**: Displays the Minecraft server’s IP address.
- **`+tienda`**: Shares a link to the server’s online donation store.
- **`+normas`**: Introduces server rules, categorized by severity.

## Rule Commands

Each command below provides users with specific server rules:

- **`+leves`**: Minor rule violations
- **`+graves`**: Severe rule violations
- **`+juicio`**: Trial rules
- **`+staff`**: Staff-specific rules
- **`+clanes`**: Clan rules

### Minecraft Commands

- **`+comandos`**: Lists all available in-game commands, such as teleportation and economic commands.

## Continuous Operation with Web Server

To prevent the bot from timing out, especially on Replit, the project includes a Flask web server. The server runs continuously and responds with “I’m alive” to indicate uptime.

## Future Improvements

- Implementing command-specific cooldowns to avoid spam.
- Adding real-time data integration from Minecraft for more dynamic features.
- Logging user interactions for better error management.
