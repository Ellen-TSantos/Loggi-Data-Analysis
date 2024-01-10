import json
from data_loader import load_data
from data_processing import create_dataframe
from data_analysis import analyze_data
from dataFrame_object import create_and_plot_deliveries_dataframe  
import logging
import os
import wget

logging.basicConfig(filename='projeto.log', level=logging.INFO)

def main():
    try:
        file_url = "https://raw.githubusercontent.com/andre-marcos-perez/ebac-course-utils/main/dataset/deliveries.json"
        file_path = "deliveries.json"

        # Download the file if it doesn't exist
        if not os.path.exists(file_path):
            print(f"Downloading {file_url}...")
            wget.download(file_url, out=file_path)
            print("\nDownload complete.")

        # Load data from the file
        data = load_data(file_path)

        # Call the function to create the DataFrame and generate the graphs
        deliveries_df, deliveries_normalized_df, graph_paths = create_and_plot_deliveries_dataframe()
        deliveries_normalized_df = create_dataframe(data)

        # Rest of the code for data analysis
        analysis_results = analyze_data(deliveries_normalized_df)

        logging.info("Data analysis and graph generation completed successfully.")

        # Use information from charts as needed
        print("Bar chart saved successfully:", graph_paths['bar_chart'])
        print("Successfully saved scatter plot:", graph_paths['scatter_plot'])
        print("Pie chart saved successfully:", graph_paths['pizza graph'])

    except FileNotFoundError:
        logging.error("Error: The file 'deliveries.json' was not found.")
    except json.JSONDecodeError as je:
        logging.error(f"Error decoding JSON: {je}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
