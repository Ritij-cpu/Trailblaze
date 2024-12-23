# Trailblaze

Trailblaze is a dynamic and visually captivating **Startup Funding Analysis Dashboard** built using **Streamlit**. It provides comprehensive insights into startup funding trends, investors' activities, and overall analysis to assist users in exploring and understanding the startup ecosystem.

---

## Features

### 1. **Overall Analysis**
   - Total investment amount.
   - Maximum funding received by a startup.
   - Average ticket size.
   - Count of funded startups.
   - Month-on-Month investment trend visualization.

### 2. **Investor-Specific Analysis**
   - Recent investments made by the selected investor.
   - Biggest investments by the investor.
   - Sector-wise distribution of investments.
   - Year-on-Year investment trends.

### 3. **Startup-Specific Analysis**
   - Detailed analysis for selected startups.

---

## Technologies Used

- **Python**: Core programming language.
- **Streamlit**: Framework for creating the interactive web application.
- **Matplotlib**: Library for creating visualizations.
- **Pandas**: Data manipulation and analysis.

---

## Installation and Setup

### Prerequisites
Ensure you have the following installed:
- Python 3.7+
- pip (Python package manager)

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/<your-username>/Trailblaze.git
   cd Trailblaze
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   streamlit run app.py
   ```

5. **Access the Dashboard**:
   Open your browser and go to `http://localhost:8501`.

---

## Usage

- Navigate to the sidebar to select analysis types.
- Explore insights from the "Overall Analysis", "Investor", or "Startup" perspectives.
- Interact with visualizations and metrics to understand the startup funding ecosystem.

---

## Directory Structure

```
Trailblaze/
├── app.py                # Main application file
├── startup_cleaned.csv   # Dataset used for analysis
├── requirements.txt      # List of dependencies
├── README.md             # Project documentation
└── .venv/                # Virtual environment (optional, not in repo)
```

---

## Future Enhancements

- **Enhanced Visualizations**: Add more interactive graphs and charts.
- **Export Options**: Allow users to download reports.
- **Integration**: Connect with APIs for live data updates.
- **Advanced Filtering**: Enable more detailed filtering options.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contributions

Contributions are welcome! Feel free to fork the repository and submit pull requests.

---

## Contact

For any inquiries or feedback, reach out to:
- **Email**: srivastavaritij49@gmail.com
- **GitHub**: [Ritij-cpu](https://github.com/Ritij-cpu)

---

Thank you for exploring **Trailblaze**! 🚀
