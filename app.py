import streamlit as st
import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from currency_converter import CurrencyConverter

# Prediksi
cc = CurrencyConverter()
def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

regressor = data["model"]
le_country = data["le_country"]
le_education = data["le_education"]

# Eksplor
def shorten_categories(categories, cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff or categories.index[i] == 'Indonesia':
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = 'Other'
    return categorical_map


def clean_experience(x):
    if x ==  'More than 50 years':
        return 50
    if x == 'Less than 1 year':
        return 0.5
    return float(x)


def clean_education(x):
    if 'Bachelor’s degree' in x:
        return 'S1'
    if 'Master’s degree' in x:
        return 'S2'
    if 'Professional degree' in x or 'Other doctoral' in x:
        return 'S3'
    return 'Bukan Sarjana'


@st.cache
def load_data():
    df = pd.read_csv("survey_results_public.csv")
    df = df[["Country", "EdLevel", "YearsCodePro", "Employment", "ConvertedComp"]]
    df = df[df["ConvertedComp"].notnull()]
    df = df.dropna()
    df = df[df["Employment"] == "Employed full-time"]
    df = df.drop("Employment", axis=1)

    country_map = shorten_categories(df.Country.value_counts(), 400)
    df["Country"] = df["Country"].map(country_map)
    df = df[df["ConvertedComp"] <= 250000]
    df = df[df["ConvertedComp"] >= 10000]
    df = df[df["Country"] != "Other"]

    df["YearsCodePro"] = df["YearsCodePro"].apply(clean_experience)
    df["EdLevel"] = df["EdLevel"].apply(clean_education)
    df = df.rename({"ConvertedComp": "Salary"}, axis=1)
    return df

df = load_data()

page = st.sidebar.selectbox("Eksplor atau Prediksi", ("Prediksi", "Eksplore Data"))

if page == "Prediksi":
    st.title("Prediksi Gaji per Tahun Software Developer 2022")

    countries = (
        "United States",
        "India",
        "United Kingdom",
        "Germany",
        "Canada",
        "Brazil",
        "France",
        "Spain",
        "Australia",
        "Netherlands",
        "Poland",
        "Italy",
        "Russian Federation",
        "Sweden",
        "Indonesia"
    )

    education = (
        "Bukan Sarjana",
        "S1",
        "S2",
        "S3",
    )

    country = st.selectbox("Negara", countries)
    education = st.selectbox("Tingkat Pendidikan", education)

    expericence = st.slider("Pengalaman (Tahun)", 0, 50, 3)

    ok = st.button("Prediksi Gaji")
    if ok:
        X = np.array([[country, education, expericence ]])
        X[:, 0] = le_country.transform(X[:,0])
        X[:, 1] = le_education.transform(X[:,1])
        X = X.astype(float)

        salary = regressor.predict(X)
        st.subheader(f"Diperkirakan gaji per tahunnya sekitar USD {salary[0]:.2f} atau IDR {cc.convert(salary, 'USD', 'IDR'):.2f}")

else:
    st.title("Eksplor Gaji per Tahun Software Developer 2022")

    data = df["Country"].value_counts()

    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels=data.index, autopct="%1.1f%%", shadow=True, startangle=90)
    ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.write("""#### Data dari negara-negara yang berbeda""")

    st.pyplot(fig1)
    
    st.write(
        """
    #### Rata-rata Gaji berdasarkan Negara
    """
    )

    data = df.groupby(["Country"])["Salary"].mean().sort_values(ascending=True)
    st.bar_chart(data)

    st.write(
        """
    #### Rata-rata Gaji berdasarkan Pengalaman (Tahun)
    """
    )

    data = df.groupby(["YearsCodePro"])["Salary"].mean().sort_values(ascending=True)
    st.line_chart(data)


