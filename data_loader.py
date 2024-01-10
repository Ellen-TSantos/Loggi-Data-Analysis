import json
import logging

def load_data(file_path='deliveries.json'):
    try:
        # Log that the file loading process is starting
        logging.info(f"Loading the file: {file_path}")
        
        # Open the file in read mode with UTF-8 encoding
        with open(file_path, mode='r', encoding='utf8') as file:
            # Read the content of the file
            file_content = file.read()
            
            # Check if the file is empty
            if not file_content:
                # If empty, raise a ValueError
                raise ValueError("The file is empty.")
            
            # Parse the JSON content of the file
            data = json.loads(file_content)
            
            # Log that data loading was successful
            logging.info("Data loaded successfully.")
        
        # Return the loaded data
        return data
    
    # Handle the case when the specified file is not found
    except FileNotFoundError:
        logging.error(f"Error: The file '{file_path}' was not found.")
    
    # Handle JSON decoding errors
    except json.JSONDecodeError as je:
        logging.error(f"Error when decoding JSON: {je}")
    
    # Handle other unexpected errors
    except Exception as e:
        logging.error(f"Error unexpected: {e}")
        
        # Reraise the exception after logging it
        raise

