from typing import Optional
from sqlmodel import SQLModel, Field


class GuidelinesCorpus(SQLModel, table=True):
    __tablename__ = "guidelines_corpus"

    id: Optional[int] = Field(default=None, primary_key=True)
    source_name: str
    source_url: Optional[str] = Field(default=None)
    chunk_text: str
    embedding_vector: Optional[str] = Field(default=None, description="Serialized vector representation")
    corpus_type: str = Field(default="guideline", description="guideline or drug_reference")
