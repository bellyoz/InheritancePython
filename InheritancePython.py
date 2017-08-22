class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)
    
class Student(Person):
   
    firstName = ""
    lastName = ""
    idNumber = 0
    scores = []
    
    def __init__(self, firstName, lastName,idNumber, scores):
        Person.__init__(self, firstName, lastName,idNumber)
        self.scores = scores

  
    def calculate(self):
        prom = sum(self.scores) / len(self.scores)
        if(prom >= 90 and prom <= 100):
            return 'O'
        elif(prom >= 80 and prom < 90):
            return 'E'
        elif(prom >= 70 and prom < 80):
            return 'A'
        elif(prom >= 55 and prom < 70):
            return 'P'
        elif(prom >= 40 and prom < 55):
            return 'D'
        elif(prom < 40):
            return 'T'
            
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
    
