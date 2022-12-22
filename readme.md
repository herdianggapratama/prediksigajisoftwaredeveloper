# Data Mining

Nama : [Herdiangga Pratama](https://github.com/herdianggapratama) <br/>
NIM : [H071211043](https://github.com/herdianggapratama) <br/>

## Aplikasi Prediksi Gaji per Tahun Software Developer 2022

Software Developer merupakan salah satu profesi programmer yang memiliki tugas untuk menciptakan suatu aplikasi sesuai dengan kebutuhan, menganalisis persyaratan software dan menentukan langkah perancangan software secara spesifik. Menjadi seorang Software Developer memerlukan pengetahuan coding, dan ketepatan dalam menilai kebutuhan sistem, memiliki ide pengembangan software, dan kemampuan dalam berkolaborasi dengan user, desainer, serta system analyst. Software Developer bekerja bersama desainer grafis, perwakilan pelanggan, manajer produk, manajer senior, dan pembuat keputusan. Oleh karena itu, gaji seorang software developer terbilang cukup tinggi. Dengan demikian penulis tertarik membuat suatu aplikasi prediksi gaji per tahun software developer tahun 2022 dengan data survey Stack Overflow 2022. <br />
[Data Survey Stack Overflow](https://insights.stackoverflow.com/survey)

### Cara Kerja Aplikasi

Dengan Data Cleaning & Modeling dataset Survey Stack Overflow 2022, kita dapat memprediksi gaji per tahun software developer berdasarkan informasi-informasi yang nantinya akan diinput. <br />
Adapun informasi-informasi yang dibutuhkan untuk memprediksi gaji per tahun software developer yaitu :

-   Negara
-   Tingkat Pendidikan
-   Pengalaman (Tahun)

### Data Cleaning

1. Import library dasar

```python
import pandas as pd
import numpy as np
```

2. Pengambilan dataframe dari dataset dan menampilkan 5 baris pertama pada data yang telah diambil

```python
df = pd.read_csv("survey_results_public.csv")
df.head()
```

3. Menampilkan dan mengganti nama kolom-kolom yang dibutuhkan dan yang akan ditampilkan

```python
df = df[["Country", "EdLevel", "YearsCodePro", "Employment", "ConvertedComp"]]
df = df.rename({"ConvertedComp": "Salary"}, axis=1)
df.head()
```

4. Menghilangkan datapoint salary bernilai kosong atau NaN

```python
df = df[df["Salary"].notnull()]
df.head()
```

5. Memperlihatkan informasi dari dataframe

```python
df.info()
```

Output:

```
<class 'pandas.core.frame.DataFrame'>
Int64Index: 34025 entries, 7 to 64154
Data columns (total 5 columns):
 #   Column        Non-Null Count  Dtype
---  ------        --------------  -----
 0   Country       34025 non-null  object
 1   EdLevel       34025 non-null  object
 2   YearsCodePro  34025 non-null  object
 3   Employment    34025 non-null  object
 4   Salary        34025 non-null  float64
dtypes: float64(1), object(4)
memory usage: 1.6+ MB
```

6. Menghapus datapoint yang bernilai kosong pada dataframe

```python
df = df.dropna()
```

7. Menghapus kolom Employment kecuali yang memiliki nilai datapoint "Employed full-time" karena tidak dibutuhkan untuk melakukan prediksi

```python
df = df[df["Employment"] == "Employed full-time"]
df = df.drop("Employment", axis=1)
```

8. Membuat function untuk membersihkan dan menyatukan datapoint negara yang memiliki nilai sedikit. (Indonesia termasuk negara yang memiliki nilai datapoint sedikit, tetapi saya tetap memasukkannya karena NKRI ttp di hati <3)

```python
def shorten_categories(categories, cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff or categories.index[i] == 'Indonesia':
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = 'Other'
    return categorical_map
```

Mengimplementasikan function ke dataframe country

```python
country_map = shorten_categories(df.Country.value_counts(), 400)
df['Country'] = df['Country'].map(country_map)
df.Country.value_counts()
```

Output:

```
Other                 8433
United States         7569
India                 2425
United Kingdom        2287
Germany               1903
Canada                1178
Brazil                 991
France                 972
Spain                  670
Australia              659
Netherlands            654
Poland                 566
Italy                  560
Russian Federation     522
Sweden                 514
Indonesia              116
Name: Country, dtype: int64
```

9. Pembersihan datapoint Experience

```python
df["YearsCodePro"].unique()
```

Output:

```python
   array(['13', '4', '2', '7', '20', '1', '3', '10', '12', '29', '6', '28',
          '8', '23', '15', '25', '9', '11', 'Less than 1 year', '5', '21',
          '16', '18', '14', '32', '19', '22', '38', '30', '26', '27', '17',
          '24', '34', '35', '33', '36', '40', '39', 'More than 50 years',
          '31', '37', '41', '45', '42', '44', '43', '50', '49'], dtype=object)
```

Membersihkan datapoint YearsCodePro (Experience)

```python
def clean_experience(x):
    if x ==  'More than 50 years':
        return 50
    if x == 'Less than 1 year':
        return 0.5
    return float(x)

df['YearsCodePro'] = df['YearsCodePro'].apply(clean_experience)
```

10. Pembersihan datapoint Education Level

```python
df["EdLevel"].unique()
```

Output:

```
array(['Bachelor’s degree (B.A., B.S., B.Eng., etc.)',
       'Master’s degree (M.A., M.S., M.Eng., MBA, etc.)',
       'Some college/university study without earning a degree',
       'Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)',
       'Associate degree (A.A., A.S., etc.)',
       'Professional degree (JD, MD, etc.)',
       'Other doctoral degree (Ph.D., Ed.D., etc.)',
       'I never completed any formal education',
       'Primary/elementary school'], dtype=object)
```

Membersihkan datapoint EdLevel (Education Level)

```python
def clean_education(x):
    if 'Bachelor’s degree' in x:
        return 'S1'
    if 'Master’s degree' in x:
        return 'S2'
    if 'Professional degree' in x or 'Other doctoral' in x:
        return 'S3'
    return 'Bukan Sarjana'

df['EdLevel'] = df['EdLevel'].apply(clean_education)
```

11. Datapoint Experience memiliki nilai dengan datatype float sedangkan datapoint Education Level dan Country memiliki nilai dengan datatype string. Maka dari itu kita perlu menyamakan datatypenya dengan menggunakan library LabelEncoder

```python
from sklearn.preprocessing import LabelEncoder
```

Education Level

```python
le_education = LabelEncoder()
df['EdLevel'] = le_education.fit_transform(df['EdLevel'])
df["EdLevel"].unique()
```

Country

```python
le_country = LabelEncoder()
df['Country'] = le_country.fit_transform(df['Country'])
df["Country"].unique()
```
