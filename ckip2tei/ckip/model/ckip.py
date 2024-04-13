from dataclasses import dataclass
from pathlib import Path
import pickle

from ckip2tei.config import config


@dataclass
class CKIPClient:
    """
    The CKIPClient object connects to ckip drivers.
    """

    def __post_init__(self) -> None:
        self.on_ready()

    def on_ready(self) -> None:
        """The on_ready method initializes and caches the CKIP drivers."""
        has_path = Path(config.ckip_drivers_path).exists()

        if not has_path:
            from ckip_transformers.nlp import (
                CkipPosTagger,
                CkipWordSegmenter,
            )

            Path(config.ckip_dir).mkdir(parents=True, exist_ok=True)
            drivers = (
                CkipWordSegmenter(model=config.nlp_model),
                CkipPosTagger(model=config.nlp_model),
            )

            with open(rf"{config.ckip_drivers_path}", "wb") as file:
                pickle.dump(drivers, file)

    def connect(self) -> tuple:
        """The connect method connects to the ckip drivers.

        Returns:
            a tuple that contains CkipWordSegmenter and CkipPosTagger.
        """
        with open(config.ckip_drivers_path, "rb") as file:
            return pickle.load(file)
