''' Write a class “TODOreminder” that will help us handling our TODOs list. This class should keep
track of current pending todos using a list attribute. The class should moreover expose 3
methods:
a. “list_todo”: List all present todos togheter with their index in the list
b. “new_todo”: Add a new todo to the list
c. “remove_todo”: Remove a todo from the list given an index  '''

todo_list=list()

class TODOreminder: #superclass
    def CreateList(self,task):
        global todo_list
        todo_list.append(task)
        return todo_list

    def DisplayList(self):
        global todo_list
        return todo_list

    def DeleteList(self,task_id):
        global todo_list
        for an in todo_list:
            todo_list.remove(task_id)
     #todo_lis.pop(task_id)
        return todo_list
while True:
    print("1:Create New Task")
    print("2:Display Task List")
    print("3:Delete Task")

    inp=int(input("Please select Options: "))

    if inp==1:
        task=input("Enter New ToDo: ")
        obj1= TODOreminder()
        p=obj1.CreateList(task)

    elif inp==2:
        obj1= TODOreminder()
        test_list = obj1.DisplayList()
        for i in range(len(test_list)):
            print(i,end= "")
            print(test_list[i])
        #print("your ToDO",p)
    elif inp==3:
        task_remove=int(input("Enter index of TODo: "))
        p=obj1.DeleteList(task)
        test_list= obj1.DisplayList()
        for i in range(len(test_list)):
            print(i,end= "")
            p(test_list[i])
        print(p)
    else:
        print("Invalid Input!")
