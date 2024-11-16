from Helpo.core import Helpo
from Helpo.decorators import module_help

async def deep_linking(chat_id: int, page: int = 1, message_id: int = None, instance: Helpo = None):
    if instance is None:
        raise ValueError("An instance of Helpo must be provided.")
    return await instance.show_help_menu(chat_id, page, message_id)

__all__ = ["Helpo", "module_help"]

__version__ = "1.0.0"
