from prefect import flow, get_run_logger


@flow
def train():
    logger = get_run_logger()
    logger.info("Training model")
    trained_model = "Trained Model"
    return trained_model
