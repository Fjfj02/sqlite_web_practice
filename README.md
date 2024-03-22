# SQLite and SQLAlchemy Practice

## Purpose

This project is based on databases and their connection to the web, specifically, Flask and Jinja

It was based on the same course as other projects that are on my GitHub.

## Overview

It works very simply. When you enter the home page, you will be faced with a library and an add books button. As you can see my current library:

<p align="center">
  <img src="https://github.com/Fjfj02/sqlite_web_practice/assets/84993558/7e998c33-3147-44f7-b339-b1131a3d688e">
</p> 

Moving on to the next page, just enter your book details and submit.

<p align="center">
  <img src="https://github.com/Fjfj02/sqlite_web_practice/assets/84993558/cfd4c92f-2084-402b-aa0a-46298d9d37c6">
</p>

You can also edit the rating of books by clicking on the button next to them, being redirected to the following screen, where you can just change the rating:

<p align="center">
  <img src="https://github.com/Fjfj02/sqlite_web_practice/assets/84993558/2d8e1a28-8813-4a64-aa64-7290aa109c99">
</p>

And if you want to delete a book from your library, just click the delete button next to it.

## Run code

First you have to install the following library:

```shell
python -m pip install -r requirements.txt
```

To run the code, use:

```shell
python3 main.py
```

So, just follow the flask link.

## Change of data

If you want to change the default database, just delete the book.db file in the instance folder.
