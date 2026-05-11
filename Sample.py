'''
The CSU Global Bookstore has a book club that awards points to its students based on the number of
 books purchased each month. The points are awarded as follows:
    If a customer purchases 0 books, they earn 0 points.
    If a customer purchases 2 books, they earn 5 points.
    If a customer purchases 4 books, they earn 15 points.
    If a customer purchases 6 books, they earn 30 points.
    If a customer purchases 8 or more books, they earn 60 points.
Write a program that asks the user to enter the number of books that they have purchased this month and then 
display the number of points awarded.
'''

def main():
    try:
        books = int(input("Enter the number of books purchased this month: "))
        if books < 0:
            print("Books cannot be negative. Please try again.")
            return
        
        if books >= 8:
            points = 60
        elif books >= 6:
            points = 30
        elif books >= 4:
            points = 15
        elif books >= 2:
            points = 5
        else:
            points = 0
            
        print(f"Points awarded: {points}")
        
    except ValueError:
        print("Error: Oops! Invalid input. Please try again")

if __name__ == "__main__":
    main()
