Milestone Project 4<br>
Full Stack Frameworks  With Django

# Trainer Nats Steele

## Overview
<b>[Trainer Nats Steele](https://trainernatssteele.herokuapp.com/)</b> is a site for people wanting to get fit with like minded people using a "Zoom" video call service, provided by Natalie Steele
<br>The site is designed to offer this service to the user in a helpful, user friendly manner.

## User stories
As a.... | I want to... | So that...
---------|--------------|-----------
Site Owner|Attract new clients to use my services|So that I can increase my revenue
Site Owner|Allow registered users to purchase my classes|So that I can build a database for mailing purposes
Site Owner|Add a new class|So that I can offer more classes to my clients
Site Owner|Edit a class|So that I can make changes when needed
Site Owner|Delete a class|So that I can remove obsolete classes when necessary
Casual site browser|See what is available at a glance|So I can get a quick overview of what is on offer before proceeding further on the site
Casual site browser|See a further description of the classes with more detail|So I can decide which class suits my needs
Registered User|Purchase a class on the site|So that I can join classes and get fit<br>

## UX
I have used a simple colour scheme and typography for this site - Trainer Nats Steele already has brand colours from her activity on her Facebook and Instagram accounts, so I have used these two colours sparingly throughout the site, together with black and white.<br>
<br>
Where there is a call to action I have utilised the blue colour to emphasize that an action will occur if pressed, where appropriate further information is displayed when hovering, for example over a button.

<br>

## UI
The user interface  is intuitive with positive or negative feedback provided to the user where appropriate.

## Wireframe


## Features
### Existing Features
1. User registration
2. User login
3. User logout
4. Admin ability to add a new class
5. Admin ability to edit an existing class
6. Admin ability to delete an existing class
7. All users have the ability to view (read) details of an existing class


### Features for the future
1. I would like to accommodate a payment subscription service
2. A feedback (rating) system for those participating in a class
3. User ability to add a rating to a class
4. User ability to mark as a "favourite"



## Technologies used
1. [HTML](https://en.wikipedia.org/wiki/HTML5)
2. [CSS](https://en.wikipedia.org/wiki/CSS)
3. [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
4. [Bootstrap v4.3.1](https://en.wikipedia.org/wiki/Bootstrap_(front-end_framework))
5. [Amazon S3 Storage](https://en.wikipedia.org/wiki/Amazon_S3)
6. [SQLITE3](https://en.wikipedia.org/wiki/SQLite)
7. [POSTGRES](https://en.wikipedia.org/wiki/PostgreSQL)
8. [STRIPE payment services](https://en.wikipedia.org/wiki/Stripe_(company))
9. [ngrok](https://ngrok.com/docs)


## Database & Schemas
I have used SQLite3 for my database in development<br>
I have used postgres for my database in production.<br>

## Testing

My site has been tested using Google Chrome Developer tools to ensure that the screen changes behaviour on different screen resolutions.

Tested on the following browsers:

Google Chrome

Mozilla Firefox


Manual testing has been carried out by my wife and I using the user stories above.<br><br>
HTML and CSS has been validated using [W3 HTML validator](https://validator.w3.org)<br>
JavaScript has been validated using [JSHint](https://validator.w3.org)<br>
Python has been validated using the flake8 linter within VS Code

## Current Known Bugs
The webhook for triggering emails following the purchase of a class is currently not functioning correctly - no email is sent.<br>

## Deployment
This code was developed using Visual Studio Code<br>
It was committed to git and pushed to Github for version control<br>
From there automatic deploys were made via Heroku, where the application is hosted.<br>
<br>To capture the code for continuing development
1. [Use this link](https://github.com/matthewpoyner/trainernats) To go to my GitHub repository
2. Click on green "Code" button
3. This will reveal Clone options
4. Choose "GitHub CLI"
5. Copy the git command shown


<br>Using VS Code
<br>

Create a project folder using explorer.

Open the project folder within VS Code


<br>To install the requirements for this app
 use this command:<br>`pip install -r requirements.txt`
<br>


Ensure that the environment varaiables are stored in a file called env.py:
<br>

<ul>os.environ["DEVELOPMENT"] = 'True'</ul>
<ul>os.environ["SECRET_KEY"] = 'XXX'</ul>
<ul>os.environ["STRIPE_PUBLIC_KEY"] = 'XXX'</ul>
<ul>os.environ["STRIPE_SECRET_KEY"] = 'XXX'</ul>
<ul>os.environ["STRIPE_WH_SECRET"] = 'XXX'</ul>
and that your env.py file is added to your gitignore file to ensure that sensitive information is not committed to GitHub
<br>
<br>
Create a Heroku app and add the following variables under settings
<br> 
Heroku Config Vars:

<ul>AWS_ACCESS_KEY_ID</ul>
<ul>AWS_SECRET_ACCESS_KEY</ul>
<ul>DATABASE_URL</ul>
<ul>DEFAULT_FROM_EMAIL</ul>
<ul>EMAIL_HOST_PASSWORD</ul>
<ul>EMAIL_HOST_USER</ul>
<ul>SECRET_KEY</ul>
<ul>STRIPE_PUBLIC_KEY</ul>
<ul>STRIPE_SECRET_KEY</ul>
<ul>USE_AWS</ul>

Create an Amazon Web Services account and set up an S3 bucket. Once done complete the settings within Heroku.


## To see the deployed website click the link below
[https://trainernatssteele.herokuapp.com/](https://trainernatssteele.herokuapp.com/) 

## Credits


## Acknowledments
Thank you to my mentor for pushing me to be better and for offering me valuable feedback, whilst encouraging me to think outside of the box<br>

A massive thank you and acknowledgement to my wife, for helping me to test the functionality of the site and for putting up with my long hours of being squirrelled away tapping on the keyboard, whilst life seemingly passes us by.<br>

Tutor support has been incredible during the "dark times" of my coding journey (it was a slash in the wrong place!)

Thanks also to my fellow students on Slack for helpful advice.

## Development Notes
### Issues
I used ngrok to expose my local webserver to the internet in order to test the Stripe payments functionality.
<br>
Whilst effective the tunnel closed after a certain period of time (2 hours).<br> 
This meant that when the session had expired I had to create a new tunnel and then update settings.py and the Stripe website with the new URL - this was time ineffective and also caused me to make unecessary changes thinking that something else had stopped working.<br>
An online IDE may be a better solution such as GitPod to avoid these issues as a https address can be provided straight away for Stripe's webhooks, without the need for a tunnel.<br>
However VS Code

### This site is for educational use