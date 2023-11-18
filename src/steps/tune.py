from prefect import flow, get_run_logger


@flow
def tune():
    logger = get_run_logger()
    logger.info("Tuning hyperparameters")
    tuned_model = "Tuned Model"

    return tuned_model
