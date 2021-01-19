from tasks import like

def chooseTask(optionNumber, login, password):

    if (optionNumber == 1):
        hashtag = input('Inform a hashtag to posts like: #')
        print('')
        like.likeTask(login, password, hashtag)
        

# Program initialization
print('')
print('How automation task you need now?')
print('')
print('1 - Like task')
print('2 - All tasks')
print('')
taskOptionNumber = int(input('Inform a task option number: '))
print('')
login = input('Inform your login: ')
print('')
password = input('Inform your password: ')
print('')

chooseTask(taskOptionNumber, login, password)