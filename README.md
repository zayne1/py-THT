# Python Magic Squares THT
A Python script allowing user to enter the size of a square, of which a magic squre will be calculated

Background:

A magic square is a square grid of distinct numbers such that each row and column add up to the same number. Further, the two diagonals (from corner to corner) also add up to that number.
An example is the 3x3 magic square (from [Wikipedia](https://en.wikipedia.org/wiki/Magic_square#Magic_constant)) which is shown below: 

![image](https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Magicsquareexample.svg/220px-Magicsquareexample.svg.png) 

Note how the arrows indicate the sum of each row, column, and diagonal. For the purposes of this task we will only be looking at creating a magic square (n x n matrix) where n is odd, e.g. 3x3, 5x5, etc. This is due to the approaches being slightly different depending on the value of n. 


# Setup - Installing Python (Linux):
To see which version of Python 3 you have installed, open a command prompt and run

```
$ python3 --version
```

If you are using Ubuntu 16.10 or newer, then you can easily install Python 3.6 with the following commands:

```
$ sudo apt-get update
$ sudo apt-get install python3.6
```

If you’re using another version of Ubuntu (e.g. the latest LTS release) or you want to use a more current Python, we recommend using the deadsnakes PPA to install Python 3.8:

```
$ sudo apt-get install software-properties-common
$ sudo add-apt-repository ppa:deadsnakes/ppa
$ sudo apt-get update
$ sudo apt-get install python3.8
```

At this point, you may have system Python 2.7 available as well.
```
$ python
```
This might launch the Python 2 interpreter.
```
$ python3
```
This will always launch the Python 3 interpreter.


# Setup - Installing Python (Windows):

1. Open your web browser and navigate to the Downloads for Windows section of the official Python website.
2. Search for Python3
3. Select a link to download either the Windows x86-64 executable installer or Windows x86 executable installer
4. For all recent versions of Python, the recommended installation options include *Pip* and *IDLE*. Older versions might not include such additional features.

# Executing script
```
python3 zayne-THT-MagicSquares.py
```
