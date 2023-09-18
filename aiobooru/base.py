from datetime import datetime
from typing import Any

from pydantic import BaseModel


class BooruPost(BaseModel):
    id: int
    created_at: datetime

    file_size: int | None
    file_url: str | None
    file_ext: str | None

    md5: str | None

    width: int | None
    height: int | None

    @classmethod
    def de_json(cls, json: dict[str, Any]) -> "BooruPost | None":
        raise NotImplementedError

    @classmethod
    def de_jsons(cls, json: list[dict[str, Any]]) -> list["BooruPost"]:
        raise NotImplementedError
