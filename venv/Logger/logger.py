import logging

# Create a custom logger
LOGGER = logging.getLogger(__name__)

# Create handlers
f_handler = logging.FileHandler('Logger/file.log')

# Set level
LOGGER.setLevel(logging.DEBUG)

# Create formatters and add it to handlers
f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
f_handler.setFormatter(f_format)

# Add handlers to the loggers
LOGGER.addHandler(f_handler)








