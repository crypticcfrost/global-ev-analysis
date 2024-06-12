import warnings
warnings.filterwarnings('ignore', category=FutureWarning)

def analyze_data(df):
    print("Analyzing data .. (0%)")

    # Analyzing growth over model years
    yearly_growth = df.groupby('Model Year')['VIN (1-10)'].count()
    print("Analyzing data .. (20%)")

    # Distribution across countries
    country_distribution = df.groupby('Country')['VIN (1-10)'].count()
    print("Analyzing data .. (40%)")

    # Average electric range by make
    average_range_by_make = df.groupby('Make')['Electric Range'].mean()
    print("Analyzing data .. (60%)")

    # Average base MSRP by make
    average_msrp_by_make = df.groupby('Make')['Base MSRP'].mean()
    print("Analyzing data .. (80%)")

    # Distribution by electric vehicle type
    ev_type_distribution = df.groupby('Electric Vehicle Type')['VIN (1-10)'].count()

    # Distribution by state
    state_distribution = df.groupby('State')['VIN (1-10)'].count()
    print("Analyzing data .. (100%)")
    print(" ---------- Data Analysis Completed ----------")
    print()

    return {
        'yearly_growth': yearly_growth,
        'country_distribution': country_distribution,
        'average_range_by_make': average_range_by_make,
        'average_msrp_by_make': average_msrp_by_make,
        'ev_type_distribution': ev_type_distribution,
        'state_distribution': state_distribution,
    }