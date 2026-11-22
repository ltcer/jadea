DEFAULTS = {"timeout": 5, "retries": 3, "verbose": False}


def load(overrides=None):
    cfg = dict(DEFAULTS)
    if overrides:
        cfg.update(overrides)
    return cfg
