# def manage_employees():
#     employees = [
#         "Ahmed", "Sarah", "Youssef", "Fatima", "Omar",
#         "Layla", "Hassan", "Amina", "Khalid", "Zainab"
#     ]
#     print(f"Original List: {employees}")

#     # 2. Split the list into two sub-lists (5 names each)
#     # We use slicing [start:end]
#     subList1 = employees[:5]
#     subList2 = employees[5:]
#     print(f"\nSubList 1: {subList1}")
#     print(f"\nSubList 2: {subList2}")

#     # 3. Add new employee "Kriti Brown" to subList2
#     # The append() method adds an element to the end of the list
#     subList2.append("Kriti Brown")
#     print(f"SubList 2 after adding Kriti: {subList2}")

#     # 4. Remove the second employee's name from subList1
#     # Lists are 0-indexed, so the 2nd employee is at index 1.
#     # We use the del statement or pop().
#     removed_emp = subList1.pop(1)
#     print(f"Removed '{removed_emp}' from SubList 1: {subList1}")

#     # 5. Merge both lists
#     # The + operator concatenates two lists
#     merged_list = subList1 + subList2
#     print(f"\nMerged List ({len(merged_list)} employees): {merged_list}")

#     # --- Salary Operations ---

#     # 6. Assume a salary list for these 10 employees
#     salaryList = [45000, 52000, 61000, 48000, 75000, 39000, 82000, 56000, 67000, 90000]
#     print(f"\nOriginal Salaries: {salaryList}")

#     # 7. Give a rise of 4% to every employee
#     # We iterate through the list by index to update values in-place
#     for i in range(len(salaryList)):
#         # Multiplying by 1.04 is equivalent to adding 4%
#         salaryList[i] = salaryList[i] * 1.04

#     print(f"Salaries after 4% raise: {salaryList}")

#     # 8. Sort the SalaryList and show top 3 salaries
#     # sort() modifies the list in-place. reverse=True sorts Descending (High to Low)
#     salaryList.sort(reverse=True)

#     # Slicing the first 3 elements gives the top 3 salaries
#     top_3_salaries = salaryList[:3]
#     print(f"Top 3 Salaries: {top_3_salaries}")

# # Execute the function
# manage_employees()



#PART B

def process_sentence():
    # 1. Define the sentence
    sentence = "Python is a powerful language for data analysis"
    print(f"Original Sentence: '{sentence}'")

    # 2. Convert sentence into a wordlist
    # The split() method breaks the string at whitespace by default
    wordlist = sentence.split()
    print(f"Wordlist: {wordlist}")

    # 3. Reverse the wordlist
    # We can use the list method .reverse() which modifies the list in-place
    wordlist.reverse()
    print(f"Reversed Wordlist: {wordlist}")

# Execute the function
process_sentence()