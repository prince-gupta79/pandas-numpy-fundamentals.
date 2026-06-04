pandas-numpy-fundamentals :
Learning pandas and numpy from scratch — this folder covers everything from the basics to actual data cleaning on real datasets like the Titanic CSV.
Started here before building anything serious with data. You can't do ML without knowing this stuff cold.

What's covered
pandas :

- Series and DataFrames from scratch
- Importing CSV and JSON files
- Selecting, filtering, and sorting data
- GroupBy and aggregate functions
- Data cleaning — handling missing values, duplicates, incorrect data
- String operations and column splitting
- Encoding categorical data with get_dummies
- Working with real datasets (Titanic, sampled sales data, car data)

numpy:

- Arrays — 1D, 2D, 3D
- Arithmetic and scalar operations
- Broadcasting
- Slicing and filtering
- Aggregate functions (sum, mean, std, var, min, max, argmin, argmax)
- Random number generation
- Vectorized functions
S- aving and loading arrays (.npy and .npz files)
- Itrating over arrays


## Folder structure

```
pandas-numpy-fundamentals/
│
├── getting_started/
│   ├── Data_Frames.py          # Creating and modifying DataFrames
│   ├── series.py               # pandas Series basics
│   ├── dic.py                  # Series from dictionary
│   ├── filtering.py            # Filtering rows by condition
│   ├── selection.py            # Selecting columns
│   ├── sorting.py              # Sorting by values
│   ├── groupby.py              # GroupBy operations
│   ├── aggregate_fun.py        # Aggregate functions reference
│   ├── data_cleaning.py        # Data cleaning workflow
│   ├── importing.py            # Full cleaning pipeline on real data
│   ├── json.txt                # Sample car dataset in JSON
│   └── sampled.csv             # Sample dataset
│
├── advanced_pandas/
│   ├── advanced_features.py    # Multi-column sorting
│   └── tested.csv              # Titanic dataset
│
├── EDA/
│   ├── duplicate_rev.py        # Finding and removing duplicates
│   ├── encoding.py             # Categorical encoding with get_dummies
│   └── general_terms.py        # Common EDA operations reference
│
└── num_pro/
    ├── array.py                # Basic array operations
    ├── arithmetic.py           # Scalar arithmetic
    ├── broadcasting.py         # Broadcasting explained
    ├── slicing.py              # Array slicing
    ├── filtering.py            # Boolean filtering
    ├── aggregate_fun.py        # Aggregate functions with axis
    ├── multi_array.py          # 3D arrays
    ├── numpy_fun.py            # zeros, empty, arange
    ├── randoms_num.py          # Random number generation
    ├── vectorized_fun.py       # Vectorized operations
    ├── suffle.py               # Shuffle and random choice
    ├── save_num.py             # Saving arrays to .npy
    ├── save_multiple.py        # Saving multiple arrays to .npz
    └── load_num.py             # Loading saved arrays
```

Stack
Python, pandas, numpy

Setup
bashgit clone https://github.com/prince-gupta79/pandas-numpy-fundamentals.git
cd pandas-numpy-fundamentals
pip install pandas numpy

Why I built this
pandas and numpy are the foundation of everything in data science and ML. Before building models or visualizations, you need to be able to manipulate data confidently. This folder is where I built that foundation.
Most of the data cleaning techniques here came from working with messy real-world datasets — the Titanic CSV, car performance data, sales records. That's where you actually learn it.

Built in Nepal. Part of a self-directed journey into ML and data science.
