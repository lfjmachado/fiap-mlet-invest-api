from pydantic import BaseModel, Field

class Country(BaseModel):
    name: str = Field(title="Name", description="Name of the country")

    def __str__(self):
        return f"{self.name}"
    
    def __repr__(self):
        return f"Country(name={self.name})"