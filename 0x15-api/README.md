1. Write me

Write a script that writes a string to a file.

The first argument is the file path

The second argument is the string to write

The content of the file must be written in utf-8

If an error occurred during while writing, print the error object

guillaume@ubuntu:~/0x14$ ./1-writeme.js my_file.txt "Python is cool"
guillaume@ubuntu:~/0x14$ cat my_file.txt ; echo ""
Python is cool
guillaume@ubuntu:~/0x14$
Repo:

GitHub repository: holbertonschool-higher_level_programming
Directory: 0x14-javascript-web_scraping
File: 1-writeme.js
2. Status code

Write a script that display the status code of a GET request.

The first argument is the URL to request (GET)

The status code must be printed like this: code: <status code>

You must use the module request
