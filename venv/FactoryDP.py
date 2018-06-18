class Plan:
    def __init__(self, data, price):
        self.data = data
        self.price = price

    def showPlan(self):
        pass


class Plan2G(Plan):
    def showPlan(self):
        print(self.data,"GB data in Plan2G is for Rs",self.price)


class Plan3G(Plan):
    def showPlan(self):
        print(self.data, "GB data in Plan3G is for Rs", self.price)


class Plan4G(Plan):
    def showPlan(self):
        print(self.data, "GB data in Plan4G is for Rs", self.price)


class PlanFactory:

    @classmethod
    def getPlan(cls,type):



        if type is 2:
            plan = Plan2G(2,200)
            return plan
        elif type is 3:
            plan = Plan3G(3, 300)
            return plan
        else:
            plan = Plan4G(5, 500)
            return plan



plan = PlanFactory.getPlan(2)
plan.showPlan()