# Winter Holidays
# Author: Pritika 
# 8 January 2024

# Requirements:
#  - create a function called winter_holiday()
#     - takes one parameter - string
#     - returns a summary of an event from your holidays

# Please do not use ChatGPT or any LLM

# If you use an LLM, indicate that you did use it
# Also, write the prompt that you used
# I USED CHATGPT
# Prompt: ...


import random


def winter_holiday(good_or_bad: str) -> str:
    """Give a summary of our winter holidays 2023/24

    Params:
        good_or_bad - string that indicates whether the event
            is good or bad

    Returns:
        an event that happened to you during the holidays
        the event is selected part"""
    
    # If the event is good, return a good event
    # TODO: return a randomly chosen good event
    if good_or_bad == "good":
        return 
    list_of_good_things = [f"I slept in. It was great.",
    "I went to the Landsdown mall. The christmas tree was pretty there.",
    "I went to the library.",
    "I began crochetting a blanket for myself."]

    random_response = random.choice(list_of_good_things)

    print(random_response)

    # If the event is bad, return a bad event
    if good_or_bad == "bad":
        return "I only watched a few chritsmas movies"
def main() -> None:
    # Runs all the things we want to test in our .py file
    print(winter_holiday("good"))
    # "I got a Lego set for the first time in a long time."
    # "I went to Richmond Centre to walk around aimlessly."
    print(winter_holiday("bad"))
    # "I hoped to snowboard during the holiday and there was only rain."
    # "I asked for a bidet for Christmas, instead I got a rando smart watch amazon."


# If we're running THIS FILE using Python
if __name__ == "__main__":
    main()
