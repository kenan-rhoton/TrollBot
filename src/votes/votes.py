def vote(*choices : str):
    msg = ""
    error = None

    if len(choices) < 3:
        msg = f"Usage: ?vote \"Vote title\" \"Option 1\" \"Option 2\" \"...\""
        error = "NotEnoughArgs"
    else:
        msg = f"{choices[0]}"
        number = [
                "regional_indicator_a",
                "regional_indicator_b",
                "regional_indicator_c",
                "regional_indicator_d",
                "regional_indicator_e",
                "regional_indicator_f",
                "regional_indicator_g"
                ]
        
        for i, choice in enumerate(choices[1:]):
            msg += f"\n:{number[i]}: {choice}"
    
    return msg, error
