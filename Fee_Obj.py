from Object_Page import StudentObject

class Fee(StudentObject):
    def __init__(self, rollNo, name, branch, total_fees, paid_fees ):
        super().__init__(rollNo, name, branch, total_fees)
        self.paid_fees = paid_fees

    def __str__(self):
        return str(self.rollNo) + "," + self.name + "," + self.branch + "," + str(self.total_fees) + "," + str(self.paid_fees)
    

    

