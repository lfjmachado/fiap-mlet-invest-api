from fastapi import APIRouter, Depends, HTTPException
from models.bond import Bond
from models.country import Country
from typing import List, Union
import investpy

router = APIRouter()

@router.get("/bonds/{country}", response_model=List[Bond])
async def get_bonds(country: str = None) -> List[Bond]:
    if country is None:
        raise HTTPException(status_code=400, detail="Country parameter is required")
    try:
        df = investpy.get_bonds(country=country)
        if df.empty:
            raise HTTPException(status_code=404, detail="Bonds not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    list_bonds = []
    for _, row in df.iterrows():
        bond = Bond(
            country=Country(name=row['country']),
            name=row['name'],
            full_name=row['full_name']
        )
        list_bonds.append(bond)
    return list_bonds