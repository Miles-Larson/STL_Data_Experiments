import pandas as pd

boardbill_df = pd.read_csv(
    r'C:\Users\\legis\Documents\BoardBill.csv', encoding='iso-8859-1')



#Assumptions, Ward is populated and with President info
#Function edits the dataframe in place
def clean_bb_data(df:pd.DataFrame) -> None:
    df['President Proposal'] = boardbill_df['Ward'] == 'President'
    df['Passed'] = boardbill_df['Ordinance'] != 0
    #Remove digits from BB data
    temp = df['Board Bill'].str.replace(pat=r'\D', repl='', regex=True)
    temp = pd.to_numeric(temp)
    df['Board Bill'].update(temp)
    #Remove digits from Ward
    temp = df['Ward'].str.replace(pat=r'\D', repl='', regex=True).astype(str)
    
    df.update(temp)
    return None

class data_analysis():

    def __init__(self,df:pd.DataFrame) -> None:
        """This class is designed to take a dataframe and return answers to analytical questions regarding Board Bill data.

    Expectations include a column for 'Passed', 'Board Bill', 'President Proposal', and 'Ward'
    """
        self.df = df.copy()
        self.number_of_bills = len(df)
        self.number_of_bills_passed = len(df['Passed']==True)
        self.number_of_bills_not_passed = len(df['Passed']==False)

        self.bills_passed_df = self.df.get(df['Passed']==True)
        self.bills_per_ward_df = self.df[['Session','Ward','Passed','Board Bill']].groupby(['Passed','Ward','Session'],0).count().reset_index().copy()
        self.bills_per_alderman_df = self.df[['Session','Alderman','Passed','Board Bill']].groupby(['Passed','Alderman','Session'],0).count().reset_index().copy()
        self._groupby_example = self.df[['Passed', 'Board Bill']].groupby(['Passed']).count().copy().at[False,'Board Bill']
        self._2015_bb_passed = self.bills_per_ward_df.query('Passed == True & Session == "2015-2016"').get(['Ward','Board Bill']).copy()
        #self._2015_bb_passed_chart = self._2015_bb_passed.plot(x='Ward', y='Board Bill',kind='Bar')
        
        print('Data Analysis Complete')

class presentation():
    def __init__(self) -> None: #todo
        pass
    
clean_bb_data(boardbill_df)
bb_data_analysis = data_analysis(boardbill_df)