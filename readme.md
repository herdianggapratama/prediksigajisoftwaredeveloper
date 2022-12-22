# Data Mining

Nama : [Herdiangga Pratama](https://github.com/herdianggapratama) <br/>
NIM : [H071211043](https://github.com/herdianggapratama) <br/>

## Aplikasi Prediksi Gaji per Tahun Software Developer 2022

Software Developer merupakan salah satu profesi programmer yang memiliki tugas untuk menciptakan suatu aplikasi sesuai dengan kebutuhan, menganalisis persyaratan software dan menentukan langkah perancangan software secara spesifik. Menjadi seorang Software Developer memerlukan pengetahuan coding, dan ketepatan dalam menilai kebutuhan sistem, memiliki ide pengembangan software, dan kemampuan dalam berkolaborasi dengan user, desainer, serta system analyst. Software Developer bekerja bersama desainer grafis, perwakilan pelanggan, manajer produk, manajer senior, dan pembuat keputusan. Oleh karena itu, gaji seorang software developer terbilang cukup tinggi. Dengan demikian penulis tertarik membuat suatu aplikasi prediksi gaji per tahun software developer tahun 2022 dengan data survey Stack Overflow 2022. <br />
[Data Survey Stack Overflow](https://insights.stackoverflow.com/survey)

### Data Cleaning

Import library dasar

```python
import pandas as pd
import numpy as np
```

Pengambilan dataframe dari dataset dan menampilkan 5 baris pertama pada data yang telah diambil

```python
df = pd.read_csv("survey_results_public.csv")
df.head()
```

Output :

```
	Respondent	MainBranch	Hobbyist	Age	Age1stCode	CompFreq	CompTotal	ConvertedComp	Country	CurrencyDesc	...	SurveyEase	SurveyLength	Trans	UndergradMajor	WebframeDesireNextYear	WebframeWorkedWith	WelcomeChange	WorkWeekHrs	YearsCode	YearsCodePro
0	1	I am a developer by profession	Yes	NaN	13	Monthly	NaN	NaN	Germany	European Euro	...	Neither easy nor difficult	Appropriate in length	No	Computer science, computer engineering, or sof...	ASP.NET Core	ASP.NET;ASP.NET Core	Just as welcome now as I felt last year	50.0	36	27
1	2	I am a developer by profession	No	NaN	19	NaN	NaN	NaN	United Kingdom	Pound sterling	...	NaN	NaN	NaN	Computer science, computer engineering, or sof...	NaN	NaN	Somewhat more welcome now than last year	NaN	7	4
2	3	I code primarily as a hobby	Yes	NaN	15	NaN	NaN	NaN	Russian Federation	NaN	...	Neither easy nor difficult	Appropriate in length	NaN	NaN	NaN	NaN	Somewhat more welcome now than last year	NaN	4	NaN
3	4	I am a developer by profession	Yes	25.0	18	NaN	NaN	NaN	Albania	Albanian lek	...	NaN	NaN	No	Computer science, computer engineering, or sof...	NaN	NaN	Somewhat less welcome now than last year	40.0	7	4
4	5	I used to be a developer by profession, but no...	Yes	31.0	16	NaN	NaN	NaN	United States	NaN	...	Easy	Too short	No	Computer science, computer engineering, or sof...	Django;Ruby on Rails	Ruby on Rails	Just as welcome now as I felt last year	NaN	15	8
```

Menampilkan dan mengganti nama kolom-kolom yang dibutuhkan dan akan ditampilkan

```python
df = df[["Country", "EdLevel", "YearsCodePro", "Employment", "ConvertedComp"]]
df = df.rename({"ConvertedComp": "Salary"}, axis=1)
df.head()
```

Output :

```
Country	EdLevel	YearsCodePro	Employment	Salary
0	Germany	Master’s degree (M.A., M.S., M.Eng., MBA, etc.)	27	Independent contractor, freelancer, or self-em...	NaN
1	United Kingdom	Bachelor’s degree (B.A., B.S., B.Eng., etc.)	4	Employed full-time	NaN
2	Russian Federation	NaN	NaN	NaN	NaN
3	Albania	Master’s degree (M.A., M.S., M.Eng., MBA, etc.)	4	NaN	NaN
4	United States	Bachelor’s degree (B.A., B.S., B.Eng., etc.)	8	Employed full-time	NaN
```
