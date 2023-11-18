from prefect import flow, get_run_logger


@flow
def clean_data():
    """Clean the raw data."""
    logger = get_run_logger()
    logger.info("Cleaning data")
    clean_data = "Clean Data"
    return clean_data
