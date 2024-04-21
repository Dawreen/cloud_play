import logging


LOGGER = logging.getLogger(__name__)

def main():
    LOGGER.info("In main")

if __name__ == "__main__":
    LOGGER.info("Starting the machine!")
    main()