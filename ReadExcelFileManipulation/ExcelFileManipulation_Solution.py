# Import Pandas and xlrd package as pre-requisite to open and read excel file
import pandas as pd


def break_points(df):
    nan_indexs = []
    for i in range(0, df.shape[0]):
        row = list(set(list(df.iloc[i].isna())))

        if len(row) == 1 and row[0] == True:
            nan_indexs.append(i)

    return nan_indexs


# Read the excel file and get the specific cell value
def cricket_summary(file_name, sheet, first_file=True):
    df = pd.read_excel(io=file_name, sheet_name=sheet)

    nan_index = break_points(df)

    first_bat = df.iloc[:nan_index[0], 1:8]

    first_bowl = df.iloc[nan_index[0] + 1: nan_index[1], :]

    first_bowl.columns = list(first_bowl.iloc[0])
    first_bowl = first_bowl.iloc[1:, :]

    second_bat = df.iloc[nan_index[2] + 1: nan_index[3], 1:8]

    second_bowl = df.iloc[nan_index[3] + 1:, :]
    second_bowl.columns = list(second_bowl.iloc[0])
    second_bowl = second_bowl.iloc[1:, :]

    # calculate runs and runs based on overs

    first_inn_runs = first_bat['R'].sum()
    second_inn_runs = second_bat['R'].sum()

    batting = pd.concat([first_bat, second_bat])

    bowling = pd.concat([first_bowl, second_bowl])

    if first_file:
        if first_inn_runs > second_inn_runs:
            print("England has Won!")
        else:
            print("India has Won!")
    else:
        if second_inn_runs > first_inn_runs:
            print("England has Won!")
        else:
            print("India has Won!")

    # output the values

    print("Scored Highest Runs : ", ", ".join(batting['BATSMEN'][batting['R'] == max(batting['R'])].values))

    print("Maximum Wickets by : ", ", ".join(bowling['BOWLING'][bowling['W'] == max(bowling['W'])].values))

    print("Scored Maximum 6’s : ", ", ".join(batting['BATSMEN'][batting['6S'] == max(batting['6S'])].values))
    print("Scored maximum 4's : ", ", ".join(batting['BATSMEN'][batting['4S'] == max(batting['4S'])].values))


print("I file")
"""
Provide the foldername which has the file location, sample: C:\Mankay\AIML\T20-Cricket-First.xlsx
"""
cricket_summary('T20-Cricket-First.xlsx', 'First T-20')
print("\nII file")
cricket_summary('T20-Cricket-Second.xlsx', 'Second T-20', first_file=False)
