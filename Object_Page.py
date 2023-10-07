
class StudentObject:
    def __init__(self, rollNo, name, branch, total_fees, paid, remain):
        self.rollNo = rollNo
        self.name = name
        self.branch = branch
        self.total_fees = total_fees
        self.paid = paid
        self.remain = remain
        

    def __str__(self):
        return str(self.rollNo) + "," + self.name + "," + self.branch + "," + str(self.total_fees) + "," + str(self.paid) + "," + str(self.remain)
    

