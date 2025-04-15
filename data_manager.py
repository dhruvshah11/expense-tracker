import json
import os
from typing import Dict, List
from expense_manager import ExpenseManager
from bill_manager import BillManager

class DataManager:
    def __init__(self, file_path='data.json'):
        self.file_path = file_path
        self.expense_manager = ExpenseManager()
        self.bill_manager = BillManager()
        self.load_data()
    
    def load_data(self) -> None:
        """Load data from JSON file if it exists"""
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r') as f:
                    data = json.load(f)
                    for expense in data.get('expenses', []):
                        self.expense_manager.add_expense(expense)
                    for bill in data.get('bills', []):
                        self.bill_manager.add_bill(bill)
            except json.JSONDecodeError:
                print(f"Error reading {self.file_path}. Using default empty data.")
    
    def save_data(self) -> None:
        """Save current data to JSON file"""
        try:
            data = {
                'expenses': self.expense_manager.get_expenses(),
                'bills': self.bill_manager.get_bills()
            }
            with open(self.file_path, 'w') as f:
                json.dump(data, f)
        except Exception as e:
            print(f"Error saving data: {str(e)}")
    
    def add_expense(self, expense: Dict) -> None:
        """Add a new expense and save to file"""
        self.expense_manager.add_expense(expense)
        self.save_data()
    
    def add_bill(self, bill: Dict) -> None:
        """Add a new bill and save to file"""
        self.bill_manager.add_bill(bill)
        self.save_data()
    
    def get_expenses(self) -> List[Dict]:
        """Get all expenses"""
        return self.expense_manager.get_expenses()
    
    def get_bills(self) -> List[Dict]:
        """Get all bills"""
        return self.bill_manager.get_bills()
    
    def get_total_expenses(self) -> float:
        """Get total expenses amount"""
        return self.expense_manager.get_total_expenses()
    
    def get_total_bills(self) -> float:
        """Get total bills amount"""
        return self.bill_manager.get_total_bills()