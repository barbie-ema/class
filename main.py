class Student():
    def __init__(self,name,age,track,score):
        self.name = name
        self.age = age
        self.track = track
        self.score = score 
        print("My name is", name,", I am", age," and I am on the on", track," track with a score of", score)

    def speak (self):     
        pass

Bob = Student(name="Bob", age=26, track=["FE","BE"],score=20.90)
Peter  = Student(name="Peter", age=34, track=["UI/UX"],score=30)
