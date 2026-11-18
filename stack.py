class stack:
    def __init__(self):
        self.list=[]
    def push(self,x):
        self.list.append(x)
    def pop(self):
        self.list.pop((len(self.list)-1))
    def display(self):
        print(self.list)
num=stack()
x=input('Enter number to add: ')
n=input('Enter number to add: ')
num.push(x)
num.push(n)
num.display()
num.pop()
num.display()