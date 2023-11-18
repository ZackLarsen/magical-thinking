from hydra import compose, initialize

if __name__ == "__main__":
    with initialize(version_base="1.3.2",
                    config_path="config",
                    job_name="run_flow"):
        cfg = compose(config_name="main")
        print(cfg)
        print(cfg.message)
        print(cfg['run']['keep_columns'])
        print(cfg['run']['remove_outliers_threshold']['age'])
        print(cfg['run']['remove_outliers_threshold']['Income'])
