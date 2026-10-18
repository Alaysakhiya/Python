<div align="center">

# 📚 E-LIBRARY DATA INSIGHTS DASHBOARD

### ⭐ A Python CLI tool to load, analyze, filter, and visualize library borrowing data from CSV files ⭐

<br>

<table align="center">
  <tr>
    <td align="center" width="170">
      <img src="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg" height="70" alt="Python logo"><br>
      <b>Python 3.8+</b>
    </td>
    <td align="center" width="170">
      <img src="https://raw.githubusercontent.com/numpy/numpy/623bc1fae1d47df24e7f1e29321d0c0ba2771ce0/branding/logo/primary/numpylogo.svg" height="70" alt="NumPy logo"><br>
      <b>NumPy</b>
    </td>
    <td align="center" width="170">
      <img src="https://pandas.pydata.org/static/img/pandas.svg" height="70" alt="pandas logo"><br>
      <b>pandas</b>
    </td>
    <td align="center" width="170">
      <img src="https://upload.wikimedia.org/wikipedia/commons/8/84/Matplotlib_icon.svg" height="70" alt="matplotlib logo"><br>
      <b>matplotlib</b>
    </td>
    <td align="center" width="170">
      <img src="https://raw.githubusercontent.com/mwaskom/seaborn/master/doc/_static/logo-wide-lightbg.svg" height="70" alt="seaborn logo"><br>
      <b>seaborn</b>
    </td>
  </tr>
</table>

</div>

---

> ## 🎯 **Main Topic: Data Analysis & Visualization of Library Transactions**
>
> A **menu-driven, command-line** Python program that lets you **load → calculate → filter → report → visualize** library borrowing data from a CSV file. Built with **NumPy**, **pandas**, **matplotlib**, and **seaborn**.

---

## ✨ Features

- **Load Dataset**: Load `library_transaction.csv` into a pandas DataFrame
- **Calculate Statistics**: Most borrowed book, average borrow time, and busiest day
- **Filter Transactions**: Filter by genre (case-insensitive) or by borrowing duration (less than / greater than)
- **Summary Report**: Maximum, standard deviation, median, total borrowing time, genre summary, and borrow count per book
- **Data Visualization**: Create Bar, Line, Pie, and Heatmap charts

---


## 📁 Dataset Format

The program expects a file named `library_transaction.csv` in the same folder as the script, with these columns:

| Column                      | Description                          |
|-----------------------------|--------------------------------------|
| `Book Title`                | Title of the borrowed book           |
| `Genre`                     | Genre of the book                    |
| `Borrowing Duration (Days)` | Number of days borrowed (numeric)    |
| `Date`                      | Date of the transaction              |



---

## 🧭 Menu Guide

### 1. Load Dataset
Reads the CSV file into a pandas DataFrame. You must do this first. All other options require a loaded dataset.

### 2. Calculate Statistics
- Most borrowed book
- Average borrow time
- Busiest day

<div align="center">

**📸 Example: Average Borrow Time**

<img src="screenshots/calculate_statistics.png" alt="Calculate Statistics menu showing Average Borrow Time of 15.53" width="420">

</div>

### 3. Filter
- **By genre**: enter a genre name (not case-sensitive)
- **By borrowing duration**: enter a number of days, then choose less than (`<`) or greater than (`>`)

### 4. Summary Report
- **Borrowing statistics**: maximum, standard deviation, median, or total borrowing time
- **Group by genre**: total borrowings, average time, and total days per genre
- **Total borrowing by book**: how many times each book was borrowed

<div align="center">

**📸 Example: Standard Deviation of Borrowing Time**

<img src="screenshots/summary_report.png" alt="Generate Report menu showing Standard Deviation of 8.557984575821576" width="420">

</div>

### 5. Data Visualization

| Chart      | What it shows                                       |
|------------|-----------------------------------------------------|
| Bar Chart  | Top 5 most borrowed books                           |
| Line Chart | Average borrowing duration by month                 |
| Pie Chart  | Share of transactions by genre                      |
| Heatmap    | Transactions by genre and borrowing duration        |

Charts open in a separate window. Close the window to return to the menu.

### 6. Exit
Quits the program.

---

## 💡 Example Workflow

```
1. Load Dataset            →  library_transaction.csv
2. Calculate Statistics    →  Most Borrowed Book
3. Filter                  →  Genre: Fiction
4. Summary Report          →  Group by Genre
5. Data Visualization      →  Pie Chart
6. Exit
```

---

## 🖼️ Screenshots

| Calculate Statistics | Summary Report |
|:--------------------:|:--------------:|
| <img src="screenshots/calculate_statistics.png" alt="Calculate Statistics" width="360"> | <img src="screenshots/summary_report.png" alt="Summary Report" width="360"> |
| Average borrow time = **15.53** days | Standard deviation = **8.558** days |

---

## 🧯 Error Handling

The program handles common input problems without crashing:

- Non-numeric menu input → *"Enter Valid Value !"*
- Wrong file name or path → *"File Not Found Enter Valid File Name"*
- Menu number out of range → *"Invalid Choice !"*
- Using features before loading data → *"Please Load Dataset First !!"*

---

## 📂 Project Structure

```
.
├── library_dashboard.py       # Main program (rename to match your file)
├── library_transaction.csv    # Input dataset
├── screenshots/
│   ├── calculate_statistics.png
│   └── summary_report.png
└── README.md
```

---

## 🔮 Possible Improvements

- Support for more chart types (box plot, scatter plot)
- Let users choose the CSV file path at runtime
- Export filtered results and reports to a new CSV
- Add a date-range filter

---

## 📄 License

This project is open source. Add your preferred license here (e.g., MIT).