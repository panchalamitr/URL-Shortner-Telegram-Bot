# URL Shortener Telegram Bot

This is a Telegram bot that shortens URLs using the TinyURL API.

## Import necessary modules:
        telegram: to interact with the Telegram API
        pyshorteners: to shorten URLs
        validators: to validate URLs

## Explaination

    Initialize the bot and shortener instances using telegram.Bot() and pyshorteners.Shortener() respectively.

    Define the start() function which sends a welcome message to the user when they start the bot.

    Define the shorten_url() function which takes the user's input URL and attempts to shorten it. Before shortening, the URL is validated using the validators.url() function. If it is not a valid URL, an error message is sent to the user. If it is a valid URL, pyshorteners.Shortener().tinyurl.short() is used to shorten it. If an error occurs during shortening, an error message is sent to the user.

    Define the error() function to log any errors that occur during the bot's operation.

    Set up the bot by creating an instance of telegram.ext.Updater and adding handlers for the 'start' command and any message that is not a command.

    Add the error handler to log any errors.

    Start the bot by calling the start_polling() method of the updater instance.

    Call the idle() method of the updater instance to keep the bot running until it is stopped.
