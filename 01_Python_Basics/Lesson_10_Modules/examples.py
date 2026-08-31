from tracker import ExpenseTracker  # From a module (.py) import its function/class

tracker = ExpenseTracker()  #set tracker as an account
tracker.function

# These uses to handle large number classified account, without any correlations

FILE_PATH = Path(__file__).parent / "expenses.txt" 
# __file__ location of this current file (Lesson10_Modules/file_manager.py) // .parent the folder containing the file (Lesson10_Modules/)
