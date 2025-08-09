# Indian-Startup-Funding-Analysis
This project analyzes and visualizes startup funding data from a CSV file (`startup_funding.csv`).
It uses **Pandas**, **Matplotlib**, and **Seaborn** to create insights such as funding trends, top sectors, leading startups, and most active investors.

## 📂 Project Structure

```
.
├── main.py               # Main Python script for analysis and visualization
├── startup_funding.csv   # Dataset containing startup funding details
└── README.md             # Project documentation
```

## 📊 Features

* **Funding Trends Over Time** – Line plot of total funding per year/month.
* **Top 5 Sectors** – Bar chart of the most common startup sectors.
* **Top 5 Startups** – Bar chart of startups with the most funding events.
* **Top 5 Investors** – Bar chart of the most active investors.
* **Investment Type Distribution** – Count of different investment types.

## 🛠 Requirements

Make sure you have Python 3.x installed and install the dependencies:

```bash
pip install pandas matplotlib seaborn
```

## ▶️ How to Run

1. Place `startup_funding.csv` in the same directory as `main.py`.
2. Open a terminal in the project directory.
3. Run:

```bash
python main.py
```

## 📈 Output

* Several plots will be displayed showing trends and rankings.
* Summary statistics for investment types will be printed in the console.
