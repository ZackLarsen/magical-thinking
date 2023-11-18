from prefect import flow, get_run_logger


@flow
def split():
    logger = get_run_logger()
    logger.info("Splitting data into train and test sets")
    splits = "Splits"
    return splits
