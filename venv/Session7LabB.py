# Has-A Relation
# 1 to 1
# 1 to many

# IS-A Relation
# Inheritance i.e. Parent and Child

# Complete the Code
class Address:
    pass

class Project:
    pass

class Employee:
    def __init__(self, eid, name, salary, address, projects):
        self.eid = eid;
        self.name = name;
        self.salary = salary;
        self.address = address;
        self.projects = projects;

# IS-A Relationship
class SoftwareEngr(Employee):
    pass

address = Address()     # Has A Relation - 1 to 1
projects = []           # Has A Relation - 1 to many

engr = SoftwareEngr()

