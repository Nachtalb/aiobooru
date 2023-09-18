from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field

from .base import BooruPost


class DanbooruFile(BaseModel):
    type: str
    url: str
    width: int
    height: int
    file_ext: str


class DanbooruMediaAsset(BaseModel):
    id: int
    created_at: datetime
    updated_at: datetime
    md5: str
    file_ext: str
    file_size: int
    width: int = Field(..., alias="image_width")
    height: int = Field(..., alias="image_height")
    duration: float | None = None
    status: str
    file_key: str
    is_public: bool
    pixel_hash: str
    variants: list[DanbooruFile] = []

    @property
    def original(self) -> DanbooruFile | None:
        return next((f for f in self.variants if f.type == "original"), None)


class DanbooruPost(BooruPost):
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

    width: int = Field(..., alias="image_width")
    height: int = Field(..., alias="image_height")

    file_size: int
    file_url: str | None = None
    file_ext: str | None = None
    md5: str | None = None

    large_file_url: str | None = None
    preview_file_url: str | None = None

    media_asset: DanbooruMediaAsset

    uploader_id: int
    approver_id: int | None = None

    pixiv_id: int | None = None

    up_score: int
    down_score: int
    fav_count: int

    tag_string_general: str
    tag_string_artist: str
    tag_string_copyright: str
    tag_string_character: str
    tag_string_meta: str
    tag_count_general: int
    tag_count_artist: int
    tag_count_copyright: int
    tag_count_character: int
    tag_count_meta: int

    last_comment_bumped_at: datetime | None = None
    last_noted_at: datetime | None = None

    has_large: bool
    has_visible_children: bool
    has_active_children: bool

    is_banned: bool
    is_deleted: bool
    is_flagged: bool

    bit_flags: int

    @classmethod
    def de_json(cls, json: dict[str, Any]) -> "DanbooruPost | None":
        if json:
            return cls(**json)
        return None

    @classmethod
    def de_jsons(cls, json: list[dict[str, Any]]) -> list["DanbooruPost"]:  # type: ignore[override]
        return [cls(**post) for post in json]
