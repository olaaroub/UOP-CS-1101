"""
CS 1101 - Discussion Assignment 01: Setting Up Python Environment

Overview:
Hello and welcome to your first computer science assignment! Before you begin
exploring the world of programming, you must finish the task of setting up the
programming environment. Let's get started!

Setup Instructions:
Download and install a working Python environment, preferably Python 3, or get
an account with PythonAnywhere. Please refer to the Software Requirements/Installation
section located in the course syllabus for details.

Assignment Tasks:
Type the statements below into your Python interpreter. For each statement, copy
the output into your Discussion Assignment and explain the output. Compare it with
any similar examples in the textbook, and describe what it means about your version
of Python.

>>> print 'Hello, World!'
>>> 1/2
>>> type(1/2)
>>> print(01)
>>> 1/(2/3)

Requirements:
- The code and its output must be explained technically whenever asked.
- The explanation can be provided before or after the code, or in the form of code
  comments within the code.
- For any descriptive type of question, your answer must be at least 150 words.
- End your discussion post with one question related to programming fundamentals
  learned in this unit from which your colleagues can formulate a response or
  generate further discussion.
- Remember to post your initial response as early as possible, preferably by
  Sunday evening, to allow time for you and your classmates to have a discussion.

Peer Response:
When you reply to your peers' submissions, compare their results with yours.
Reply to two (2) of your classmates' posts.

NOTE: Remember to post as early as possible, preferably by Sunday evening,
in order to allow time for you and your classmates to discuss.
"""

print("--- Experiment 1: print 'Hello, World!' ---")


try:
	result = eval("print 'Hello, World!!'")
except Exception as e:
	print(f"Output: {e}\n")
else:
	print(result)

print("--- Experiment 2: 1/2 ---")

try:
	result = 1/2
except Exception as e:
	print(f"Output: {e}\n")
else:
	print(result)

print("--- Experiment 3: type(1/2) ---")

try:
	result = eval("type(1/2)")
except Exception as e:
	print(f"Output: {e}\n")
else:
	print(result)

print("--- Experiment 4: print(01) ---")

try:
	result = eval("print(01)")
except Exception as e:
	print(f"Output: {e}")

print("--- Experiment 5: 1/(2/3) ---")

try:
	result = eval("1/(2/3)")
except Exception as e:
	print(f"Output: {e}\n")
else:
	print(result)
