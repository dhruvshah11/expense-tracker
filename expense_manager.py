from typing import Dict, List

class ExpenseManager:
    def __init__(self):
        self.expenses: List[Dict] = []
    
    def add_expense(self, expense: Dict) -> None:
        """Add a new expense to the list"""
        if not self._validate_expense(expense):
            raise ValueError("Invalid expense format")
        self.expenses.append(expense)
    
    def get_expenses(self) -> List[Dict]:
        """Get all expenses"""
        return self.expenses
    
    def get_total_expenses(self) -> float:
        """Calculate total expenses"""
        return sum(float(expense['amount']) for expense in self.expenses)
    
    def get_expenses_by_category(self, category: str) -> List[Dict]:
        """Get expenses filtered by category"""
        return [expense for expense in self.expenses if expense.get('category') == category]
    
    def _validate_expense(self, expense: Dict) -> bool:
        """Validate expense data structure"""
        required_fields = ['amount', 'category', 'description', 'date']
        return all(field in expense for field in required_fields) and \
               isinstance(expense['amount'], (int, float, str)) and \
               float(expense['amount']) > 0