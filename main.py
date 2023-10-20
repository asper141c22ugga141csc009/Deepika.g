1! = 1 * 1
2! = 2 * 1! --->2 * 1
3! = 3 * 2! --->3 * 2 *1
.
.
10! = 10 * 9! ---> 10 * 9 * 8 * . . . * 1

Formula - n * (n-1)!
"""


def fact_rec(n):
  if n==0 or n==1:
   return 1
  else:
   return n*fact_rec(n-1)

number = int(input("Enter a value : "))
res = fact_rec(number)
print("The factorial of ",number," is ",res)
"""
year % 4 == 0 &
year % 100 != 0 /
year % 400 == 0
"""
def isleapyear(year):
  if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    return True
  else:
    return False

year = int(input("Enter a year : "))

if isleapyear(year):
  print('{} is a leap year.'.format(year))
else:
   print('{} is not a leap year.'.format(year))
0 comments on commit ed16a98class BankAccount:

 def __init__(self, account_number, account_holder_name, initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance

 def deposit(self, amount):
    if amount > 0:
      self.__account_balance += amount
      print("Deposited ₹{}. New balance: ₹{}".format(amount,self.__account_balance))

    else:
      print("Invalid deposit amount, Please deposit a positive amount.")

 def withdraw(self, amount):
   if amount > 0 and amount <= self.__account_balance:
    self.__account_balance -= amount
    print("Withdrew ₹{}. New balance: ₹{}".format(amount, self.__account_balance))

   else:
     print("Invalid withdrawal amount or insufficient balance.")

 def display_balance(self):
    print("Account balance for {} (Account #{}: ₹{}".format)
    self.__account_holder_name, self.__account_number,
    self.__account_balance


account = BankAccount(account_number="123456789",
                      account_holder_name="Ruba",
                      initial_balance=5000.0)

account.display_balance()
account.deposit(500.0)
account.withdraw(200.0)
account.display_balance()class player:
  def play(self):
    print("The player is playing cricket.")

# define the derived class batsman
class Batsman(player):
  def play(self):
    print("The Batsman is batting.")

# define the derived class bowler
class Bowler(player):
  def play(self):
    print("The Bowler is bowling.")

# create object of Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

# call the play() method for each object
batsman.play()
bowler.play()class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(students):
    return sorted(students, key=lambda student: student.cgpa, reverse=True)

# Test the function with different input lists of students
students = [
    Student("Alice", "1", 9.5),
    Student("Bob", "2", 9.0),
    Student("Charlie", "3", 8.5),
]

sorted_students = sort_students(students)
for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")