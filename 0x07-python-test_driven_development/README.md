0x07. Python - Test-driven development
/Doctest/ 
Doctest is an inbuilt test framework that comes bundled with Python by default. The doctest module searches for code fragments that resemble interactive Python sessions and runs those sessions to confirm they operate as shown. Simple usage: 1. Checking examples in docstrings -use testmod() function example: if name == "main": import doctest doctest.testmod() doctest examimes the doctstring in module m can run the script with: python m.py or python M.py -v or python -m doctest -v (filename.py extension) -use testfile() function example: import doctest doctest.testfile(filename.txt extension) can run the file with: python -m doctest -v (filename.txt)

/Unittest/ 
Unittest uses methods created in classes to manage tests. It has support for automation, setup, and shutdown code when testing. Unittest has several rich, in-built features that are unavailable in doctest, including generators and group fixture managers like setUp and tearDown.

