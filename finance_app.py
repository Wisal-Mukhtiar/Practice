class Bill:
    def __init__(self, bill_detail, spent):
        self.bill_detail=bill_detail
        self.spent=spent
        self.breakfast=[]
        self.lunch=[]
        self.dinner=[]
        self.totalspent=0
        self.available=[]
        self.extra=[]
    
        if self.bill_detail=="breakfast" or self.bill_detail=="BreakFast":
            self.breakfast.append(spent)        
        
        elif self.bill_detail=="dinner" or self.bill_detail=="Dinner":
            self.breakfast.append(spent)        
        
        elif self.bill_detail=="=Lunch" or self.bill_detail=="Lunch":
            self.breakfast.append(spent)        
        
        else:
            self.extra.append(spent)


    def __repr__(self):
        return f"< Bill({self.bill_detail}, {self.spent}) >"  
    
    def spent_amount(self):
        for amount in self.lunch:
            self.totalspent+=amount

        for amount in self.breakfast:
            self.totalspent+=amount
        
        for amount in self.dinner:
            self.totalspent+=amount
        
        for amount in self.extra:
            self.totalspent+=amount
        
    def show_total_spent(self):
        return f"Total amount spent ==> {self.totalspent}"    


 # Comment 1 removed for the change 