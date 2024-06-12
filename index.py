# Virtual Environment Instructions

# To create a virtual environment on your local system, run the following commands:
# python3 -m venv myvenv
# source myvenv/Scripts/activate
# pip install -r requirements.txt

from data_cleaning import clean_data
from data_analysis import analyze_data
from data_visualisation import plot_data

def main():
    # Step 1: Data Cleaning
    cleaned_df = clean_data('data/global_ev_adoption.csv')
    cleaned_df.to_csv('data/cleaned_ev_adoption.csv', index=False)
    
    # Step 2: Data Analysis
    analysis_results = analyze_data(cleaned_df)
    
    # Step 3: Data Visualization
    plot_data(analysis_results)
    print("Successfully completed data cleaning, analysis and visualization!")

if __name__ == "__main__":
    main()
