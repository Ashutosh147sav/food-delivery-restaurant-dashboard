# Food Delivery Restaurant Analytics and Recommendation Dashboard

A Python-based data analytics and interactive dashboard project using **Pandas, NumPy, Matplotlib, Seaborn, Plotly, and Dash**.

---

## 📌 Project Overview

The **Food Delivery Restaurant Analytics and Recommendation Dashboard** is a data analytics project that analyzes restaurant data from the Zomato dataset.

The project uses Python libraries such as **Pandas, NumPy, Matplotlib, Seaborn, Plotly, and Plotly Dash** to clean the dataset, perform Exploratory Data Analysis (EDA), generate visualizations, and develop an interactive dashboard.

The dashboard helps users compare restaurants based on:

* Restaurant ratings
* Number of customer votes
* Approximate cost for two people
* Restaurant type
* Online ordering availability
* Table booking availability
* Value for money

---

## 🎯 Problem Statement

Restaurant datasets contain useful information such as customer ratings, votes, approximate cost, restaurant type, online ordering, and table-booking facilities. However, analyzing raw data directly can make it difficult to identify useful patterns and trends.

The objective of this project is to:

* Clean and preprocess restaurant data.
* Perform Exploratory Data Analysis (EDA).
* Analyze restaurant ratings and popularity.
* Study the relationship between restaurant rating and approximate cost.
* Compare restaurants based on online ordering and table-booking facilities.
* Identify relatively good value-for-money restaurants.
* Present the analysis through an interactive Plotly Dash dashboard.

---

## 📊 Dataset

The project uses the **Zomato Dataset** available on Kaggle.

**Dataset Source:** Kaggle
**Dataset:** Zomato Dataset
**Dataset Size Used:** 148 rows × 7 columns

### Dataset Columns

| Column                        | Description                          |
| ----------------------------- | ------------------------------------ |
| `name`                        | Restaurant name                      |
| `online_order`                | Whether online ordering is available |
| `book_table`                  | Whether table booking is available   |
| `rate`                        | Restaurant rating                    |
| `votes`                       | Number of customer votes             |
| `approx_cost(for two people)` | Approximate cost for two people      |
| `listed_in(type)`             | Restaurant type/category             |

> **Note:** The dataset used in this project does not contain cuisine or locality/location columns. Therefore, the analysis does not include cuisine or location-based analysis.

---

## 🛠️ Technology Stack

### Programming Language

* Python

### Python Libraries

* **Pandas** — Data loading, cleaning and data analysis
* **NumPy** — Numerical operations
* **Matplotlib** — Data visualization
* **Seaborn** — Statistical visualization
* **Plotly** — Interactive visualizations
* **Dash** — Interactive web dashboard

### Development and Deployment Tools

* Jupyter Notebook
* GitHub
* Render
* Gunicorn
* AI-assisted development using ChatGPT

---

## 🔄 Project Workflow

```text
Dataset
   ↓
Data Loading
   ↓
Data Cleaning & Preprocessing
   ↓
Exploratory Data Analysis
   ↓
Data Visualization
   ↓
Interactive Dash Dashboard
   ↓
GitHub Repository
   ↓
Render Deployment
```

---

## 🧹 Data Cleaning and Preprocessing

The following preprocessing steps were performed on the dataset:

1. Loaded the Zomato dataset using Pandas.
2. Checked the dataset shape and column names.
3. Checked data types using `info()`.
4. Checked missing values.
5. Removed `/5` from restaurant rating values.
6. Converted the rating column into numeric format.
7. Converted approximate cost into numeric format.
8. Checked duplicate records.
9. Handled missing values required for analysis.
10. Created a value-for-money score for comparison.

### Rating Cleaning

The original rating values contained `/5`, for example:

```text
4.4/5
3.8/5
4.1/5
```

The `/5` part was removed and the values were converted into numeric form.

### Value-for-Money Score

A simple score was created to compare restaurant rating with approximate cost.

```text
Value Score = (Restaurant Rating / Approximate Cost for Two) × 1000
```

A higher value score indicates a relatively better rating compared with the approximate cost.

---

## 📈 Exploratory Data Analysis

The project performs different types of Exploratory Data Analysis.

### Univariate Analysis

* Distribution of restaurant ratings
* Restaurant type distribution
* Online ordering availability
* Table booking availability

### Bivariate Analysis

* Rating vs approximate cost
* Restaurant popularity based on votes
* Average rating by restaurant type

### Multivariate Analysis

* Relationship between rating, votes and approximate cost
* Correlation analysis between numerical variables
* Scatter plot using rating, cost and votes

---

## 📊 Data Visualizations

The project includes the following visualizations:

### 1. Restaurant Rating Distribution

A histogram is used to understand the distribution of restaurant ratings.

### 2. Top Restaurants by Votes

A bar chart is used to identify restaurants with a high number of customer votes.

### 3. Rating vs Approximate Cost

A scatter plot is used to study the relationship between restaurant rating and approximate cost for two people.

### 4. Correlation Heatmap

A heatmap is used to analyze the correlation between:

* Rating
* Votes
* Approximate cost

### 5. Rating Boxplot

A boxplot is used to understand the distribution, spread and possible outliers in restaurant ratings.

### 6. Average Rating by Restaurant Type

A line chart is used to compare the average rating of different restaurant types.

### 7. Top-Rated Restaurants

A bar chart is used to identify restaurants with high ratings.

### 8. Value-for-Money Restaurants

A bar chart is used to identify restaurants with relatively high value scores.

### 9. Online Order Analysis

Restaurants are compared based on online-order availability and average rating.

### 10. Table Booking Analysis

Restaurants are compared based on table-booking availability and average rating.

---

## 🖥️ Interactive Dashboard

The project includes an interactive **Plotly Dash** dashboard for restaurant analysis.

### Dashboard Features

* 📌 KPI cards
* 📊 Interactive charts
* 🔽 Restaurant type filter
* ⭐ Average rating analysis
* 👍 Popularity based on votes
* 💰 Rating vs cost analysis
* 🍽️ Restaurant type distribution
* 🛵 Online ordering analysis
* 🪑 Table booking analysis
* 💵 Value-for-money analysis

### Dashboard Charts

The dashboard contains seven major interactive charts:

1. Top 10 Restaurants by Rating
2. Top 10 Restaurants by Votes
3. Rating vs Approximate Cost
4. Restaurant Type Distribution
5. Online Order Analysis
6. Table Booking Analysis
7. Top 10 Value-for-Money Restaurants

The dashboard also uses a **Dash callback** so that the displayed KPIs and charts can update according to the selected restaurant type.

---

## 🔽 Dashboard Filter

The dashboard provides a restaurant type dropdown filter.

Users can select a restaurant type to analyze the corresponding:

* Number of restaurants
* Average rating
* Total votes
* Restaurant cost
* Other visual insights

This makes the dashboard interactive rather than a collection of static charts.

---

## 📁 Project Structure

```text
FoodDeliveryDashboard/
│
├── README.md
├── requirements.txt
├── app.py
├── dashboard.ipynb
├── AI_Analysis.txt
│
├── data/
│   └── Zomato-data-.csv
│
├── reports/
│   ├── rating_distribution.png
│   ├── top_restaurants_votes.png
│   ├── rating_vs_cost.png
│   ├── correlation_heatmap.png
│   └── rating_boxplot.png
│
└── Presentation/
    └── Food_Delivery_Restaurant_Analytics_Presentation_With_Codes.pptx
```

> **Note:** The filenames in the repository may vary slightly depending on the final files uploaded to GitHub.

---

## 🚀 Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/Ashutosh147sav/food-delivery-restaurant-dashboard.git
```

### Step 2: Open the Project Folder

```bash
cd food-delivery-restaurant-dashboard
```

### Step 3: Install Required Libraries

```bash
pip install -r requirements.txt
```

### Step 4: Run the Dash Application

```bash
python app.py
```

The dashboard will normally be available at:

```text
http://127.0.0.1:8050/
```

---

## 📦 Requirements

The project requires the following Python packages:

```text
dash
plotly
pandas
gunicorn
```

Additional libraries used in the analysis notebook include:

```text
numpy
matplotlib
seaborn
```

---

## ☁️ Deployment

The Plotly Dash application can be deployed using **GitHub and Render**.

### Render Build Command

```bash
pip install -r requirements.txt
```

### Render Start Command

```bash
gunicorn app:server
```

The Dash application exposes the server using:

```python
app = Dash(__name__)
server = app.server
```

This allows Gunicorn and Render to access the Dash application.

---

## 🤖 AI Tool Integration

AI tools were used as a supporting tool during the development of this project.

### Example Prompts Given to AI

1. How can I clean the rating and cost columns using Pandas?
2. How can I create a bar chart showing top-rated restaurants?
3. How can I create a scatter plot between restaurant rating and approximate cost?
4. How can I create a correlation heatmap for numerical columns?
5. How can I create a line chart for average restaurant ratings by restaurant type?
6. How can I create a boxplot for restaurant ratings?
7. How can I create a Plotly Dash dashboard with a dropdown filter?
8. How can I create a Dash callback?
9. How can I deploy a Dash application using GitHub and Render?
10. How can I debug errors occurring while running the dashboard?

### Evaluation of AI Responses

The AI-generated suggestions were tested using the actual dataset.

The code was modified wherever necessary according to:

* Dataset column names
* Data types
* Project requirements
* Runtime errors
* Dashboard requirements

AI was mainly used as a supporting tool for understanding Python, Pandas, data visualization, Plotly Dash, debugging and deployment.

Detailed AI prompts and evaluation are documented in:

```text
AI_Analysis.txt
```

---

## 🔍 Key Findings

The analysis produced the following major findings:

1. **Restaurant Ratings:**
   Restaurant ratings vary across the dataset, allowing restaurants to be compared based on customer ratings.

2. **Restaurant Popularity:**
   Restaurants with a higher number of votes show greater customer engagement and popularity.

3. **Rating and Cost:**
   Higher restaurant cost does not necessarily mean a higher rating.

4. **Online Ordering:**
   Restaurants with and without online ordering can be compared based on restaurant count and average rating.

5. **Table Booking:**
   Restaurants differ in the availability of table-booking facilities.

6. **Restaurant Types:**
   Different restaurant types show differences in their distribution and average ratings.

7. **Value for Money:**
   The value-score analysis helps identify restaurants that provide relatively good ratings at lower approximate costs.

---

## 🎓 Course Outcome Mapping

| Course Outcome | Project Application                  |
| -------------- | ------------------------------------ |
| **CO3**        | Exploratory Data Analysis            |
| **CO4**        | Data Visualization                   |
| **CO5**        | Dashboard Development and Deployment |

---

## 📚 Repository Contents

This repository contains the major components of the project:

* `README.md` — Project documentation
* `app.py` — Plotly Dash dashboard application
* `dashboard.ipynb` — Data analysis and visualization notebook
* `requirements.txt` — Python dependencies
* `data/` — Dataset or dataset information
* `reports/` — Exported visualization images
* `AI_Analysis.txt` — AI prompts and evaluation
* `Presentation/` — Project presentation

---

## 👥 Team Members

**Team Member 1:** [Name] — [Roll Number]
**Team Member 2:** [Name] — [Roll Number]
**Team Member 3:** [Name] — [Roll Number]

**College/University:** [College/University Name]

**Project Guide:** [Guide Name]

---

## 📌 Conclusion

The **Food Delivery Restaurant Analytics and Recommendation Dashboard** demonstrates the practical application of Python, Exploratory Data Analysis, data visualization and interactive dashboard development.

The project transforms raw restaurant data into meaningful insights that can help users compare restaurants based on:

* Ratings
* Popularity
* Approximate cost
* Restaurant type
* Online ordering
* Table booking
* Value for money

Overall, the project demonstrates the complete workflow of a data analytics application, from **data loading and preprocessing to EDA, visualization, interactive dashboard development, GitHub management and deployment**.

---

## ⭐ Project Highlights

* ✔ Python-based data analytics project
* ✔ Real-world Zomato restaurant dataset
* ✔ Data cleaning and preprocessing
* ✔ Exploratory Data Analysis
* ✔ Multiple statistical visualizations
* ✔ Interactive Plotly charts
* ✔ Plotly Dash dashboard
* ✔ Dropdown filtering
* ✔ Dash callback implementation
* ✔ AI-assisted development
* ✔ GitHub repository
* ✔ Render deployment

---

**Developed as an academic project using Python and Data Analytics.**
