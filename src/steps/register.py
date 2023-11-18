from prefect import flow, get_run_logger


@flow
def register_model():
    logger = get_run_logger()
    logger.info("Registering model")
    registered_model = "Registered Model"
    return registered_model
