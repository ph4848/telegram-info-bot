# Telegram Movie Info Bot

A Persian-language Telegram bot that allows users to search for movie information by movie ID or title. The bot uses the Movies API to retrieve movie details and provides interactive menus, news links, and support commands.

## Features

- `/start` — Start the bot.
- `/help` and `/support` — Display support information.
- `/news` — Show buttons linking to sports, general, and financial news.
- `/menu` — Display the interactive menu.
- `/movie` — Search for a movie by its ID.
- `/movie_name` — Search for a movie by its title.
- Persian-language responses and keyboard navigation.

## Technologies

- Python
- pyTelegramBotAPI
- Requests
- Movies API: https://moviesapi.ir/

## Project Structure

```text
telegram-movie-info-bot/
├── src
    |├── app.py
    └── app_api.py
├── requirements.txt
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/ph4848/telegram-info-bot.git
cd telegram-movie-info-bot
```

### 2. Create a virtual environment

On Windows:

```powershell
py -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can use Command Prompt instead:

```bat
.venv\Scripts\activate.bat
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```


### 4. Run the bot

```bash
python app.py
```

Once the bot starts, open it in Telegram and send `/start`.

## Usage

Use the following commands in your Telegram chat:

| Command | Description |
|---|---|
| `/start` | Start the bot |
| `/help` | Get support information |
| `/support` | Get support information |
| `/news` | Open news links |
| `/menu` | Open the interactive menu |
| `/movie` | Search by movie ID |
| `/movie_name` | Search by movie title |

## Notes

- An internet connection is required.
- Movie information depends on the availability of the external Movies API.
- API failures and movies with no search results should be handled gracefully.
- The contact details and news links can be customized for your needs.
