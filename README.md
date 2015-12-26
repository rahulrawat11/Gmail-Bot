# Python Gmail Bot
Gmail Bot written in Python and Splinter by [Dominic Peel](https://github.com/P-aradox).

# Commands
Send command to bot in email in the subject or message:

Command |Parameters |Description
 -------- | ----------- | ----------- 
!coinflip||Flips a coin.
!cookie||Free cookies!
!diceroll||Roll a dice.
!greet||Greet the bot.
!help||View available commands.
!info||View information about the bot.
!ping||Check the bot is alive.
!rps|rock/paper/scissors|Play rock, paper, scissors against the bot.

# LICENSE
The MIT License (MIT)

Copyright (c) 2015 Dominic Peel

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

# Installation
1. Download and install Python 3 from [python.org](https://www.python.org/downloads/).
2. Download and install Splinter:
 * If you don't already have pip, follow this [installation guide](https://pip.pypa.io/en/stable/installing/).
 * Install Splinter from a terminal using the command:
  * `$ [sudo] pip install splinter`

# Configuring the Gmail Bot
1. Save bot.py to a directory of your choice.
2. Open bot.py in IDLE and edit:
 * `email = ""` with your gmail email.
 * `password = ""` With your gmail password *(Note - Anyone with access to the python code can see your password)*.
3. Save bot.py and exit IDLE.
4. Open up your terminal and navigate to the directory where bot.py is saved, for example:
 * `cd Desktop`
5. Run `python bot.py`.
6. Your bot should work now!

# Author
The Python Gmail Bot was created by [Dominic Peel](https://github.com/P-aradox).

# Bugs and Requests
Submit bugs and requests [here](https://github.com/P-aradox/Gmail-Bot/issues/new).
Please post bugs in the following format:
 * Overview of bug or problem
 * Error from console
