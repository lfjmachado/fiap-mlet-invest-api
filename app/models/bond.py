from pydantic import BaseModel, Field
from models.country import Country

class Bond(BaseModel):
    country: Country = None
    name: str = Field(title="Name", description="Name of the bond")
    full_name: str = Field(title="Full Name", description="Full name of the bond")

    def __str__(self):
        return f"{self.name} ({self.country})"

    def __repr__(self):
        return f"Bond(country={self.country}, name={self.name}, full_name={self.full_name})"