# Qwenzie Ticket Bot

Qwenzie is a Discord bot designed to streamline the ticketing process in your server. With Qwenzie, users can create tickets for support, report issues, or request assistance, and staff members can manage these tickets efficiently.

## Features

- **Ticket Creation**: Users can create tickets by using a simple command or reacting to a specific message.
- **Ticket Management**: Staff can view, close, and manage tickets directly within Discord.
- **Customizable**: Configure Qwenzie to fit the needs of your server with various settings and options.
- **Logging**: All ticket actions are logged for transparency and record-keeping.
- **Permissions**: Fine-tune who can create, view, and manage tickets with role-based permissions.

## Installation

1. **Clone the Repository**
   \`\`\`bash
   git clone https://github.com/samarth3301/Qwenzie.git
   cd Qwenzie
   \`\`\`

2. **Set Up Environment Variables**
   Create a \`.env\` file in the project root and add the following:
   \`\`\`env
   ENVDATABASE_URL=your_database_url_here
   TOKEN=[your_discord_client_token]
   \`\`\`

   - \`ENVDATABASE_URL\`: The URL of your database.
   - \`OWNER_IDS\`: A list of Discord user IDs who will have owner-level access to the bot.

3. **Run the Bot**
   \`\`\`bash
   docker compose up --build
   \`\`\`

## Contributing

We welcome contributions! Please fork the repository and create a pull request with your changes. Make sure to follow the code style and include tests for any new features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Support

If you encounter any issues or have questions, feel free to open an issue on GitHub or join our [Discord server](https://discord.gg/techsolace).

---

Happy ticketing with Qwenzie!
