'''Capstone template project for FCS Task 19 Compulsory task 1.
This template provides a skeleton code to start compulsory task 1 only.
Once you have successfully implemented compulsory task 1 it will be easier to
add a code for compulsory task 2 to complete this capstone'''

# =====importing libraries===========
'''This is the section where you will import libraries'''
from datetime import date

# Temp variables to store
assigned_to = ''
task = ''
assigned_date = ''
due_date = ''
task_completed = ''
task_description = ''

# ====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''

# Create empty dictionary and list
# To store the user details ie. username and password
user_details = {}
task_dict = {}
usernames_list = []
password_list = []
task_list = []

count = 1

with open('user.txt', 'r+') as file1:  # Open the user.txt file
    for lines in file1:
        newline = lines.strip('\n')  # Strip and new line on the file
        split_line = newline.split(", ")  # Split the newline using a ', '

        # Add the user details into username_list and password_list
        usernames_list.append(split_line[0])
        password_list.append(split_line[1])

        # Update the user_details info
        user_details['Username'] = usernames_list
        user_details['password'] = password_list

while True:

    # Request user to log in
    username = input('enter username: ')
    user_password = input('enter password: ')

    # If the username and password are in the user.txt
    # The user can use the program
    if (username in usernames_list) and (user_password in password_list):

        # After logging in start use the program
        # presenting the menu to the user and
        # making sure that the user input is converted to lower case.
        while True:
            menu = input('''Select one of the following Options below:
        r - Registering a user
        a - Adding a task
        va - View all tasks
        vm - view my task
        ds - Display statics
        e - Exit
        : ''').lower()

            if menu == 'r':
                '''In this block you will write code to add a new user to the user.txt file
                - You can follow the following steps:
                    - Request input of a new username
                    - Request input of a new password
                    - Request input of password confirmation.
                    - Check if the new password and confirmed password are the same.
                    - If they are the same, add them to the user.txt file,
                    - Otherwise you present a relevant message.'''

                # Request user input for new user.
                new_username = input('Enter the new username:')
                password = input('Enter the password:')
                confirm_password = input('Confirm the password: ')

                # If confirmed password and password are the same
                # And new_name is admin, then user can register a user.
                if password == confirm_password:

                    # Add the user into the user_list, password_list and user_details
                    usernames_list.append(new_username)
                    password_list.append(confirm_password)

                    # Update the user_details
                    user_details['Username'] = usernames_list
                    user_details['password'] = password_list

                    # Open the user.txt file as file2
                    # To add the new user details
                    with open('user.txt', 'w+') as file2:

                        # Create a for loop to write the user_details
                        for i in range(len(password_list)):
                            # Write the user_details into file2
                            file2.write(user_details['Username'][i] + ', ' + user_details['password'][i] + '\n')
                    print(f'The new user has been registered successfully. ')
                else:
                    print(f'The new user password is not the same as confirmed  or username is not admin. ')
            elif menu == 'a':

                '''In this block you will put code that will allow a user to add a new task to task.txt file
                    - You can follow these steps:
                    - Prompt a user for the following:
                    - A username of the person whom the task is assigned to,
                    - A title of a task,
                    - A description of the task and
                    - the due date of the task.
                    - Then get the current date.
                    - Add the data to the file task.txt and
                    - You must remember to include the 'No' to indicate if the task is complete.'''

                # Request users info and task info
                Username = input('Enter the new username: ')
                title_task = input('Enter the title of task: ')
                description = input('Enter the description of the task: ')
                due_date = input('Enter the due date of the task: (e.g 2022-04-11)')
                task_completed = input('Enter if the task is complete or Not: (Yes or No)')
                current_date = str(date.today())

                # Update the task_list to keep count of it later.
                # Along with task_dict
                task_list = [Username, task, task_description, assigned_date, due_date, task_completed]
                task_dict[f'Task number {count} information: '] = task_list

                # Now add this information to the task.txt
                task_file = open('tasks.txt', 'w+')
                text = f"""{Username}, Register Users with taskManager.py, Use taskManager.py to add the username \nand passwords for all team members that will be using this program., '\n{current_date},\n{due_date}, No \n{Username}, {title_task}, {description}, {current_date}, {due_date},' {task_completed}""".format(
                    Username, current_date, due_date, Username, title_task, description, current_date, due_date,
                    task_completed)
                task_file.write('\n' + text)
                task_file.close()  # Close the file

            elif menu == 'va':
                '''In this block you will put code so that the program will read the task from task.txt file and
                    print to the console in the format of Output 2 presented in the L1T19 pdf file page 6
                    You can do it in this way:
                    - Read a line from the file.
                    - Split that line where there is comma and space.
                    - Then print the results in the format shown in the Output 2 in L1T19 pdf
                    - It is much easier to read a file using a for loop.'''
                # Open the task file
                task_file = open('tasks.txt', 'r+')
                task_dict = {}
                for lines in task_file:
                    line = lines.strip()
                    last_line = line.strip().split(',')
                    if len(last_line) == 6:
                        for column in range(len(last_line)):
                            task = last_line[1]
                            assigned_to = last_line[0]
                            assigned_date = last_line[3]
                            due_date = last_line[4]
                            task_completed = last_line[-1]
                            task_description = last_line[2]

                            # Create a task_list to store all the above data
                            task_list = [username, task, task_description, assigned_date, due_date, task_completed]
                text = f'''Task: {task}\nAssigned to: {assigned_to}\nDate assigned: {assigned_date}\nDue date: {due_date}\nTask complete? {task_completed}\nTask description: {task_description}'''.format(task, assigned_to, assigned_date, due_date, task_completed,task_description)

                task_dict[f'Task number {count} information: '] = task_list
                count += 1
                print(text)
                print(task_dict)

            elif menu == 'vm':

                '''In this block you will put code the that will read the task from task.txt file and
                     print to the console in the format of Output 2 presented in the L1T19 pdf
                     You can do it in this way:
                        - Read a line from the file
                        - Split the line where there is comma and space.
                        - Check if the username of the person logged in is the same as the username you have
                        read from the file.
                        - If they are the same you print the task in the format of output 2 shown in L1T19 pdf '''

                # Open the task file.
                task_file = open('tasks.txt', 'r+')
                # Create a count for number of tasks
                task_count = 0
                for lines in task_file:
                    line = lines.strip()
                    last_line = line.strip().split(',')
                    if len(last_line) % 6 == 0:
                        for column in range(len(last_line)):
                            task = last_line[1]
                            assigned_to = last_line[0]
                            assigned_date = last_line[3]
                            due_date = last_line[4]
                            task_completed = last_line[-1]
                            task_description = last_line[2]
                            task_list = [assigned_to, task, task_description, assigned_date, due_date, task_completed]
                # Update the task_list to keep count of it later.
                # Along with task_dict
                task_dict[f'Task number {task_count} information: '] = task_list

                for key in task_dict:

                    # Update the count
                    task_count += 1
                    # Check if the task if assigned to the user logged in
                    if username == (task_dict[key][0]):
                        text = f''' Task {str(task_count)}: {str(task_dict[key][1])}\n'Assigned to: {str(task_dict[key][0])}'\n'Date assigned: {str(task_dict[key][3])}'\n'Date: {str(task_dict[key][4])}'\n'Task Complete? {str(task_dict[key][5])}'\n'Task Description: {str(task_dict[key][2])}'''
                        print(text)
                    else:
                        print('The username of person logged in is not the same as username on from the file')

            elif menu == 'ds':
                task_file = open('tasks.txt', 'r+')
                task_dict = {}
                for lines in task_file:
                    line = lines.strip()
                    last_line = line.strip().split(',')
                    if len(last_line) % 6 == 0:
                        for column in range(len(last_line)):
                            task = last_line[1]
                            assigned_to = last_line[0]
                            assigned_date = last_line[3]
                            due_date = last_line[4]
                            task_completed = last_line[-1]
                            task_description = last_line[2]

                            # Create a task_list to store all the above data
                            task_list = [username, task, task_description, assigned_date, due_date, task_completed]

                task_dict[f'Task number {count} information: '] = task_list
                count += 1

                total_user = len(user_details['Username'])
                print(f'The total users are: {total_user}')
                print(f'The total task {len(task_dict)}')

            elif menu == 'e':
                print('Goodbye!!!')
                exit()
    else:
        print('The username and password entered are not registered, try again....')

file1.close()
