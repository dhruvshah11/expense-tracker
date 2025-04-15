import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
from user_manager import UserManager
from csv_data_manager import CSVDataManager

# Initialize managers
user_manager = UserManager()
data_manager = CSVDataManager()

# Initialize session state variables
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = None

# Main app layout
st.title('💰 Expense Tracker & Bill Splitter')

# Login/Register System
if not st.session_state.logged_in:
    tab1, tab2 = st.tabs(['Login', 'Register'])
    
    with tab1:
        with st.form('login_form'):
            username = st.text_input('Username')
            password = st.text_input('Password', type='password')
            
            if st.form_submit_button('Login'):
                if user_manager.verify_user(username, password):
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.success('Login successful!')
                    st.rerun()
                else:
                    st.error('Invalid username or password')
    
    with tab2:
        with st.form('register_form'):
            new_username = st.text_input('Username')
            new_password = st.text_input('Password', type='password')
            email = st.text_input('Email')
            
            if st.form_submit_button('Register'):
                if user_manager.register_user(new_username, new_password, email):
                    st.success('Registration successful! Please login.')
                else:
                    st.error('Username already exists')

else:
    # Logout button in sidebar
    if st.sidebar.button('Logout'):
        st.session_state.logged_in = False
        st.session_state.username = None
        st.rerun()
    
    # Sidebar navigation
    page = st.sidebar.radio('Navigation', ['Expense Tracker', 'Bill Splitter'])
    
    if page == 'Expense Tracker':
        st.header('Expense Tracker')
        
        # Input form for new expense
        with st.form('expense_form'):
            description = st.text_input('Description')
            amount = st.number_input('Amount', min_value=0.0, step=0.01)
            category = st.selectbox('Category', [
                'Food', 'Transportation', 'Housing', 'Utilities',
                'Entertainment', 'Shopping', 'Healthcare', 'Other'
            ])
            date = st.date_input('Date')
            
            if st.form_submit_button('Add Expense'):
                expense = {
                    'description': description,
                    'amount': amount,
                    'category': category,
                    'date': date.strftime('%Y-%m-%d')
                }
                if data_manager.add_expense(st.session_state.username, expense):
                    st.success('Expense added successfully!')
                else:
                    st.error('Error adding expense')
        
        # Display expenses
        expenses = data_manager.get_user_expenses(st.session_state.username)
        if expenses:
            df = pd.DataFrame(expenses)
            df['date'] = pd.to_datetime(df['date'])
            
            # Summary statistics
            total_expenses = df['amount'].sum()
            st.metric('Total Expenses', f'${total_expenses:.2f}')
            
            # Expenses by category pie chart
            fig_category = px.pie(df, values='amount', names='category', title='Expenses by Category')
            st.plotly_chart(fig_category)
            
            # Expenses over time line chart
            fig_timeline = px.line(df.groupby('date')['amount'].sum().reset_index(),
                                 x='date', y='amount', title='Expenses Over Time')
            st.plotly_chart(fig_timeline)
            
            # Expense list
            st.subheader('Expense List')
            display_df = df[['date', 'description', 'category', 'amount']].sort_values('date', ascending=False)
            st.dataframe(display_df)
    
    else:  # Bill Splitter page
        st.header('Bill Splitter')
        
        with st.form('bill_form'):
            bill_description = st.text_input('Bill Description')
            total_amount = st.number_input('Total Amount', min_value=0.0, step=0.01)
            participants = st.text_input('Participants (comma-separated names)')
            split_type = st.selectbox('Split Type', ['Equal', 'Custom'])
            
            if st.form_submit_button('Split Bill'):
                if participants and total_amount > 0:
                    participant_list = [name.strip() for name in participants.split(',')]
                    num_participants = len(participant_list)
                    
                    if split_type == 'Equal':
                        amount_per_person = total_amount / num_participants
                        split_details = {
                            'description': bill_description,
                            'total_amount': total_amount,
                            'participants': participant_list,
                            'split_type': split_type,
                            'amount_per_person': amount_per_person,
                            'date': datetime.now().strftime('%Y-%m-%d')
                        }
                        if data_manager.add_bill(st.session_state.username, split_details):
                            st.success('Bill split successfully!')
                            st.write(f'Each person should pay: ${amount_per_person:.2f}')
                            for participant in participant_list:
                                st.write(f'{participant}: ${amount_per_person:.2f}')
                        else:
                            st.error('Error adding bill')
                    else:
                        st.info('Custom split functionality coming soon!')
        
        # Display bill history
        bills = data_manager.get_user_bills(st.session_state.username)
        if bills:
            st.subheader('Bill History')
            for bill in reversed(bills):
                with st.expander(f"{bill['description']} - {bill['date']}"):
                    st.write(f"Total Amount: ${bill['total_amount']:.2f}")
                    st.write(f"Split Type: {bill['split_type']}")
                    st.write(f"Amount per person: ${bill['amount_per_person']:.2f}")
                    st.write("Participants:", ", ".join(bill['participants']))