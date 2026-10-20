import asyncio
from fastapi import APIRouter, HTTPException
from mysite.chain.ticket_chain import ticket_chain
from mysite.schemas.ai_schema import TicketInputSchema, TicketOutputSchema, AnswerOutputSchema, AnswerInputSchema
from langchain_core.exceptions import OutputParserException
from mysite.chain.answer_chain import answer_chain
from mysite.chain.order_chain import order_chain
from mysite.schemas.ai_schema import OrderAIInputSchema, OrderAIOutputSchema


ai_router = APIRouter(prefix='/ai', tags=['AI Assistant'])

@ai_router.post('/analyze', response_model=TicketOutputSchema)
async def analyze_ticket(ticket: TicketInputSchema):
    text = ticket.text.strip()

    if not text:
        raise HTTPException(status_code=422, detail='Маалымат туура эмес форматта берилип жатат')

    try:
        result = await asyncio.wait_for(
            ticket_chain.ainvoke({"text": text}), timeout=120
     )

    except TimeoutError:
        raise HTTPException(status_code=500, detail='Модель тапшырманы аткарганы жетишкен жок')

    except OutputParserException:
        raise HTTPException(status_code=500, detail='Модельдин жообу схемага туура келбейт')

    return result



@ai_router.post('/answer/', response_model=AnswerOutputSchema)
async def answer_list(answer: AnswerInputSchema):
    text = answer.text.strip()
    facts = answer.facts.strip()

    if not text:
        raise HTTPException(status_code=422, detail='Маалымат туура эмес форматта берилип жат')

    try:
        result = await asyncio.wait_for(
            answer_chain.ainvoke({"text": text, 'facts': facts}), timeout=120
        )
    except TimeoutError:
        raise HTTPException(status_code=500, detail='Модель тапшырманы аткарганы жетишкен жок')

    except OutputParserException:
        raise HTTPException(status_code=500, detail='Модельдин жообу схемага туура келбейт')

    result = result.strip()

    return AnswerOutputSchema(text_draft=result)


@ai_router.post('/order', response_model=OrderAIOutputSchema)
async def analyze_order(order: OrderAIInputSchema):
    text = order.text.strip()

    if not text:
        raise HTTPException(status_code=422, detail='Маалымат туура эмес форматта берилип жатат')

    try:
        result = await asyncio.wait_for(
            order_chain.ainvoke({"text": text}), timeout=120
        )
    except asyncio.TimeoutError:
        raise HTTPException(status_code=504, detail='Модель тапшырманы аткарганы жетишкен жок')
    except OutputParserException:
        raise HTTPException(status_code=502, detail='Модельдин жообу схемага туура келбейт')

    return result