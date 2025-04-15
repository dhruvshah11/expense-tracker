# Expense Tracker & Bill Splitter

A comprehensive web application built with Streamlit that helps users track their expenses and split bills with friends. The application provides an intuitive interface for managing personal finances and shared expenses.

## Features

### Expense Tracking
- Track daily expenses with detailed information
- Categorize expenses (Food, Transportation, Housing, etc.)
- Visualize spending patterns through interactive charts
- View expense history and summaries
- Real-time expense analytics with pie charts and timeline views

### Bill Splitting
- Split bills equally among multiple participants
- Add detailed bill descriptions and amounts
- Track split bill history
- View individual shares for each participant
- Maintain a record of all shared expenses

### User Management
- Secure user authentication system
- Personal user accounts with email registration
- Password encryption using secure hashing
- Individual expense tracking for each user

## Technology Stack

- **Frontend Framework**: Streamlit
- **Data Visualization**: Plotly Express
- **Data Management**: Pandas
- **Data Storage**: CSV-based file system
- **Security**: Werkzeug security for password hashing

## Project Structure

```
├── app.py                 # Main application file with UI and core logic
├── user_manager.py        # User authentication and management
├── csv_data_manager.py    # Data persistence and retrieval
├── expense_manager.py     # Expense tracking functionality
├── bill_manager.py        # Bill splitting functionality
├── requirements.txt       # Project dependencies
├── users.csv             # User data storage
├── expenses.csv          # Expense records storage
└── bills.csv            # Bill splitting records storage
```

## Setup Instructions

1. Install Python 3.x on your system
2. Clone the repository
3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   streamlit run app.py
   ```

## Usage Guide

### Getting Started
1. Register a new account or login with existing credentials
2. Navigate between Expense Tracker and Bill Splitter using the sidebar

### Tracking Expenses
1. Select "Expense Tracker" from the navigation
2. Fill in expense details:
   - Description
   - Amount
   - Category
   - Date
3. Click "Add Expense" to record the transaction
4. View expense analytics and history below the input form

### Splitting Bills
1. Select "Bill Splitter" from the navigation
2. Enter bill details:
   - Description
   - Total Amount
   - Participant names (comma-separated)
   - Split type (Equal/Custom)
3. Click "Split Bill" to calculate individual shares
4. View bill history in the expandable sections below

## Data Management

The application uses CSV files for data storage:
- `users.csv`: Stores user account information and encrypted passwords
- `expenses.csv`: Records all user expenses with categories and dates
- `bills.csv`: Maintains bill splitting records and participant information

## Security Features

- Passwords are securely hashed using Werkzeug's security functions
- User sessions are managed securely through Streamlit's session state
- Data is stored locally with proper access controls

## Future Enhancements

- Custom bill splitting ratios
- Export functionality for expense reports
- Monthly budget tracking and alerts
- Multi-currency support
- Cloud data synchronization