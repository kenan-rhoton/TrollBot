def vote(*choices : str):
    msg = ""
    error = None

    if len(choices) < 3:
        msg = f"Usage: ?vote \"Vote title\" \"Option 1\" \"Option 2\" \"...\""
        error = "NotEnoughArgs"
    else:
        msg = f"{choices[0]}"
        number = [
                "potato",
                "bacon",
                "alien",
                "upside_down",
                "sunny",
                "see_no_evil",
                "cactus"
                ]
        
        for i, choice in enumerate(choices[1:]):
            msg += f"\n:{number[i]}: {choice}"
    
    return msg, error
