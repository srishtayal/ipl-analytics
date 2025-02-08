## 🏏 IPL Analytics Dashboard

### 📌 Overview  
The **IPL Analytics Dashboard** is an interactive web application built using **Streamlit**, **Pandas**, and **Matplotlib** that provides deep insights into IPL matches from **2008 to 2024**. It allows users to explore key statistics such as team performances, player achievements, and venue trends.

### 🚀 Features  
 **- Total Matches Per Season** – View the total matches played per IPL season  
 **- Most Successful Teams** – Analyze team wins and win percentages  
 **- Player of the Match Awards** – Discover players with the most MVP awards  
 **- Venue Analysis** – Identify the best batting and chasing grounds  
 **- Top Scorers & Wicket Takers** – Check leading run-scorers and wicket-takers  
 **- Death Over Specialists** – Find bowlers with the best economy in the last 5 overs  
 **- Best Finishers** – See the highest strike rates in the last 5 overs  
 **- Most Impactful Players** – Rank players based on runs + wickets  

### 🏗 Tech Stack  
- **Frontend**: Streamlit (Python-based interactive UI)  
- **Backend**: Pandas for data analysis, Matplotlib for visualizations  
- **Data**: IPL matches and deliveries dataset (`matches.csv`, `deliveries.csv`)  

### 📂 Installation & Usage  
#### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/srishtayal/ipl-analytics.git
cd ipl-analytics
```

#### 2️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```

#### 3️⃣ Run the Application  
```bash
streamlit run main.py
```

### 📊 Data Cleaning & Processing  
- **Handled missing values**: Filled null values in `winner`, `city`, and umpire columns  
- **Standardized team names**: Renamed **Delhi Daredevils → Delhi Capitals**, **Deccan Chargers → Sunrisers Hyderabad**  
- **Converted date formats** for better analysis  

