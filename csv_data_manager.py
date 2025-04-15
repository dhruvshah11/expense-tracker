import pandas as pd
import os
from typing import Dict, List
from datetime import datetime

class CSVDataManager:
    def __init__(self):
        self.expenses_file = 'expenses.csv'
        self.bills_file = 'bills.csv'
        self.create_data_files()
    
    def create_data_files(self) -> None:
        """Create CSV files if they don't exist"""
        if not os.path.exists(self.expenses_file):
            expense_df = pd.DataFrame(columns=[
                'username', 'description', 'amount', 'category',
                'date', 'created_at'
            ])
            expense_df.to_csv(self.expenses_file, index=False)
        
        if not os.path.exists(self.bills_file):
            bills_df = pd.DataFrame(columns=[
                'username', 'description', 'total_amount', 'participants',
                'split_type', 'amount_per_person', 'date', 'created_at'
            ])
            bills_df.to_csv(self.bills_file, index=False)
    
    def add_expense(self, username: str, expense: Dict) -> bool:
        """Add a new expense for a user"""
        try:
            df = pd.read_csv(self.expenses_file)
            expense_data = {
                'username': username,
                'description': expense['description'],
                'amount': expense['amount'],
                'category': expense['category'],
                'date': expense['date'],
                'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            df = pd.concat([df, pd.DataFrame([expense_data])], ignore_index=True)
            df.to_csv(self.expenses_file, index=False)
            return True
        except Exception as e:
            print(f"Error adding expense: {str(e)}")
            return False
    
    def add_bill(self, username: str, bill: Dict) -> bool:
        """Add a new bill for a user"""
        try:
            df = pd.read_csv(self.bills_file)
            bill_data = {
                'username': username,
                'description': bill['description'],
                'total_amount': bill['total_amount'],
                'participants': ','.join(bill['participants']),
                'split_type': bill['split_type'],
                'amount_per_person': bill['amount_per_person'],
                'date': bill['date'],
                'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            df = pd.concat([df, pd.DataFrame([bill_data])], ignore_index=True)
            df.to_csv(self.bills_file, index=False)
            return True
        except Exception as e:
            print(f"Error adding bill: {str(e)}")
            return False
    
    def get_user_expenses(self, username: str) -> List[Dict]:
        """Get all expenses for a user"""
        try:
            df = pd.read_csv(self.expenses_file)
            user_expenses = df[df['username'] == username]
            return user_expenses.to_dict('records')
        except Exception as e:
            print(f"Error getting expenses: {str(e)}")
            return []
    
    def get_user_bills(self, username: str) -> List[Dict]:
        """Get all bills for a user"""
        try:
            df = pd.read_csv(self.bills_file)
            user_bills = df[df['username'] == username]
            # Convert participants string back to list
            bills = user_bills.to_dict('records')
            for bill in bills:
                bill['participants'] = bill['participants'].split(',')
            return bills
        except Exception as e:
            print(f"Error getting bills: {str(e)}")
            return []
    
    def get_user_total_expenses(self, username: str) -> float:
        """Get total expenses for a user"""
        try:
            df = pd.read_csv(self.expenses_file)
            return df[df['username'] == username]['amount'].sum()
        except Exception as e:
            print(f"Error calculating total expenses: {str(e)}")
            return 0.0