def printList(toDolist):
    """this is a function to list all items one by one"""
    for index,item in enumerate(toDolist):
        print(str(index + 1) + ". " + item.strip("\n"))

def readTodo(files):
    with open(files,'r') as readFile:
        todoList = readFile.readlines()
        return todoList

def writeToDo(file,toDoList):
    file = open(file, 'w')
    file.writelines(toDoList)
    file.close()

if __name__=="__main__":
    todoList=readTodo("../Files/todo_gui.txt")
    print(todoList)
    printList(todoList)

