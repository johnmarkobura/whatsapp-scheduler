# WhatsApp Scheduler

A Python automation script that sends scheduled WhatsApp messages to multiple recipients across time zones. Built as a practical application of Anthropic's 4D AI Framework.

## What It Does

Automatically sends personalized WhatsApp messages to multiple people via WhatsApp Web. Each person gets a custom message tailored to their needs. No more manual messaging or scheduling errors.

## Requirements

- Python 3.x
- WhatsApp Web logged in on your browser
- Internet connection

## Installation

```bash
git clone https://github.com/johnmarkobura/whatsapp-scheduler.git
cd whatsapp-scheduler
pip install pywhatkit keyboard
```

## Usage

1. Open `wedding_reminders.py`
2. Edit the `messages` dictionary with your recipients' phone numbers (include country codes like +256) and custom messages
3. Make sure WhatsApp Web is open and logged in
4. Run: `python wedding_reminders.py`
5. Don't touch your keyboard or mouse while it runs

## How It Works

The script loops through your contacts, opens WhatsApp Web for each one, sends their personalized message, waits 10 seconds, then moves to the next person. If a message fails, it logs the error and continues.

## Built With

- Python
- pywhatkit (WhatsApp Web automation)
- Anthropic's 4D AI Framework (Delegation, Description, Discernment, Diligence)

## License

MIT License - Free to use for personal or educational purposes.

## Contact

John Mark Obura - oburajohnmark7@gmail.com - [LinkedIn](https://linkedin.com/in/johnmarkobura)
