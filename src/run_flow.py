import sys
from pathlib import Path

import hydra
from hydra import compose, initialize
from omegaconf import DictConfig
from prefect import flow, get_run_logger

sys.path.append(Path.cwd().parent)

from steps.ingest import ingest_raw_data
from steps.clean import clean_data
from steps.split import split
from steps.transform import transform
from steps.train import train
from steps.evaluate import evaluate
from steps.tune import tune
from steps.register import register_model


@flow
@hydra.main(config_path="config", config_name="main", version_base="1.3.2")
def run_flow(cfg: DictConfig) -> None:
    logger = get_run_logger()
    logger.info("Running flow")
    logger.info(cfg.message)
    logger.info(f"Age threshold: {cfg['run']['remove_outliers_threshold']['age']}")
    logger.info(f"Income threshold: {cfg['run']['remove_outliers_threshold']['income']}")
    logger.info(cfg['run']['keep_columns'])
    ingest_raw_data()
    clean_data()
    split()
    transform()
    train()
    evaluate()
    tune()
    register_model()


if __name__ == "__main__":
    with initialize(version_base="1.3.2",
                    config_path="config",
                    job_name="run_flow"):
        cfg = compose(config_name="main")
        run_flow(cfg)
