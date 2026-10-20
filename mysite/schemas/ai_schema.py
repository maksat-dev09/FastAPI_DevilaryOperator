from pydantic import BaseModel, Field

class TicketInputSchema(BaseModel):
    text: str = Field(min_length=1, max_length=2000)

class TicketOutputSchema(BaseModel):
    answer: str = Field(min_length=1, max_length=300)
    order_id: int | None = Field(ge=1, default=None)
    priority: int = Field(ge=1, le=3)

class AnswerInputSchema(BaseModel):
    text: str = Field(min_length=1, max_length=2000)
    facts: str = Field(min_length=1, max_length=1000)

class AnswerOutputSchema(BaseModel):
    text_draft: str
    review: bool = True

class OrderAIInputSchema(BaseModel):
    text: str = Field(min_length=1, max_length=2000)

class OrderAIOutputSchema(BaseModel):
    answer: str = Field(min_length=1, max_length=300)
    product_name: str | None = Field(default=None, max_length=200)
    quantity: int = Field(ge=1, le=100, default=1)