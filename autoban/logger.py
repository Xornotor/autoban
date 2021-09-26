import logging

logging.basicConfig(
    format="%(asctime)s [%(levelname)8s] [%(threadName)20s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
)

logging.captureWarnings(True)
