import pandas as pd

def load_thoughts():
    col_list = ["episode","character","thought"]
    df = pd.read_csv("thoughts.csv",  header=None, names=col_list)
    return df


thoughts = load_thoughts()
print(thoughts)

indexNames = thoughts[(thoughts['character'] != 'Mark') & (thoughts['character'] != 'Jez') & (thoughts['character'] != 'Jeremy')].index
thoughts.drop(indexNames,inplace=True)
print(thoughts)


thoughts.to_csv('thoughtsu.csv',index=False,header=False)
