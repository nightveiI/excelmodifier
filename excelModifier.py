import xlwings as xw
from datetime import date
import pandas as pd

xw.App(visible=False)
# = pd.read_csv (r'D:\test\DF_Standard_Project_Export.csv')
#read_file.to_excel (r'D:\test\DF_Standard_Project_Export.xlsx', index = None, header=True)

today = date.today()

# dd/mm/YY
# Month abbreviation, day and year	
# we use this variable to name our file and save at the end
d = today.strftime("%b_%d_%Y")
print("date =", d)

#df = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
#xw.view(df)
def lastRow(idx, workbook, col=1):
    """ Find the last row in the worksheet that contains data.

    idx: Specifies the worksheet to select. Starts counting from zero.

    workbook: Specifies the workbook

    col: The column in which to look for the last cell containing data.
    """

    ws = workbook.sheets[idx]

    lwr_r_cell = ws.cells.last_cell      # lower right cell
    lwr_row = lwr_r_cell.row             # row of the lower right cell
    lwr_cell = ws.range((lwr_row, col))  # change to your specified column

    if lwr_cell.value is None:
        lwr_cell = lwr_cell.end('up')    # go up untill you hit a non-empty cell

    return lwr_cell.row

# we declare what workbooks we are going to be using and what sheets we are going to be using
# in this case, we need a clean new workbook and opening the export from dataforma 
# the sheets we are going to be using are, from the new workbook: general, steep, and low slope
# and the dataforma export which is all jumbled together with the other columns we don't want for the current data analysis

file = r'C:\Users\jhagu\Downloads\DF_Standard_Project_Export(5).csv'
file.replace('.csv', '.xlsx')
newWB = xw.Book()
dfWB = xw.Book(file)


newWB.sheets[0].name = 'Steep Slope'
newWB.sheets.add(name='Low Slope')
newWB.sheets.add(name='Shingles')
newWB.sheets.add(name='Metal')
newWB.sheets.add(name='TPO')
newWB.sheets.add(name='Coatings')
newWB.sheets.add(name='General')
general = newWB.sheets['General']
lowSlope = newWB.sheets['Low Slope']
steepSlope = newWB.sheets['Steep Slope']

print("Creating new workbook")
indexes = ["Project ID", "Number Alt", "Project Name", "Building Name", "Building Address", "Building City", "Building State", "Building Zip", "Assigned To", "Type", "Subtype", "Status", "Status Date", "Who Created", "Date Created", "Modified", "Who Modified", "Bid Amount",  "Original Contract Amount", "Revised Contract Amount", "Outstanding Contract Amount", "Gross Profit Margin %", "Notes", "Actual Project Cost", "Actual Project Cost Who", "Actual Project Cost Date", "Source", "Budget Amount", "Budget Notes", "Budget Dates", "Contract With Object", "Contract With Name", "Contract With Office Name", "Salesperson Name",
           "Contract Terms", "Contract Term Notes", "Division", "Reference", "Subsource", "Client PO Number", "Local Union", "Construction Capacity", "Exclusions", "Special Instructions", "Contract Date", "Hide Daily Work Crew", "Running Notes", "Reference Notes", "Serial Number", "Production Status", "Contract Status", "Contract Status Date Open", "Contract Status Date Completed", "Contract Status Date Closed", "Contract Status Who Open", "Contract Status Who Completed", "Contract Status Who Closed", "Production Status Date", "Status Who", "Production Status Who", "Contact Name", "Contact Phone Number", "Contact Email"]



# we copy the original data forma into an array we will use later
generalArr =  dfWB.sheets[0].range((1, 1), (lastRow(0, dfWB), len(indexes))).value

print("Copying headers")

# we find where the last row of data is in the general sheet
totalDataRows = lastRow(0, dfWB)

#  indexes are as followed and dictate where in the original list data structure are the variables we want into our new workbook
# [0] is project id [1] is number alt [2] is project name [3] is type [4] is subtype [5] is production status [6] is production status date [7] is sales person name [8] is building name [9] is building address [10] is building city [11] is building state [12] is building zip [13] is orginal contract amount [14] is revised contract amount [15] is division
neededIndex = [0,1,2,9,10,49,57,33,3,4,5,6,7,18,19,36]

# we need to create a new array that will hold the data we want to export

print("grabbing data we want from dataforma")
modifiedGeneral = []
for i in range(0, totalDataRows):
    modifiedGeneral.append([])
    for j in range(0, len(neededIndex)):
        modifiedGeneral[i].append(generalArr[i][neededIndex[j]])


print("sorting by ascending order of production status")
# we bubble sort the array so that the data is in the correct order being from ascending production status date
for i in range(1, len(modifiedGeneral)):
    for j in range(1, len(modifiedGeneral)):
        if modifiedGeneral[i][6] < modifiedGeneral[j][6]:
            modifiedGeneral[i], modifiedGeneral[j] = modifiedGeneral[j], modifiedGeneral[i]


# we declare new arrays that will hold the data for the other sheets
steepSlopeArr= []
lowSlopeArr = []
shinglesArr = []
metalArr = []
tpoArr = []
coatingsArr = []


print("copying data into new workbook")
# we find the data that will be needed for the steep slope array and the low slope array
for i in range(0, len(modifiedGeneral)):
    if(i == 0):
        steepSlopeArr.append(modifiedGeneral[i])
        lowSlopeArr.append(modifiedGeneral[i])
        shinglesArr.append(modifiedGeneral[i])
        metalArr.append(modifiedGeneral[i])
        tpoArr.append(modifiedGeneral[i])
        coatingsArr.append(modifiedGeneral[i])
    elif(modifiedGeneral[i][3] == 'Steep Slope Roof Systems'):
        steepSlopeArr.append(modifiedGeneral[i])
    elif(modifiedGeneral[i][3] == 'Low Slope Roof Systems'):
        lowSlopeArr.append(modifiedGeneral[i])
    if(modifiedGeneral[i][4] != None):
        if(modifiedGeneral[i][4].find('Shingle') != -1):
            shinglesArr.append(modifiedGeneral[i])
        if(modifiedGeneral[i][4].find('Metal') != -1):
            metalArr.append(modifiedGeneral[i])
        if(modifiedGeneral[i][4].find('TPO') != -1):
            tpoArr.append(modifiedGeneral[i])
        if(modifiedGeneral[i][4].find('Coating') != -1):
            coatingsArr.append(modifiedGeneral[i])

        

#we move the array data into the sheets we created earlier
for i in range(0, len(steepSlopeArr)):
    steepSlope.range('A' + str(i+1)).value = steepSlopeArr[i]

for i in range(0, len(lowSlopeArr)):
    lowSlope.range('A' + str(i+1)).value = lowSlopeArr[i]

for i in range(0, len(modifiedGeneral)):
    general.range('A' + str(i+1)).value = modifiedGeneral[i]

for i in range(0, len(shinglesArr)):
    newWB.sheets['Shingles'].range('A' + str(i+1)).value = shinglesArr[i]

for i in range(0, len(metalArr)):
    newWB.sheets['Metal'].range('A' + str(i+1)).value = metalArr[i]

for i in range(0, len(tpoArr)):
    newWB.sheets['TPO'].range('A' + str(i+1)).value = tpoArr[i]

for i in range(0, len(coatingsArr)):
    newWB.sheets['Coatings'].range('A' + str(i+1)).value = coatingsArr[i]

for i in newWB.sheets:
    i.autofit(axis='columns')

print("done")
# we save the new workbook
newWB.save(r'D:\test\%s.xlsx' % d)
newWB.close()
dfWB.close()