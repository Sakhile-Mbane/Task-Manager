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


# ============== Functions ===============

def reg_user(new_username, password, confirm_password):
    ''' In this block you will write code to add a new user to the user.txt file
             - You can follow the following steps:
                - Request input of a new username
                - Request input of a new password
                - Request input of password confirmation.
                - Check if the new password and confirmed password are the same.
                - If they are the same, add them to the user.txt file,
                - Otherwise you present a relevant message.'''

    # If confirmed password and password are the same
    # And new_name is admin, then user can register a user.
    if (new_username not in usernames_list) and password == confirm_password:

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


def add_task(Username, title_task, description, due_date, task_completed, current_date, count=1):
    ''' In this block you will put code that will allow a user to add a new task to task.txt file
        - You can follow these steps:
        - Prompt a user for the following:
        - A username of the person whom the task is assigned to,
        - A title of a task,
        - A description of the task and
        - the due date of the task.
        - Then get the current date.
        - Add the data to the file task.txt and
        - You must remember to include the 'No' to indicate if the task is complete.'''

    # Update the task_list to keep count of it later.
    # Along with task_dict
    task_list.append(Username)
    task_list.append(title_task)
    task_list.append(description)
    task_list.append(current_date)
    task_list.append(due_date)
    task_list.append(task_completed)
    task_dict[f'Task number {count} information: '] = task_list

    count += 1
    print(task_dict)

    # Now add this information to the task.txt
    task_file = open('tasks.txt', 'w+')

    text = f"""{Username}, Register Users with taskManager.py, Use taskManager.py to add the username \nand passwords for all team members that will be using this program., '\n{current_date},\n{due_date}, No \n{Username}, {title_task}, {description}, {current_date}, {due_date},' {task_completed}""".format(
        Username, current_date, due_date, Username, title_task, description, current_date, due_date, task_completed)
    task_file.write('\n' + text)  # Write the text into the task file
    task_file.close()  # Close the file


def view_all(task_file, count=1):
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
        if len(last_line) % 6 == 0:
            for column in range(len(last_line)):
                task = last_line[1]
                assigned_to = last_line[0]
                assigned_date = last_line[3]
                due_date = last_line[4]
                task_completed = last_line[-1]
                task_description = last_line[2]
                # Create a task_list to store all the above data
                task_list = [assigned_to, task, task_description, assigned_date, due_date, task_completed]
    text = f'''Task: {task}\nAssigned to: {assigned_to}\nDate assigned: {assigned_date}\nDue date: {due_date}\nTask complete? {task_completed}\nTask description: {task_description}'''.format(
        task, assigned_to, assigned_date, due_date, task_completed, task_description)

    task_dict[f'Task number {count} information: '] = task_list
    count += 1
    print(text)
    print(task_dict)


def view_mine(task_file):
    '''In this block you will put code the that will read the task from task.txt file and
        print to the console in the format of Output 2 presented in the L1T19 pdf
        You can do it in this way:
                - Read a line from the file
                - Split the line where there is comma and space.
                - Check if the username of the person logged in is the same as the username you have
                read from the file.
                - If they are the same you print the task in the format of output 2 shown in L1T19 pdf '''

    # Create a count for number of tasks
    task_count = 0
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

    # Update the task_list to keep count of it later.
    # Along with task_dict
    task_list = [assigned_to, task, task_description, assigned_date, due_date, task_completed]
    task_dict[f'Task number {task_count} information: '] = task_list

    # Access the dictionary for each task number
    for key in task_dict:
        # Update the count
        task_count += 1
        # Check if the task if assigned to the user logged in
        if username == (task_dict[key][0]):
            # store tasks to display in a easy manner
            text = f'''Task {task_count}: {task_dict[key][1]}\nAssigned to: {task_dict[key][0]}\nDate assigned: {task_dict[key][3]}\nDate: {task_dict[key][4]}\nTask Complete? {task_dict[key][5]}\nTask Description: {task_dict[key][2]}'''
            # display the tasks
            print(text)

        else:
            # display relevant error message if the person logged in is not the same.
            print('The username of person logged in is not the same as username on from the file')

        # allow the user to chose to either specify the task or return to main menu
        task_select = int(input('''Select the below:
                  1-99: Enter a number of task
                  -1: return to menu main '''))

        # open the task file
        with open('tasks.txt', 'r+') as file:
            task_file_info = file.readline()

        # If a user selects -1 to return menu
        if task_select == -1:
            return menu
        else:
            options = input('''Mark as complete or edit,
                    E - edit
                    M - Mark as complete or not (No or Yes)
                     ''').lower()
            # option selected is M
            if options == 'm':

                # Split the task_file using ', ', so to access the last entry and change it to Yes
                # task_details is a list, resulting from splitting above
                task_details = task_file_info.split(',')

                # access the last entry and update the task_details
                if task_details[-1] == ' No\n':
                    # Assign Yes to the last element in the list
                    task_details[-1] = 'Yes\n'
                    print(f'The task is marked as complete (Yes) \n')
                    # Now write the info into a the file
                    text = f'''Task {task_count}: {task_dict[key][1]}\nAssigned to: {task_dict[key][0]}\nDate assigned: {task_dict[key][3]}\nDate: {task_dict[key][4]}\nTask Complete? {task_details[-1].strip()}\nTask Description: {task_dict[key][2]}'''
                    print(text)
                else:

                    print('The task has already been  marked as complete')

            # edit tasks, username and due_date
            elif options == 'e':

                # Split the task_file using ', ', so to access the username and due date
                task_details = task_file_info.split(',')
                if task_details[-1] == ' No\n':

                    # Request user to input the choice to edit
                    choice_to_edit = input('''What do  you wish to edit ( task username or due_date):
                    U - username
                    D - Due date ''').lower()

                    # user selection is to edit username
                    if choice_to_edit == 'u':

                        # Change the user and update the task dictionary
                        task_details[0] = input('Change to username')
                        text = f'''Task {task_count}: {task_dict[key][1]}\nAssigned to: {task_details[0]}\nDate assigned: {task_dict[key][3]}\nDate: {task_dict[key][4]}\nTask Complete? {task_dict[key][5]}\nTask Description: {task_dict[key][2]}'''
                        print(text)

                    elif choice_to_edit == 'd':

                        # Change the due date and update the task_dictionary
                        task_details[-2] = input('Change due date to: ')
                        text = f'''Task {task_count}: {task_dict[key][1]}\nAssigned to: {task_dict[key][0]}\nDate assigned: {task_details[-2]}\nDate: {task_dict[key][4]}\nTask Complete? {task_dict[key][5]}\nTask Description: {task_dict[key][2]}'''
                        print(text)


def generate_reports(count=1):
    task_dict = {}
    with open('user_overview.txt', 'w+') as user_file:
        total_users = str(len(user_details['Username']))
        user_file.write(f'The total number of users to registered to task_manager.py {total_users}')

    with open('tasks.txt', 'r+') as f:
        for lines in f:
            line = lines.strip()
            last_line = line.strip().split(',')
            if len(last_line) % 6 == 0:
                for column in range(len(last_line)):
                    task = last_line[1]
                    username = last_line[0]
                    assigned_date = last_line[3]
                    due_date = last_line[4]
                    task_completed = last_line[-1]
                    task_description = last_line[2]

                    # Create a task_list to store all the above data
                    task_list = [username, task, task_description, assigned_date, due_date, task_completed]

        task_dict[f'Task number {count} information: '] = task_list

        with open('task_overview.txt', 'w+') as f2:
           f2.write('The number of tasks tracked by task manager ' + str(task_dict))

        count += 1

        total_user = len(user_details['Username'])
        print(f'The total users are: {total_user}')
        print(f'The total task {len(task_dict)}')


while True:

    # Request user to log in
    username = input('enter username: ')
    user_password = input('enter password: ')

    # If the username and password are in the user.txt
    # The user can use the program
    if (username in usernames_list) and (user_password in password_list):

        # After logging in start use the program
        # presenting the menu to the user and
        # making sure that the user input is coneverted to lower case.
        while True:

            menu = input('''Select one of the following Options below:
                            r - Registering a user
                            a - Adding a task
                            va - View all tasks
                            vm - view my task
                            gr - generate reports
                            ds - display statistics
                            e - Exit: ''').lower()

            if menu == 'r' and username == 'admin':

                # Request new user inform
                # Confirm the password also
                new_username = input('Enter the new username:')
                password = input('Enter the password:')
                confirm_password = input('Confirm the password: ')

                # Call the reg_user function to register a user
                reg_user(new_username, password, confirm_password)

            elif menu == 'a':

                # Request task inform
                Username = input('Enter the new username: ')
                title_task = input('Enter the title of task: ')
                description = input('Enter the description of the task: ')
                due_date = input('Enter the due date of the task: (e.g 2022-04-11)')
                task_completed = input('Enter if the task is complete or Not: (Yes or No)')
                current_date = str(date.today())

                # Call the add_task function
                add_task(Username, title_task, description, due_date, task_completed, current_date)

            elif menu == 'va':

                # Open the task file
                task_file = open('tasks.txt', 'r+')

                # Call the view_all function
                view_all(task_file)

            elif menu == 'vm':

                # Open the task file.

                task_file = open('tasks.txt', 'r+')
                # Call the view_mine function
                view_mine(task_file)

            elif menu == 'gr':

                generate_reports()

            elif menu == 'ds':

                task_file = open('tasks.txt', 'r+')
                task_dict = {}
                for lines in task_file:
                    line = lines.strip()
                    last_line = line.strip().split(',')
                    if len(last_line) % 6 == 0:
                        for column in range(len(last_line)):
                            task = last_line[1]
                            username = last_line[0]
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
