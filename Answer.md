# Answer

Statement 1: ">>> print 'Hello, World!!'"
Output: "SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?"
Explanation: This command results in a SyntaxError. In Python 3, print is a function, not a statement as it was in Python 2. Because it is a function, you need parentheses () to call it (all programming languages use () to call functions). When the parser reads the print token and finds the string 'Hello, World!!' instead of an opening parenthesis, it stops and throws this error. This confirms the note in the textbook Think Python (Ch 1.3) that "in Python 2, the print statement... is not a function, so it doesn't use parentheses."

Statement 2: ">>> 1/2"
Output: "0.5"
Explanation: In Python 3, the operator / performs floating point division, which gives a float value (0.5) Even if both numbers are intergers. This behavior is referenced in Think Python (Ch 1.4), which notes that division like 84/2 results in a float (42.0)..
However in Python 2, that same command "1/2" would result in "0", because the / operator would find that 1 and 2 are integers,
so the result must be integer (the same for c/c++), to perform the floating point division, at least one of the numbers must be float (1.0/2 = 0.5). To get the normal integer division in Python 3, we should use the // operator (1 // 2 = 0).

Statement 3: ">>> type(1/2)"
Output: "<class 'float'>"
Explanation: The type function first performs the operation "1/2" and see that the result is of class float, then it returns it.
This confirms that Python 3 performs floating point division on integer numbers, which results in float.

Statement 4: ">>> print(01)"
Output: "SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers"
Explanation: Python 3 does not allow leading zeros on decimal integers. This was enforced because in Python 2 and C/C++, putting a leading 0 before a decimal number converts it to octal base (base 8) ( int a = 010 => a = 8). That was implicit and a source of bugs for a long time. That's why python devs chose to solve this imbiguity by telling you to use 0o prefix for octal base or remove the 0 for decimal.

Statement 5: ">>> 1/(2/3)"
Output: "1.5"
Explanation: The interpreter evaluates the expression in parentheses (2/3) first, this is noted in Think Python (Ch 2.5).
