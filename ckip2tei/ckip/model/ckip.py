import pickle
from dataclasses import dataclass, field
from pathlib import Path, PosixPath
from typing import Optional

from ckip2tei.config import CKIP_DIR, CKIP_PATH


@dataclass(slots=True)
class CKIPClient:
    """
    The CKIPClient object connects to ckip drivers.
    """

    path: Optional[PosixPath | str] = None
    model: Optional[str] = None
    _ckip_path: str = field(init=False, repr=False)
    _nlp_model: str = field(init=False, repr=False)

    def __post_init__(self) -> None:
        self._ckip_path = self.path if self.path is not None else CKIP_PATH
        self._nlp_model = self.model if self.model is not None else "bert-base"
        self.on_ready()

    def on_ready(self) -> None:
        """The on_ready method initializes and caches the CKIP drivers."""
        has_path = Path(self._ckip_path).exists()

        if not has_path:
            from ckip_transformers.nlp import CkipPosTagger, CkipWordSegmenter

            Path(CKIP_DIR).mkdir(parents=True, exist_ok=True)
            drivers = (
                CkipWordSegmenter(model=self._nlp_model),
                CkipPosTagger(model=self._nlp_model),
            )

            with open(rf"{self._ckip_path}", "wb") as file:
                pickle.dump(drivers, file)

    def connect(self) -> tuple:
        """The connect method connects to the ckip drivers.

        Returns:
            a tuple that contains CkipWordSegmenter and CkipPosTagger.
        """
        with open(self._ckip_path, "rb") as file:
            return pickle.load(file)
