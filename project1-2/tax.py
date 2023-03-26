import pandas as pd

tax_table = None

def load_tax_table(path):
    global tax_table
    tax_table = pd.read_csv(path, thousands=',')
    tax_table.replace('-',0,inplace=True)
    tax_table.astype('int64',copy=False)