# UCJournalBot
Tired of fake applying for jobs for a measly £80 per week? Fed up leaving it to the last minute to update your journal, so you don't get sanctioned? Is your work coach busting your balls because they hate their own life? You've come to the right place.

Introducing UCJournalBot, an AI powered bot trained on anti-government propaganda, with a particular disgust for tories. With just a few settings you can outsource your journal updating task to the bot and get on with more important things.

#### Table of Contents
- [Requirements](#requirements)
- [Install](#install)
- [Setup](#setup)
- [Run](#run)

# Requirements
You will need Git and Python installed on your machine.

Install Git by visiting the [official website](https://git-scm.com/downloads) and downloading the appropriate version for your operating system.

Install Python by visiting the [official website](https://www.python.org/downloads/) and downloading the latest version.

A couple of python packages are required, they can be installed with the following command.

```
pip install requests lxml tomli
```

# Install
Clone the repository from GitHub by running the following command

```
git clone git@github.com:DoleGallagher/UCJournalBot.git
```

# Setup
In order to set up and tailor the bot you will need to edit the settings.toml file found in the settings folder of the cloned repo. The following outlines the necessary settings:

### API Key
An API Key is needed from [Reed.co.uk](https://www.reed.co.uk/developers/jobseeker) to search for jobs. The key included in the settings works right now but may not continue to if multiple people use it so its advised you get your own key.

### Keywords
You will find some defaults in the settings file, these should be edited to suit the type of jobs you are pretending to apply for as per your agreements.

### Date Range
A start and end date should be supplied, probably a 2-week period between your appointments. The jobs will be recorded as having been applied for in this period.

### Location
A city is required and a mile radius for which you are "prepared to travel" to "work". This is to get local search results just like you would using the website search.

### Jobs per day
This setting determines how many jobs you will "apply for" each day, initially set to 2. You can turn this up if you have a particularly depressed work coach who hates the fact that you don't need to get up in the morning and who's only joy in life is demanding more from you despite your government handout not affecting their lives at all.

### Cookies - IMPORTANT
In order to send valid requests to the government website, a couple of cookies need to be present. 'sessionId' and 'uctx' tokens are issued when you log in, and they expire regularly so will need to be updated every time you use the bot.

The following instructions show how to find these using the developer tools of your browser. These values should be copied into the settings.toml file.

**You must be logged into UC or these values won't be valid.**

#### Chrome

Open Chrome and press F12 to open the developer tools or right-click anywhere on the page and select "Inspect"
Click on the "Application" tab in the developer tools. Under the "Storage" section, click on "Cookies" to view and manage cookies for the current website.

![Cookies](https://i.postimg.cc/1tfPD3YY/cookies.png)

#### Firefox

Open Firefox and press F12 to open the developer tools or right-click anywhere on the page and select "Inspect Element"
Click on the "Storage" tab in the developer tools.
Under the "Cookies" section, you can view and manage cookies for the current website.

#### Safari

Open Safari and press Option+Command+C to open the developer tools or right-click anywhere on the page and select "Inspect Element"
Click on the "Storage" tab in the developer tools.
Under the "Cookies" section, you can view and manage cookies for the current website.



### Run
To run the bot, navigate to the UCJournalBot folder in your terminal, wherever you git cloned it.

```
cd path/to/UCJournalBot
```

Then execute the following command:
```
python3 UCJournalBot.py
```

If your settings are correct the bot will finish in a few seconds and your journal will be updated.