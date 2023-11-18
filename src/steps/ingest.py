from prefect import flow, get_run_logger


@flow
def ingest_raw_data():
    """Ingest raw data from the data source."""
    logger = get_run_logger()
    logger.info("Ingesting raw data")
    raw_data = "Raw Data"
    return raw_data
