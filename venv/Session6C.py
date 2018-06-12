class Employee:

    def __init__(self, name, designation, salary, projects):
        self.name = name
        self.designation = designation
        self.salary = salary
        self.projects = projects # HAS-A Relation with 1 to Many

    def showEmployee(self):
        print("{} works as {} and withdraws {} INR".format(self.name,self.designation,self.salary))

        #Iterate in the projects
        for p in self.projects:
            p.showProject()


class Project:
    def __init__(self, title, technology, duration):
        self.title = title
        self.technology = technology
        self.duration = duration

    def showProject(self):
        print("{} is developed in {} technology in a timeline of {} months".format(self.title,self.technology,self.duration))


# Collection : List or Projects
projectList = []
projectList.append(Project("Elzo","Firebase",2))
projectList.append(Project("YankTow","AWS",3))

emp = Employee("John Watson", "Software Engr", 30000, projectList)
emp.showEmployee()