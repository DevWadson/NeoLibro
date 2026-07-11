"""Exceções customizadas do NeoLibro.

Define a hierarquia de exceções para erros de domínio,
incluindo duplicidade, busca e operações inválidas.
"""
from .neolibro_error import NeoLibroError
from .duplicate_work_error import DuplicateWorkError
from .invalid_price_error import InvalidTypePriceError, EmptyPriceError, NegativePriceError
from .missing_search_criteria_error import MissingSearchCriteriaError
from .work_not_found_error import WorkNotFoundByCodeError, WorkNotFoundByTitleError
