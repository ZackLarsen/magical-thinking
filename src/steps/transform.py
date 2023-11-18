from prefect import flow, get_run_logger


@flow
def transform():
    logger = get_run_logger()
    logger.info("Transforming the data")
    transformed_data = "Transformed data"

    return transformed_data
