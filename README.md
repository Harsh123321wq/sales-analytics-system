# Sales Analytics System

This project is a Python-based **Sales Data Analytics System** that reads messy sales data, cleans and validates it, integrates external API data, performs detailed analysis, and generates professional reports for business decision-making.

---

## 📁 Project Structure

```
sales-analytics-system/
│
├── data/
│   ├── sales_data.txt
│   └── enriched_sales_data.txt
│
├── output/
│   └── sales_report.txt
│
├── utils/
│   ├── file_handler.py
│   ├── data_processor.py
│   └── api_handler.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 🧠 Features Implemented

* Handles non-UTF-8 encoded files safely
* Cleans and validates messy sales data
* Performs sales analysis (revenue, regions, products, customers, dates)
* Integrates product data using DummyJSON API
* Enriches and saves sales data
* Generates a comprehensive text report

---

## ⚙️ Requirements

* Python 3.x
* requests library

Install dependencies using:

```
pip install -r requirements.txt
```

---

## ▶️ How to Run the Project

1. Clone the repository:

```
git clone https://github.com/your-username/sales-analytics-system
```

2. Navigate to the project folder:

```
cd sales-analytics-system
```

3. Run the main program:

```
python main.py
```

---

## 📄 Output Files Generated

* `data/enriched_sales_data.txt` → Sales data enriched with API details
* `output/sales_report.txt` → Final analytics report with all sections

These files are **generated automatically** when the program runs.

---

## 📝 Notes

* No hardcoded file paths are used
* Proper error handling is implemented
* The project follows the given assignment structure and marking scheme

---

## 👤 Author

**Rishi**
Class 8 – Python Assignment

---

## ✅ Submission Instructions

* Ensure the repository is **public**
* Repository name must be: **sales-analytics-system**
* Submit **only the root GitHub repository link**
