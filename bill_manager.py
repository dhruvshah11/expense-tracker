from typing import Dict, List

class BillManager:
    def __init__(self):
        self.bills: List[Dict] = []
    
    def add_bill(self, bill: Dict) -> None:
        """Add a new bill to the list"""
        if not self._validate_bill(bill):
            raise ValueError("Invalid bill format")
        self.bills.append(bill)
    
    def get_bills(self) -> List[Dict]:
        """Get all bills"""
        return self.bills
    
    def get_total_bills(self) -> float:
        """Calculate total bills amount"""
        return sum(float(bill['amount']) for bill in self.bills)
    
    def get_bills_by_status(self, status: str) -> List[Dict]:
        """Get bills filtered by payment status"""
        return [bill for bill in self.bills if bill.get('status') == status]
    
    def get_bills_by_due_date(self, due_date: str) -> List[Dict]:
        """Get bills filtered by due date"""
        return [bill for bill in self.bills if bill.get('due_date') == due_date]
    
    def _validate_bill(self, bill: Dict) -> bool:
        """Validate bill data structure"""
        required_fields = ['amount', 'description', 'due_date', 'status']
        return all(field in bill for field in required_fields) and \
               isinstance(bill['amount'], (int, float, str)) and \
               float(bill['amount']) > 0