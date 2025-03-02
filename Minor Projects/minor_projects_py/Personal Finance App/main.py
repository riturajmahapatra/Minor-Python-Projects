import pandas as pd
import csv
from datetime import datetime
from data_entry import get_amount,get_category,get_date,get_description
import matplotlib.pyplot as plt

class CSV:
    CSV_File = 'finance_traker.csv'
    COLUMNS = ["date", "amount", "category", "description"]
    DATE_FORMAT ="%d-%m-%Y"

    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_File)
        except FileNotFoundError:
            df= pd.DataFrame(columns=cls.COLUMNS) #dataFrame added if file not found
            df.to_csv(cls.CSV_File, index=False) #exporting the dataFrame into CSV file

    @classmethod
    def add_entry(cls,date,amount,category,description):
        new_entry ={
            "date":date,
            "amount":amount,
            "category":category,
            "description":description
        } # storing in oython Dictionary
        with open(cls.CSV_File,"a",newline="") as csvfile: # appending--> "a"
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Entry Added Sucessfully")

    @classmethod
    def get_transactions(cls, start_date,end_date):  # review this transactions again need to clarify
        df = pd.read_csv(cls.CSV_File)
        # converting into datetime objects because they were strings at fist
        try:
            df['date'] = pd.to_datetime(df['date'], dayfirst=True)
        except ValueError as e:
            print(f"Error parsing dates: {e}")
            return pd.DataFrame()
        start_date = datetime.strptime(start_date,CSV.DATE_FORMAT)
        end_date = datetime.strptime(end_date,CSV.DATE_FORMAT)

        # filtering trough mask and loc function
        mask = (df['date']>= start_date) & (df['date']<=end_date)
        filtered_dateFrame = df.loc[mask]

        if filtered_dateFrame.empty:
            print('No trsnsactions were found in this range')
        else:
            print(f'Transactions from {start_date.strftime(CSV.DATE_FORMAT)} to {end_date.strftime(CSV.DATE_FORMAT)}')    
            print(
                filtered_dateFrame.to_string(
                    index= False,formatters = {"date": lambda x: x.strftime(CSV.DATE_FORMAT)}
                )
            )
            total_income = filtered_dateFrame[filtered_dateFrame["category"]=="Income"]["amount"].sum() #pandas functionality
            total_expense = filtered_dateFrame[filtered_dateFrame["category"]=="Expense"]["amount"].sum() #pandas functionality
            print("\nSummary: ")
            print(f'Total Income(I) comes up as {total_income:.2f} \nThe total Expense(E) is at {total_expense:.2f}')
            print(f'Net Savings throughout: {total_income-total_expense:.2f}') #:.2f is for significant digits(2)
        return filtered_dateFrame

def add():
    CSV.initialize_csv()
    date = get_date("Enter the date of the transaction (dd-mm-yyyy) or press 'ENTER' for today's date: ",allow_default=True) 
    amount= get_amount()
    category= get_category()
    description = get_description()
    CSV.add_entry(date,amount,category,description)     



#plotting in matplotlib
def plot_transaction(df):
    df['date'] = pd.to_datetime(df['date'], dayfirst=True)  # Ensure date is in datetime format
    df.set_index('date', inplace=True)

    # Resampling data to daily frequency, filling missing dates with 0
    income_df = df[df['category'] == 'Income'].resample("D").sum().reindex(df.index, fill_value=0)
    expense_df = df[df['category'] == 'Expense'].resample("D").sum().reindex(df.index, fill_value=0)

    plt.figure(figsize=(10, 5))
    plt.plot(income_df.index, income_df['amount'], label='Income', color='g')  # Correct function call
    plt.plot(expense_df.index, expense_df['amount'], label='Expense', color='r')  # Correct function call
    plt.xlabel('Date')
    plt.ylabel('Amount')
    plt.title("Expense and Income Chart")
    plt.legend()
    plt.grid(True)
    plt.show()
    
# main function running the code
def main():
    while True:
        print("1. Add a new transaction")
        print("2. View transactions and summary within a date range")
        print("3. Exit")        
        choice = input('Select between options 1, 2 or 3: ')

        if choice == '1':
            add()
        elif choice == '2':
            start_date = get_date('Enter the start Date in format (dd-mm-yyyy)')    
            end_date = get_date('Enter the end Date in format (dd-mm-yyyy)',allow_default=True)    # allow default when enters it takes the date of today
            df = CSV.get_transactions(start_date,end_date)
            if input('Do you want to see the Graph plot of transactions? [y/N]').lower() == 'y':
                plot_transaction(df)
        elif choice == '3':
            print("Exiting App ... ")
            break
        else:
            print("Invalid Choice it should be between (1-3)")

if __name__ == "__main__":
    main()          