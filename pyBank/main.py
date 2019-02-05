# Dependencies
import csv
import os

#File to load
#budget_data=os.path.join("..","pyBank","budget_data.csv")
budget_data=os.path.join("budget_data.csv")

# Open and read csv
with open(budget_data, newline="") as csvfile:
 csvreader = csv.reader(csvfile, delimiter=",")
 #skip the header
 header= next(csvreader)

 #Define the variables and lists
 line_count=0
 PandL_count= 0
 prevval = 0
 revchglist = []
 skiplist = []
 finalmax = 0
 finalmin = 9999999
# Loop through data
 for row in csvreader:
     #get the line count
     line_count = line_count + 1
     #get the total count
     PandL_count = (int(row[1])) + PandL_count
     #Calculate the revenue change between current and next month
     revchg = int(row[1]) - prevval
     prevval = int(row[1])
     #Conditional to find the max row and date
     if revchg > finalmax:
         finalmax = revchg
         finaldate = row[0]
     #Conditional to find the min row and data
     if revchg < finalmin:
         finalmin = revchg
         finaldate2 = row[0]
     #Hold the values of the change in the list
     revchglist.append(revchg)

#Calculate the average of the revenue change
newvar = revchglist[1:]
avglist = sum(newvar)/len(newvar)

#Print the output to screen
print("Financal Analysis")
print("-" * 35)
print("Total Months: " + str(line_count))
print("Total: $" + str(PandL_count))
print("Average Change: $" + str(round(avglist,2)))
print("Greatest Increase in Profits: " + str(finaldate) + " ($" + str(finalmax) + ")")
print("Greatest Decrease in Profits: " + str(finaldate2) + " ($" + str(finalmin) + ")")

#Print the output to a file
fileOut = open("Financal_Analysis.txt", 'w')
fileOut.write("Financal Analysis\n")
fileOut.write("-" * 35 + "\n")
fileOut.write("Total Months: " + str(line_count) + "\n")
fileOut.write("Total: $" + str(PandL_count) + "\n")
fileOut.write("Average Change: $" + str(round(avglist,2)) + "\n")
fileOut.write("Greatest Increase in Profits: " + str(finaldate) + " ($" + str(finalmax) + ")\n")
fileOut.write("Greatest Decrease in Profits: " + str(finaldate2) + " ($" + str(finalmin) + ")\n")
fileOut.close()
