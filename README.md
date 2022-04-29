## Wordle Cheater

----------------------------------------------------------------
### Let's have some fun! 

This little app helps you solve the Wordle daily challenge. Does not solve it for you! for now...

Crawler option will be added later (feel free to fork and make PR). That would be the real cheating! ;)

### How do I cheat?
For now, I get the input from user in the terminal.
Then, I create an url based on ``wordfinderx.com`` template and get the response.
Next, I use beautiful soup (bs4) to parse the response and get a list of words.
Finally, I process the list based on the other parameters in the challenge.

After all, I suggest the users words they can use to solve the challenge.

### Requirements
Before running the program you need to install the dependencies. Enter the following in the command-line:
``pip install -r requirements.txt``

### How to tun the program
To begin the mischief, first run the following in the command-line:
``python app.py``

Next, in each guess, you will write your first guess and press enter.
Then, you will enter the status of your guess according to the result in wordle app and press enter.

You will see a list of suggestion after a few seconds to help you make your next guess and repeat from top if needed.

### Why?
This repo is a playground for me to learn and experiment things with the Wordle challenge.

I wanted to practice some scarping, unit-testing, and CI/CD. That's all.

### What next?
Maybe I add a crawler option later or a webpage that you can use as interface. Who knows...?