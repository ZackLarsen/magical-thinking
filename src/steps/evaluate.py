from prefect import flow, get_run_logger


@flow
def evaluate():
    logger = get_run_logger()
    logger.info("Evaluating model performance")
    metrics = "Evaluation Metrics"
    return metrics
