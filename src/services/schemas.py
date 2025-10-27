from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class ImageCrete(BaseModel):
    title: Optional[str]
    image_url: str

class ImageRead(BaseModel):
    pass