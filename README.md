# 🛰️ Active Satelllites Data Visualization

> **🎓 Learning Project:** This repository is a technical exercise to practice data science, geospatial visualization, and web development, applying the concepts covered during Alura's Python Immersion (Imersão Alura de Python).

An interactive dashboard created to explore the global active satellite infrastructure from 2016. This exercise focuses on applying Python libraries to visualize orbital data.

---

## 📖 Objectives
The primary goal of this project was to handle a real-world dataset and transform raw information into actionable visual insights.
* **Data Wrangling:** Cleaning and standardizing country names and orbital data using `Pandas`.
* **Geospatial Logic:** Mapping individual satellites to specific **Launch Site** coordinates.
* **UI/UX Design:** Creating an intuitive dashboard interface with `Streamlit`.

## 🛠️ Tech Stack & Libraries Used
* **Python:** The core language for data logic.
* **Streamlit:** Used to build the web interface.
* **Pydeck:** Implemented for 3D geospatial scatter plots.
* **Plotly Express:** Used for statistical choropleth mapping.
* **NumPy:** Utilized for "jitter" logic to prevent data point overlapping.

## 🚀 Features Explored
* **Dynamic Visualization Toggle:** Learning how to switch between different map types (`Plotly` vs. `Pydeck`) based on user input.
* **Independent Filter Logic:** Implementing a filtering system where `Purpose`, `Orbit`, and `Launch Site` can be explored separately.
* **Interactive Tooltips:** Custom HTML tooltips to display satellite metadata (Name, Launch Site, etc.).

## 📂 Data Source
* **Dataset:** [Kaggle - Active Satellites](https://www.kaggle.com/datasets/ucsusa/active-satellites).
* **Note:** The dataset info is from 2016.

## 📥 How to use (Local Setup)
* **Clone the repository:**

* **Create a Virtual Environment: Open your local terminal**
  
  Windows
  ```bash
  python -m venv venv
  .\venv\Scripts\activate
  ```
  
  macOS/Linux
  ``` bash
  python3 -m venv venv
  source venv/bin/activate
  ```
* **Install requirements.txt file:**
  ``` bash
  pip install -r requirements.txt
  ```

* **Run Introduction.py:**
  ``` bash
  streamlit run Introduction.py
  ```
