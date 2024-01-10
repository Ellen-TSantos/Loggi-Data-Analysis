import logging
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def analyze_data(deliveries_normalized_df, analyze_size=True, analyze_region=True):
    # Log that data analysis is starting
    logging.info("Starting data analysis.")
    
    # Check if the 'region' column is present in the DataFrame
    if 'region' in deliveries_normalized_df.columns:
        # Analyze delivery sizes if specified
        if analyze_size:
            logging.info("Analyzing delivery sizes.")
            # Calculate the mean delivery size
            mean_delivery_size = deliveries_normalized_df['deliveries_size'].mean()
            print(f'Average delivery size: {mean_delivery_size}')

        # Analyze delivery regions if specified
        if analyze_region:
            logging.info("Analyzing delivery regions.")
            # Count the deliveries in each region
            region_counts = deliveries_normalized_df['region'].value_counts()
            print('Delivery count by region:')
            print(region_counts)
            logging.info("Data analysis completed.")

        # Analyze descriptive statistics of delivery coordinates
        delivery_lat_stats = deliveries_normalized_df['deliveries_lat'].describe()
        delivery_lng_stats = deliveries_normalized_df['deliveries_lng'].describe()
        print('Descriptive statistics of delivery coordinates (Latitude):')
        print(delivery_lat_stats)
        print('Descriptive statistics of delivery coordinates (Longitude):')
        print(delivery_lng_stats)

        # Create a dictionary to store the analysis results
        analysis_results = {
            'mean_delivery_size': mean_delivery_size,
            'region_counts': region_counts,
            'delivery_lat_stats': delivery_lat_stats,
            'delivery_lng_stats': delivery_lng_stats
        }

        # Return the analysis results
        return analysis_results
    else:
        # Log an error if the 'region' column is not present
        logging.error("Error.")
