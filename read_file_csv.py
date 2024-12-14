import pandas as pd

# URL raw file CSV di GitHub
url = 'https://github.com/mhdalfarisy/Assignment-dibimbing-belajar-github-/blob/main/Example_profil.csv'

# Membaca file CSV dari URL
df = pd.read_csv(url)

# Menampilkan data
print(df.head())
