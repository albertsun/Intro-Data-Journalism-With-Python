Intro to Data Journalism With Python
====================================

A lot of the basic tasks of data journalism require scripting literacy and the ability to move bits of data around. In this course, I'll try and take you from knowing nothing about programming to knowing enough to do some basic analysis.

In this set of lessons we go over the basics of opening files, counting things, searching for data with regular expressions and parsing web pages with the BeautifulSoup module.
We'll go through enough python to scrape a university regisrar website and find out which timeslots are the most popular for classes.

The first school we analyze (Penn) the class listings are in plain text so we just use regular expressions.
The second set of listings (CUNY City College) are formatted as HTML so we use the Python package BeautifulSoup to parse them.

Here's how to follow along
--------------------------

1.    Make sure you have Python and a text editor installed.
        
      If you're on a Mac, Python comes installed. You'll want to be sure to install a text editor. Something like Textmate, BBEdit, etc. I like TextWrangler (the free, lite version of BBEdit, http://www.barebones.com/products/textwrangler/ )

      If you're on Windows, I'm less sure of how to get things running, but you can download it here. Make sure to get a Python 2 version, not Python 3. Link here ( http://www.python.org/getit/releases/2.7.2/ ) A text editor I like there is Notepad++ ( http://notepad-plus-plus.org/ )

      If you're on Linux, you probably know what to do. If you're not sure (and you're on Ubuntu), try finding your terminal and entering "sudo apt-get install python2.7 gedit"


2.    Open up your terminal (on a Mac, look in /Applications/Utilities/Terminal.app) and navigate to the folder that these files are in. For example, enter this to change directories

      `$ cd ~/Desktop/Intro-Data-Journalism-With-Python`

      Throughout, commands that are to be typed on the command line will be prefixed with a dollar sign. So on the above line, the first letter you'd type would be the 'c' in 'cd'.

3.    Take a look in the directories pennregistrar/ and citycollege/

      That's where the data files that we're going to use are located. They're just simple HTML pages downloaded using the Save As option from a web browser. To grab lots of files all at once, there's a Firefox extension called DownThemAll.

4.    Open the file analyze_penn.py in your text editor and look through it, to see what you can understand.
Lines that start with a pound sign (#) are comments and are not executed by the computer.

      The files sample1.py to sample5.py build up this, so it'll help to see what you're trying to accomplish.

      Now go back to your terminal and run the file.

      `$ python analyze_penn.py`

      You should see a whole bunch of lines of times fly by and at the end two lines with the number of total classes found, and the top 10 most popular time slots for classes.

      Now we'll work through the samples up to there.

5.    Read through each of sample1.py through sample6.py reading the code and comments. Try running each one from the command line to see the output.

      `$ python sample1.py`

--

To learn more, try these resources
----------------------------------

Intro to Python in a more general way
http://learnpythonthehardway.org/

Reference on how to use regular expressions
http://www.regular-expressions.info/

Documentation for BeautifulSoup is here.
http://www.crummy.com/software/BeautifulSoup/documentation.html

--

Data Sources:
Penn course data from http://www.upenn.edu/registrar/timetable/ and downloaded using http://www.downthemall.net/
City College course data from http://www1.ccny.cuny.edu/current/registrar/index.cfm
