import pandas as pd
import os
from typing import Dict, Optional
from werkzeug.security import generate_password_hash, check_password_hash

class UserManager:
    def __init__(self, users_file='users.csv'):
        self.users_file = users_file
        self.create_users_file()
    
    def create_users_file(self) -> None:
        """Create users CSV file if it doesn't exist"""
        if not os.path.exists(self.users_file):
            df = pd.DataFrame(columns=['username', 'password_hash', 'email'])
            df.to_csv(self.users_file, index=False)
    
    def register_user(self, username: str, password: str, email: str) -> bool:
        """Register a new user"""
        try:
            df = pd.read_csv(self.users_file)
            
            # Check if username already exists
            if username in df['username'].values:
                return False
            
            # Hash password and add new user
            password_hash = generate_password_hash(password)
            new_user = pd.DataFrame([
                {'username': username, 'password_hash': password_hash, 'email': email}
            ])
            df = pd.concat([df, new_user], ignore_index=True)
            df.to_csv(self.users_file, index=False)
            return True
        except Exception as e:
            print(f"Error registering user: {str(e)}")
            return False
    
    def verify_user(self, username: str, password: str) -> bool:
        """Verify user credentials"""
        try:
            df = pd.read_csv(self.users_file)
            user = df[df['username'] == username]
            
            if not user.empty:
                stored_hash = user.iloc[0]['password_hash']
                return check_password_hash(stored_hash, password)
            return False
        except Exception as e:
            print(f"Error verifying user: {str(e)}")
            return False
    
    def get_user_info(self, username: str) -> Optional[Dict]:
        """Get user information"""
        try:
            df = pd.read_csv(self.users_file)
            user = df[df['username'] == username]
            
            if not user.empty:
                return {
                    'username': user.iloc[0]['username'],
                    'email': user.iloc[0]['email']
                }
            return None
        except Exception as e:
            print(f"Error getting user info: {str(e)}")
            return None