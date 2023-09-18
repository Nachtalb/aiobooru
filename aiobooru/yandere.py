from datetime import datetime
from typing import Any

from .base import BooruPost


class YanderePost(BooruPost):
    id: int

    created_at: datetime
    updated_at: datetime

    rating: str
    source: str | None = None
    score: int
    parent_id: int | None = None
    has_children: bool
    is_pending: bool

    tag_string: str

    width: int
    height: int

    md5: str | None = None

    file_size: int
    file_url: str | None = None
    file_ext: str | None = None

    approver_id: int | None = None
    author: str
    change: int
    creator_id: int

    frames: list[str]
    frames_pending: list[str]
    frames_pending_string: str
    frames_string: str

    is_held: bool
    is_note_locked: bool
    is_rating_locked: bool
    is_shown_in_index: bool

    last_commented_at: int
    last_noted_at: int

    jpeg_file_size: int
    jpeg_height: int
    jpeg_url: str
    jpeg_width: int

    preview_url: str
    preview_height: int
    preview_width: int
    actual_preview_height: int
    actual_preview_width: int

    sample_file_size: int
    sample_height: int
    sample_url: str
    sample_width: int

    status: str

    @classmethod
    def de_json(cls, json: list[dict[str, Any]]) -> "YanderePost | None":  # type: ignore[override]
        if json:
            return cls(**json[0])
        return None

    @classmethod
    def de_jsons(cls, json: list[dict[str, Any]]) -> list["YanderePost"]:  # type: ignore[override]
        return [cls(**post) for post in json]
