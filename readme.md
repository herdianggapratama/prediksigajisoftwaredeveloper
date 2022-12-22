# Data Mining

Nama : [Herdiangga Pratama](https://github.com/herdianggapratama) <br/>
NIM : [H071211043](https://github.com/herdianggapratama) <br/>

## Aplikasi Prediksi Gaji per Tahun Software Developer 2022

Software Developer merupakan salah satu profesi programmer yang memiliki tugas untuk menciptakan suatu aplikasi sesuai dengan kebutuhan, menganalisis persyaratan software dan menentukan langkah perancangan software secara spesifik. Menjadi seorang Software Developer memerlukan pengetahuan coding, dan ketepatan dalam menilai kebutuhan sistem, memiliki ide pengembangan software, dan kemampuan dalam berkolaborasi dengan user, desainer, serta system analyst. Software Developer bekerja bersama desainer grafis, perwakilan pelanggan, manajer produk, manajer senior, dan pembuat keputusan. Oleh karena itu, gaji seorang software developer terbilang cukup tinggi. Dengan demikian penulis tertarik membuat suatu aplikasi prediksi gaji per tahun software developer tahun 2022 dengan data survey Stack Overflow 2022. <br />
[Data Survey Stack Overflow](https://insights.stackoverflow.com/survey)

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
