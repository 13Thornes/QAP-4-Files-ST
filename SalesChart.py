#Description: Program that generates a chart for the total monthly sales of a company
#Date: 11/26/2023
#Author: Samantha Thorne

#Define necessary contants

#Import required libraries
from matplotlib import pyplot as plt
from matplotlib import style

#Define program Functions

#Start the main program
while True:
    style.use('ggplot')

    xLst = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    yLst = []



    for month in xLst:
        Amount = yLst.append(input(f"Enter the total sales amount for {month}: "))

    fig, ax = plt.subplots()

   

    ax.bar(xLst, yLst, align='center')

    ax.set_title('Monthly Sales Report')
    ax.set_ylabel('Total Sales ($)')
    ax.set_xlabel('Months')

    ax.set_xticks(xLst)
    ax.set_xticklabels(("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"))

    plt.show()

    Continue = input("Do you want to continue? (Y / N)").upper()
    if Continue == "N":
        print("Thank you for using this program")
        break