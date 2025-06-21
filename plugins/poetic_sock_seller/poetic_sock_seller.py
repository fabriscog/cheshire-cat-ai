from cat.mad_hatter.decorators import tool
from cat.mad_hatter.decorators import hook

@tool
def socks_prices(color, cat):
    """How much do socks cost? Input is the sock color."""
    prices = {
        "black": 5,
        "white": 10,
        "pink": 50,
    }
    
    if color not in prices.keys():
        return f"No {color} socks"
    else:
        return f"{prices[color]} €"

@hook
def agent_prompt_prefix(prefix, cat):
    prefix = """You are Marvin the socks seller, a poetic vendor of socks.
You are an expert in socks, and you reply with exactly one rhyme.
"""
    return prefix