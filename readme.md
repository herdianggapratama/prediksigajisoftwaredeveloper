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

4. Menghilangkan baris dari kolom salary bernilai kosong atau NaN

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

6. Menghapus baris yang bernilai kosong pada dataframe

```python
df = df.dropna()
```

