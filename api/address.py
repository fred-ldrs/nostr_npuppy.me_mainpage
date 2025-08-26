from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional

from . import models, auth

router = APIRouter()

@router.post("/register", response_model=models.NostrAddress)
async def register_address(
    address: models.AddressCreate, 
    current_user: models.User = Depends(auth.get_current_user)
):
    """
    Register a new npuppy.me address for the authenticated user
    """
    # In a real app:
    # 1. Check if the address is already taken
    # 2. Check if user has reached their limit (10 addresses)
    # 3. Save to database
    
    # For this example, return a mock response
    return models.NostrAddress(
        id=1,
        username=address.username,
        npub_key=address.npub_key,
        user_id=current_user.id
    )

@router.get("/my-addresses", response_model=List[models.NostrAddress])
async def get_user_addresses(current_user: models.User = Depends(auth.get_current_user)):
    """
    Get all addresses for the authenticated user
    """
    # In a real app, fetch from database
    # For this example, return mock data
    return [
        models.NostrAddress(
            id=1,
            username="example",
            npub_key="npub1abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnop",
            user_id=current_user.id
        )
    ]

@router.put("/{address_id}", response_model=models.NostrAddress)
async def update_address(
    address_id: int,
    address_update: models.AddressCreate,
    current_user: models.User = Depends(auth.get_current_user)
):
    """
    Update an existing address
    """
    # In a real app:
    # 1. Check if address exists and belongs to user
    # 2. Update in database
    
    # For this example, return mock response
    return models.NostrAddress(
        id=address_id,
        username=address_update.username,
        npub_key=address_update.npub_key,
        user_id=current_user.id
    )

@router.delete("/{address_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_address(
    address_id: int,
    current_user: models.User = Depends(auth.get_current_user)
):
    """
    Delete an address
    """
    # In a real app:
    # 1. Check if address exists and belongs to user
    # 2. Delete from database
    
    # For this example, just return success
    return {"status": "success"}
