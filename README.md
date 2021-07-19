# MatteoBlog
#### Video Demo: https://youtu.be/03QZZJmZhtQ
#### Description:
This is the final project i made for CS50 introduction to computer science course by Harvard University. I liked this a lot, and i'm very thankful to David Malan and all other instructors for having made such a great course for free for whoever wanted to learn more about CS!


### About the project
The blog is just a first page with links to dinamic link routes, with some API calls with NOTION, that is where i store my pages!
When the user first gots into the page, he sees some intro stuff i made for my non-tech friend to know how to use the Notion stuff and learn how to make the pages.

Then i dinamically fecth through api calls all the pages that are present within that notion Database.
These are showed as cards and contain a dinamica link to the blog page.

Then this blog page renders the stuff that he has gotten through the API call.

This is the core of how a blog works! And it's soo cool to learn this now!

Sadly i didn't spent too much time trying to make the site beautiful to look. I justify it telling myself i don't want to work as a web designer or designer in general. I'd like to focus on the code part, and i hope i got that thing right. but i'm a beginner with no mentors, so probably i got many things wrong without knowing it. Anyway i hope i did a good job with this and i'm looking forward to take CS50 ai now. Thank you for this course!


### Why i made this
Some months ago i got an idea to make a blog for one of my friends. This friends reads a lot, and watches many films. He would enjoy so much opening a blog, or having his own personal space on the web to share his passion, his readings, and comments or ratings to the films he saw.
I didn't know how to do it before, so i just hinted at the idea and he liked it a lot. But now, with the new tools that i have thanks to CS50 i tried, and (hopefully successfully) created a working site where he could write (if still interested in this, sadly i doubt about this :sad:) But i made an effort, and i hope the initial hype that he had when i showed this to him could keep this thing going on also later!

#### Back End stuff
The two main files for the backend are the __init__.py files, i called this __init__ and not index because i had some problems with gunicorn, when i was trying to host this on herokuapp, (i hope it is still on!, you can see the web site on this link! https://blogmatteo.herokuapp.com/) anyway this had the main routes, and decided how to route to the pages, you can see the index, who had to do the api calls and pass it through the jinja file, and a error route, that i just used to show up to my non-tech friend what kind of errors i usually get... and his face when he saw the kinds of errors xD) And then dinamically route for the ids. (if the id doesnt exists it just shows blank page, but in this case its the user that entered stuff, because all the links showed there are good links!)

Then there is the Helper where all the APi calls are present, things like query a database, query the content of the page etc. I had to browse notion api calls as described here https://www.notion.so/guides/connect-tools-to-notion-api (love notion btw :D :love:). And i put here also a easy date filter, who just shows the date when the page was made and not also the hour, minute or seconds

### Front end stuff
As i said before, i didn't put too much effort in the design of the page. In the layout you can find almost the same layout given by us in the Lab9 exercise (copy pasted the style, so thank you for making it available :D). (and i have a version on my machine, that is showed in the YT video that just changes that big jumbotron in layout with a not working navbar, not so complicated so i didn't put it here).
for the index page i wrote some instructions for my non - tech friend to read and understand what is needed to be done in order to put on the notion stuff.
I fetched stuff from my own notion, that at this moment is just some pages with content filled by placeholders, just random stuff from wikipedia, just to test that it works well.

In the blog page i just fetched what i got through the api calls. When i made this it was very difficult to juggle with all the sections of the JSON response, but it think this is how it needs to be done in order to be precise, and not just sending some random text.... I think its fine!

### Setup stuff
It was hard the first day when i set up the heroku web server. I didn't know about gunicorn and didn't know how to make it work with Flask App. I had to make research and to do a lot of trial and error, and hopefully it worked, and now it's hosted! :D)
