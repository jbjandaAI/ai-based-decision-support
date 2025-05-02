from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
from ..core.database import Base

class ShellMaterial(str, enum.Enum):
    PLASTIC = "plastic"
    METAL = "metal"
    MIXED = "mixed"

class EwasteProduct(Base):
    __tablename__ = "ewaste_products"

    id = Column(Integer, primary_key=True, index=True)
    model_name = Column(String, index=True)
    manufacturer = Column(String, index=True)
    category = Column(String, index=True)
    nominal_weight = Column(Float)  # in kg
    initial_price = Column(Float)  # in currency units
    manufacturing_year = Column(Integer)
    dimensions = Column(String)  # stored as "length x width x height" in cm
    shell_material = Column(Enum(ShellMaterial))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    processing_records = relationship("ProcessingRecord", back_populates="product")

class ProcessingRecord(Base):
    __tablename__ = "processing_records"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("ewaste_products.id"))
    measured_weight = Column(Float)  # in kg
    image_path = Column(String)  # path to stored image
    confidence_score = Column(Float)  # AI recognition confidence
    evaluation_score = Column(Float)  # calculated value score
    intactness_score = Column(Float)  # calculated weight ratio score
    difficulty_score = Column(Float)  # calculated processing difficulty score
    recommended_path = Column(String)  # final recommended EoL path
    processed_at = Column(DateTime, default=datetime.utcnow)
    operator_id = Column(Integer, ForeignKey("users.id"))

    # Relationships
    product = relationship("EwasteProduct", back_populates="processing_records")
    operator = relationship("User", back_populates="processing_records") 