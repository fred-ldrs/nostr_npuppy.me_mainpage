from datetime import datetime
from pydantic import BaseModel, Field, validator
import re

class User(BaseModel):
    id: int = None
    username: str
    password_hash: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class UserCreate(BaseModel):
    username: str
    password: str

    @validator('username')
    def username_valid(cls, v):
        if not re.match(r'^[a-zA-Z0-9._-]{3,30}$', v):
            raise ValueError('Username must be 3-30 alphanumeric characters, dots, underscores, or hyphens')
        return v

    @validator('password')
    def password_valid(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters')
        return v

class NostrAddress(BaseModel):
    id: int = None
    username: str
    npub_key: str
    user_id: int
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    
    @validator('username')
    def username_valid(cls, v):
        if not re.match(r'^[a-zA-Z0-9._-]{3,30}$', v):
            raise ValueError('Address must be 3-30 alphanumeric characters, dots, underscores, or hyphens')
        return v.lower()  # Store addresses as lowercase

class AddressCreate(BaseModel):
    username: str
    npub_key: str
    
    @validator('npub_key')
    def npub_key_valid(cls, v):
        if not v.startswith('npub1'):
            raise ValueError('NPUB key must start with npub1')
        return v

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str = None
