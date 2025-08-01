# Birthday Wisher Automation

This project automatically sends personalized birthday emails to people listed in a CSV file. It selects a random letter template, fills in the recipient's name, and sends the email using your Gmail account.

## Features
- Reads birthdays from a CSV file
- Picks a random birthday letter template
- Sends personalized emails automatically
- Can be automated using Windows Task Scheduler or PythonAnywhere

## File Structure
- `main.py` — Main script to send birthday emails
- `birthdays.csv` — List of people and their birthdays
- `letter_templates/` — Folder containing birthday letter templates

## Setup
1. **Clone the repository** and navigate to the project folder.
2. **Install dependencies:**
   ```bash
   pip install pandas
   ```
3. **Configure your email:**
   - Open `main.py` and set `MY_EMAIL` to your Gmail address.
   - Set `MY_PASSWORD` to your Gmail app password (not your main password; see [Google App Passwords](https://support.google.com/accounts/answer/185833)).

## CSV Format (`birthdays.csv`)
```
name,email,year,month,day
shreyas,example.@gmail.com,2005,04,13
```
- Add one row per person. The script checks for birthdays matching today's month and day.

## Letter Templates
Each template should contain `[NAME]` where the recipient's name should appear. Example:

**letter_1.txt**
```
Dear [NAME],

Happy birthday!

All the best for the year!

shresh
```

**letter_2.txt**
```
Hey [NAME],

Happy birthday! Have a wonderful time today and eat lots of cake!

Lots of love,

Angela
```

**letter_3.txt**
```
Dear [NAME],

It's your birthday! Have a great day!

All my love,

Angela
```

## Usage
Run the script manually:
```bash
python main.py
```

## Automating the Script

### 1. Using Windows Task Scheduler
1. Open Task Scheduler and create a new task.
2. Set the trigger to run daily at your preferred time.
3. Set the action to run `python` with the full path to `main.py` as the argument.
4. Make sure your Python environment and dependencies are available in the scheduled context.

### 2. Using PythonAnywhere
1. Sign up at [PythonAnywhere](https://www.pythonanywhere.com/).
2. Upload your project files.
3. Set up a scheduled task in the PythonAnywhere dashboard to run `main.py` daily.
4. Store your credentials securely (never commit real passwords to code).

## Security Note
- Use [App Passwords](https://support.google.com/accounts/answer/185833) for Gmail if you have 2FA enabled.
- Never share your real credentials or commit them to public repositories.

## License

MIT License

Copyright (c) 2024 [shresh shende]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
