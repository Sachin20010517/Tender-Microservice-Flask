# dbConfig/cleanup.py

import os
import logging

def remove_generated_outs():
    try:
        # Remove directory if it exists
        if os.path.exists("outs"):
            os.rmdir("outs")
            logging.info("Deleted pre-generated apps in 'outs/'")

        # Recreate directory
        os.mkdir("outs")
        logging.info("Created a fresh 'outs/' directory")
    except Exception as e:
        logging.error("Error managing 'outs/' directory", exc_info=True)
