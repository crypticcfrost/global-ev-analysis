import matplotlib.pyplot as plt

def plot_data(analysis_results):
    print("Visualizing data .. (0%)")

    yearly_growth = analysis_results['yearly_growth']
    country_distribution = analysis_results['country_distribution']
    average_range_by_make = analysis_results['average_range_by_make']
    average_msrp_by_make = analysis_results['average_msrp_by_make']
    ev_type_distribution = analysis_results['ev_type_distribution']
    state_distribution = analysis_results['state_distribution']
    
    # Plotting yearly growth
    plt.figure(figsize=(10, 5))
    plt.plot(yearly_growth.index, yearly_growth.values, marker='o')
    plt.title('Yearly Growth of EV Adoption')
    plt.xlabel('Model Year')
    plt.ylabel('Number of EVs')
    plt.grid(True)
    plt.show()
    print("Visualizing data .. (20%)")

    # Plotting country distribution
    plt.figure(figsize=(12, 6))
    country_distribution.plot(kind='bar')
    plt.title('EV Adoption Distribution by Country')
    plt.xlabel('Country')
    plt.ylabel('Number of EVs')
    plt.xticks(rotation=90)
    plt.show()
    print("Visualizing data .. (40%)")

    # Plotting average electric range by make
    plt.figure(figsize=(12, 6))
    average_range_by_make.plot(kind='bar')
    plt.title('Average Electric Range by Make')
    plt.xlabel('Make')
    plt.ylabel('Average Electric Range (miles)')
    plt.xticks(rotation=90)
    plt.show()
    print("Visualizing data .. (60%)")

    # Plotting average base MSRP by make
    plt.figure(figsize=(12, 6))
    average_msrp_by_make.plot(kind='bar')
    plt.title('Average Base MSRP by Make')
    plt.xlabel('Make')
    plt.ylabel('Average Base MSRP ($)')
    plt.xticks(rotation=90)
    plt.show()
    print("Visualizing data .. (80%)")

    # Plotting distribution by electric vehicle type
    plt.figure(figsize=(12, 6))
    ev_type_distribution.plot(kind='bar')
    plt.title('Distribution by Electric Vehicle Type')
    plt.xlabel('Electric Vehicle Type')
    plt.ylabel('Number of EVs')
    plt.xticks(rotation=45)
    plt.show()

    # Plotting distribution by state
    plt.figure(figsize=(12, 6))
    state_distribution.plot(kind='bar')
    plt.title('EV Adoption Distribution by State')
    plt.xlabel('State')
    plt.ylabel('Number of EVs')
    plt.xticks(rotation=90)
    plt.show()
    print("Visualizing data .. (90%)")

    # Pie chart of market share by country
    plt.figure(figsize=(8, 8))
    country_distribution.plot(kind='pie', autopct='%1.1f%%')
    plt.title('Market Share of EV Adoption by Country')
    plt.ylabel('')
    plt.show()
    print("Visualizing data .. (100%)")
    print(" ---------- Data Visualization Completed ----------")
    print()