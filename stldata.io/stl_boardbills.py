import pandas as pd

boardbill_df = pd.read_csv(
    r'C:\Users\\legis\Documents\BoardBill.csv', encoding='iso-8859-1')


#Remove digits from BB data
boardbill_df['Board Bill'] = boardbill_df['Board Bill'].str.replace(
    pat=r'\D', repl='', regex=True).astype(int)

#Sort data after bb has been turned into int, will sort correctly
boardbill_df = boardbill_df.sort_values(
    ['Session', 'Board Bill'], ascending=[True, True])

#Analysis 1: Which wards have had the most ordinances come from it?
#Visualization ideas - ward map over time
analysis_1_df = boardbill_df[['Session','Ward','Ordinance']].copy()
analysis_1_df['Passed'] = boardbill_df['Ordinance'].divide(boardbill_df['Ordinance'])
analysis_1_df['Passed'][analysis_1_df['Passed'] != 1.0] = 0
analysis_1_df.pop('Ordinance')
analysis_1_df.groupby(['Session','Ward']).sum()

print(analysis_1_df)



