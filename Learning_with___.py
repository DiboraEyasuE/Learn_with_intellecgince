import pandas as pd
data = {
    'Name': ['Eyasu', 'Workinesh', 'Abe', 'Eshet'],
    'Age' : [70, 45, 33, 31],
    'City': ['Addis Ababa', 'Bahir Dar', 'Gondar', 'Mekele']
}
books_data = {
    'Title': ['The Great Gatsby', '1984', 'To Kill a Mockingbird', 'Pride and Prejudice'],
    'Author': ['F. Scott Fitzgerald', 'George Orwell', 'Harper Lee', 'Jane Austen'],
    'Year': [1925, 1949, 1960, 1813],
    'Pages': [218, 328, 281, 432]
}
beteseb = pd.DataFrame(data)
print(beteseb.shape)
print(beteseb.head(3))
print(beteseb.columns.to_list())
Metsaf = pd.DataFrame(books_data)
print(Metsaf.shape) 