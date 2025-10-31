import pandas as pd
data = {
    'Name': ['Eyasu', 'Workinesh', 'Abe', 'Eshet'],
    'Age' : [70, 45, 33, 31],
    'City': ['Addis Ababa', 'Bahir Dar', 'Gondar', 'Mekele']
}
beteseb = pd.DataFrame(data)
print(beteseb.shape)
print(beteseb.head)
print(beteseb.columns.to_lis)