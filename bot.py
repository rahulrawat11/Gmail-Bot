#################################################################
#                                                               #
# Gmail Bot Created By Dominic Peel https://github.com/P-aradox #
#             https://github.com/P-aradox/Gmail-Bot             #
#                                                               #
#################################################################

from splinter import Browser
import time
import random

email = ""
password = ""
start_time = time.time()
version = "1.4.3"
page_load = 1
action_wait = 0.5

with Browser("firefox") as browser:
    browser.visit("http://mail.google.com/mail/h/")
    time.sleep(page_load)
    browser.fill("Email", email)
    time.sleep(action_wait)
    browser.fill("Passwd", password)
    time.sleep(action_wait)
    browser.find_by_name("signIn").click()
    time.sleep(page_load)
    try:
        browser.find_by_value("I'd like to use HTML Gmail").click()
        time.sleep(page_load)
    except:
        pass
    while True:
        browser.visit("http://mail.google.com/mail/h/")
        time.sleep(page_load)
        browser.fill("q", "is:unread")
        time.sleep(action_wait)
        browser.find_by_value("Search Mail").click()
        time.sleep(action_wait)
        if browser.is_element_present_by_tag("tr"):
            try:
                browser.find_link_by_partial_href("=is:unread&v=c&s=q").click()
                time.sleep(page_load)

                if browser.is_text_present("!rps"):
                    try:
                        if browser.is_text_present("rock"):
                            userChoice = "rock"
                        elif browser.is_text_present("paper"):
                            userChoice = "paper"
                        elif browser.is_text_present("scissors"):
                            userChoice = "scissors"
                        computerChoice = random.randint(0,2)
                        if computerChoice == 0:
                            computerChoice = "rock"
                        elif computerChoice == 1:
                            computerChoice = "paper"
                        elif computerChoice == 2:
                            computerChoice = "scissors"
                        if computerChoice == userChoice:
                            browser.fill("body", ("You choose ", userChoice, ", computer chooses ", computerChoice, ". Draw!"))
                            time.sleep(action_wait)
                            browser.find_by_value("Send").click()
                            time.sleep(action_wait)
                        elif userChoice == "rock":
                            if computerChoice == "paper":
                                browser.fill("body", ("You choose ", userChoice, ", computer chooses ", computerChoice, ". You lose!"))
                                time.sleep(action_wait)
                                browser.find_by_value("Send").click()
                                time.sleep(action_wait)
                            elif computerChoice == "scissors":
                                browser.fill("body", ("You choose ", userChoice, ", computer chooses ", computerChoice, ". You Win!"))
                                time.sleep(action_wait)
                                browser.find_by_value("Send").click()
                                time.sleep(action_wait)
                        elif userChoice == "paper":
                            if computerChoice == "rock":
                                browser.fill("body", ("You choose ", userChoice, ", computer chooses ", computerChoice, ". You win!"))
                                time.sleep(action_wait)
                                browser.find_by_value("Send").click()
                                time.sleep(action_wait)
                            elif computerChoice == "scissors":
                                browser.fill("body", ("You choose ", userChoice, ", computer chooses ", computerChoice, ". You lose!"))
                                time.sleep(action_wait)
                                browser.find_by_value("Send").click()
                                time.sleep(action_wait)
                        elif userChoice == "scissors":
                            if computerChoice == "rock":
                                browser.fill("body", ("You choose ", userChoice, ", computer chooses ", computerChoice, ". You lose!"))
                                time.sleep(action_wait)
                                browser.find_by_value("Send").click()
                                time.sleep(action_wait)
                            elif computerChoice == "paper":
                                browser.fill("body", ("You choose ", userChoice, ", computer chooses ", computerChoice, ". You Win!"))
                                time.sleep(action_wait)
                                browser.find_by_value("Send").click()
                                time.sleep(action_wait)
                    except:
                        browser.fill("body", "Invalid input: please enter !rps rock/paper/scissors")
                        time.sleep(action_wait)
                        browser.find_by_value("Send").click()
                        time.sleep(action_wait)

                elif browser.is_text_present("!coinflip"):
                    coin = random.randint(0,1)
                    if coin == 0:
                        coin = "Heads!"
                    elif coin == 1:
                        coin = "Tails!"
                    browser.fill("body", coin)
                    time.sleep(action_wait)
                    browser.find_by_value("Send").click()
                    time.sleep(action_wait)
                    
                elif browser.is_text_present("!diceroll"):
                    dice = random.randint(1,6)
                    browser.fill("body", (dice, " rolled!"))
                    time.sleep(action_wait)
                    browser.find_by_value("Send").click()
                    time.sleep(action_wait)
                    
                elif browser.is_text_present("!help"):
                    browser.fill("body", ("Availavle commands:", "\n", "Flip a coin: !coinflip", "\n", "Free cookies!: !cookie", "\n", "Roll a dice: !diceroll", "\n", "Greet the bot: !greet", "\n", "View available commands: !help", "\n", "Information about bot: !info", "\n", "Check the bot is alive: !ping", "\n", "Play rock, paper, scissors against bot: !rps rock/paper/scissors"))
                    time.sleep(action_wait)
                    browser.find_by_value("Send").click()
                    time.sleep(action_wait)
                                    
                elif browser.is_text_present("!info"):
                    browser.fill("body", ("Email Bot ", version, " created by Dominic Peel. !help for available commands. View on GitHub: https://github.com/P-aradox/Gmail-Bot"))
                    time.sleep(action_wait)
                    browser.find_by_value("Send").click()
                    time.sleep(action_wait)
                    
                elif browser.is_text_present("!ping"):
                    browser.fill("body", "Pong!")
                    time.sleep(action_wait)
                    browser.find_by_value("Send").click()
                    time.sleep(action_wait)
                                    
                elif browser.is_text_present("!greet"):
                    browser.fill("body", "Hello!")
                    time.sleep(action_wait)
                    browser.find_by_value("Send").click()
                    time.sleep(action_wait)

                elif browser.is_text_present("!cookie"):
                    browser.fill("body", "Free Cookie!")
                    time.sleep(action_wait)
                    browser.find_by_value("Send").click()
                    time.sleep(action_wait)
                    
            except:
                pass
