from pathlib import Path

from pydantic import (
    Field,
    field_validator,
    model_validator,
)
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)

PROJECT_ROOT = Path("__file__").resolve().parent


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env", ".env.prod"), env_file_encoding="utf-8", extra="ignore"
    )
    nlp_model: str = Field("bert-base", validation_alias="NLP_MODEL")
    ckip_dir: Path = Field(PROJECT_ROOT / ".ckip", validation_alias="CKIP_DIR")
    ckip_drivers_path: Path | None = Field(None)

    @model_validator(mode="after")
    @classmethod
    def config_drivers_path(cls, values: "Config"):  # noqa: F841
        values.ckip_drivers_path = values.ckip_dir / "ckip_drivers.pickle"
        return values

    @field_validator("ckip_dir")
    @classmethod
    def to_path(cls, v):  # noqa: F841
        return Path(v)


config = Config()
