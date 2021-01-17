# Python Book Scraper

This is a tiny project I am using to learn python!

It is a web scraper of the site http://books.toscrape.com.

It gets all of the books in the catalouge using async http calls.

However the site doesn't accept that many connections,
so the fact that it is async does not make a significant performance difference.

It is currently quite slow. I will work on speeding that up at a later date.

You can start this application by ensuring the dependencies are installed and by running `python menu.py`

I am using pipenv to manage my dependencies.

I am logging to a file called logs.txt that is not being version controlled.

The logging is exaggerated, I would likely not log this way in a production deployment, I am just learning the tool.

This project is my interpretation and extension of an example in the [The Complete Python Course](https://www.udemy.com/course/the-complete-python-course/).
