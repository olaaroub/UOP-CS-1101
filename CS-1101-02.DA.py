
# Example 1:


def log_event(message): # message is the parameter
	print(f"[INFO] {message}")

# Calling the function
log_event("Server listening on 0.0.0.0") # "server listening on 0.0.0.0" is the argument


# Example 2:


log_event("restarting...") # 1: string literal (value)
status = "Server is up" # 2: variable
log_event(status)
# 3: this expression calculates the string before passing it to the function
log_event("Error code: " + str(401))


# Example 3:


def foo():
	pid = 1337
	return pid

print(pid) #This throws the error: 'NameError: name 'pid' is not defined.
"""
Explanation: The variable pid is allocated in the stack in the function foo().
once the function returns that variable is destroyed. The global scope does not
know any variable named pid.
"""


# Example 4:


def is_digit(number):
	if number >= 0 and number <= 9:
		print(f"{number} is a digit")
	else:
		print(f"{number} is not a digit")

print(number) # This throws the error: 'NameError: name 'number' is not defined.
"""
Explanation: the parameter number does not exist, it only exists while the function is executing
and it gets the value passed to the function as an argument. once the function returns
the parameter is destroyed and the global scope does not know any variable named number.
"""


# Example 5:


holder = 1337

def foo():
	holder = 42
	return holder

foo()
print(holder)

"""
Output:
42
1337
Explanation: The variable "holder" inside the function foo() is created as local variable that shadows
the global "holder", modifying the local variable inside the function does not affect the global one.
"""



