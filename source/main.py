import random
import time
import os
import types
from colorama import Fore, Back, Style

# Debug
IS_DEV_BUILD = True
console_used = False
suppress = False

# Game state
is_running = True
player_credits = 250
spins = 0
wins = 0
streak = 0
jackpots = 0
total_won = 0
total_lost = 0

# Misc
kidneys = 2
is_high_roller = False
roulette_chips = 0
spouse = "wife"
cake = "thecakeisalie"

# Upgrade purchases
luck_upgrades = 0
reward_upgrades = 0
streak_upgrades = 0
speed_upgrades = 0

# Upgrade prices
luck_upgrade_price = 50
reward_upgrade_price = 25
streak_upgrade_price = 25
speed_upgrade_price = 50

# Game parameters
luck = 0
reward_multiplier = 1.0
streak_multiplier = 1.1

# bar variables
bar_dialogue_count = 0

# Bank variables
has_loan = False
fake_id = False
interest_percent = 0.05
loan_payment = 0
loan_amount = 0
days_passed = 0

# Insurance variables
has_insurance = False
insurance_coverage = 0
insurance_payment = 0
insurance_type = 0
total_covered = 0
insurance_base = 0

# Achievement variables
total_won = 0
total_lost = 0
total_spent_in_shop = 0
loans_total = 0
loans_paid = 0

# Borrowing variables
has_borrow = False
has_borrowed = False
borrow_amount = 0

# Checks
ach_x = f"{Fore.MAGENTA}x{Style.RESET_ALL}"

achievements = {

    "getting_somewhere": False,  # win a spin for the first time #
    "on_a_roll": False,  # win 1,000 credits #
    "a_decent_sum": False,  # win 10,000 credits #
    "rolling_in_dough": False,  # win 100,000 credits #
    "millionaire": False,  # win 1,000,000 credits #

    "oof_moment": False,  # lose a spin for the first time #
    "you_should_stop": False,  # lose 1,000 credits #
    "you_should_REALLY_stop": False,  # lose 10,000 credits #
    "you're_just_gonna_lose_more": False,  # lose 100,000 credits #
    "rock_bottom": False,  # lose 1,000,000 credits #

    "confidence_is_key": False,  # go all in on a spin #
    "i_can't_stop_winning": False,  # win an all-in spin #
    "aw_dangit": False,  # lose an all-in spin #

    "at_least_i_still_have_clothes": False,  # take out a loan #
    "petty_cash": False,  # take out a loan less than or equal to 10 credits #
    "money_management": False,  # pay back a loan #
    "still_hanging_in_there": False,  # take out another loan #
    "redemption_arc": False,  # pay back your third loan #

    "i_feel_funny": False,  # first shop purchase #
    "big_spender": False,  # spend 1,000 credits in the shop #
    "i'll_have_the_regular": False,  # spend 10,000 credits in the shop #
    "writing_checks_left_and_right": False,  # spend 100,000 credits in the shop #
    "overload": False,  # max out energy drinks #

    "insured": False,  # purchase an insurance plan #
    "volatile": False,  # make your insurance rate rise #
    "the_bills_caught_up_to_you": False,  # can't afford an insurance payment #

    "your_family_is_worried": False,  # spend 14 days gambling #
    "concerning_hygeine": False,  # spend 50 days gambling #
    "what_year_is_it": False,  # spend 100 days gambling #
    "the_light_is_blinding": False  # leave the casino after 100 days #

}

# bonus achievements
bonus_achievements = {
    "counting_cards": False, # use the devtools #
    "extra_zesty": False, # see all flavor text #
    "regular_patron": False,  # have every conversation with the bartender #
    "back_from_the_brink": False,  # win the deal #
    "last_resort": False,  # sell a kidney #
    "shifty_business": False  # buy a fake ID #
}

# Bonus and letter options
bonuses = ["WIN", "FUN", "FLY", "ABC", "AAA", "DIE", "ASS", "AOL", "HIT",
           "BRO", "BET", "TIT", "SCP", "WHY", "BOP", "BEE", "BUM", "ZAP",
           "DEW", "MUM", "HAG", "WTF", "PBS", "POO"]
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
           "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X",
           "Y", "Z"]

# FLAVOR TEXT (EXTRA ZESTY)
flavor_text = [
    {"days_start": 0, "days_end": 1, "text": f"You can practically taste your {Fore.GREEN}winnings{Style.RESET_ALL} already.", "displayed": False},
    {"days_start": 2, "days_end": 5, "text": "You haven't been here very long, but you feel like you could stay forever.", "displayed": False},
    {"days_start": 6, "days_end": 9, "text": "You begin to notice a regular deposit of crumbs at your machine. Are they yours?", "displayed": False},
    {"days_start": 10, "days_end": 14, "text": f"The handle on the machine is getting {Style.DIM}greasy{Style.RESET_ALL}. You should wash your hands.", "displayed": False},
    {"days_start": 15, "days_end": 19, "text": f"Your back is {Style.DIM}weary{Style.RESET_ALL} of hunching over the machine. Taking a walk might help.", "displayed": False},
    {"days_start": 20, "days_end": 24, "text": f"You haven't seen the {Style.BRIGHT}{Fore.YELLOW}sun{Style.RESET_ALL} in quite a while.", "displayed": False},
    {"days_start": 25, "days_end": 54, "text": "Are you satisfied yet?", "displayed": False},
    {"days_start": 55, "days_end": 94, "text": f"Your committment would be inspiring, were it not an {Fore.RED}addiction{Style.RESET_ALL}.", "displayed": False},
    {"days_start": 95, "days_end": 100, "text": "Is the casino still real?", "displayed": False}
]

bar_dialogue = [
    '"Hey there, care for a drink?"',
    f'"How are the {Fore.GREEN}winnings{Style.RESET_ALL}?"',
    '"Good day, huh?"',
    '"Business is slow today. Take a look."',
    '"What\'s new?"',
    f'"Every day\'s a good day to get {Fore.GREEN}drunk{Style.RESET_ALL}."',
    '"How\'re the kids?"',
    '"My husband says I need to get a real job."',
    '"Rough day, huh?"',
    f'"Here, have a {Fore.YELLOW}beer{Style.RESET_ALL} on me."',
    '"Kids these days..."',
    f'"Went to college for {Fore.BLUE}physics{Style.RESET_ALL}, why am I here?"',
    '"Everyone leaves eventually. Will you?"'
]

bar_actions = [
    "The bartender looks up and says, ",
    "The bartender doesn't look up when you enter.",
    "The bartender seems engrossed in cleaning a glass. He doesn't appear to notice you.",
    f"The bartender is wiping down the counter - the room smells vaguely of {Fore.CYAN}cleaning chemicals{Style.RESET_ALL} and {Fore.GREEN}vomit{Style.RESET_ALL}.",
    f"The bartender isn't in. There's a sign that says: \"Leave the {Fore.YELLOW}money{Style.RESET_ALL} on the counter. Help yourself.\"",
    f"The bartender isn't in. There's a {Fore.RED}woman{Style.RESET_ALL} at the counter who eyes you with an {Fore.MAGENTA}emotion{Style.RESET_ALL} you can't decipher."
]


def pick_flavor_text():
    global spins, flavor_text
    for f in flavor_text:
        if f["days_start"] <= spins <= f["days_end"] and not f["displayed"]:
            if random.randint(1, ((f["days_end"] - f["days_start"]))) == 1:
                f["displayed"] = True
                return f["text"]
            else:
                return "Just another day in the casino."
        return "Just another day in the casino."

# Clear the screen
def clear_screen():
    if os.name == 'nt':  # windows
        os.system('cls')
    else:  # mac & linux (posix)
        os.system('clear')

def btn(label):
    return f"[{Style.BRIGHT}{Fore.CYAN}{label.upper()}{Style.RESET_ALL}]"

def calculate_achievements():
    if total_won >= 1:
        achievements["getting_somewhere"] = True
    if total_won >= 1000:
        achievements["on_a_roll"] = True
    if total_won >= 10000:
        achievements["a_decent_sum"] = True
    if total_won >= 100000:
        achievements["rolling_in_dough"] = True
    if total_won >= 1000000:
        achievements["millionaire"] = True

    if total_lost >= 1:
        achievements["oof_moment"] = True
    if total_lost >= 1000:
        achievements["you_should_stop"] = True
    if total_lost >= 10000:
        achievements["you_should_REALLY_stop"] = True
    if total_lost >= 100000:
        achievements["you're_just_gonna_lose_more"] = True
    if total_lost >= 1000000:
        achievements["rock_bottom"] = True

    if total_spent_in_shop >= 1:
        achievements["i_feel_funny"] = True
    if total_spent_in_shop >= 1000:
        achievements["big_spender"] = True
    if total_spent_in_shop >= 10000:
        achievements["i'll_have_the_regular"] = True
    if total_spent_in_shop >= 100000:
        achievements["writing_checks_left_and_right"] = True

    if has_insurance:
        achievements["insured"] = True
    if insurance_payment > insurance_base:
        achievements["volatile"] = True

    if spins >= 14:
        achievements["your_family_is_worried"] = True
    if spins >= 50:
        achievements["concerning_hygeine"] = True
    if spins >= 100:
        achievements["what_year_is_it"] = True

    if console_used == True:
        bonus_achievements["counting_cards"] = True
        
    b = 0
    for f in flavor_text:
        if f["displayed"]:
            b += 1
    if b == len(flavor_text):
        bonus_achievements["extra_zesty"] = True


# display all achievements
def display_achievements():
    calculate_achievements()
    global achievements, console_used
    a = 0
    for i in achievements.keys():
        if achievements[i]:
            a += 1

    try:
        # calculate percent of achievements
        p = round((100 * (a / len(achievements))))
    except ZeroDivisionError:
        p = 0
    if p == 100:
        p = f"{Fore.GREEN}100%{Style.RESET_ALL}"
    else:
        p = f"{p}%"

    print(f"""
You've Unlocked [{f"{Fore.GREEN}{a}/{len(achievements)}{Style.RESET_ALL}" if a == len(achievements) else f"{a}/{len(achievements)}"}] Achievements ({p}) {f"({Fore.RED}Cheats used{Style.RESET_ALL})" if console_used else ""}
    
    [{ach_x if achievements["getting_somewhere"] else " "}] Getting Somewhere (Win a spin)
    [{ach_x if achievements["on_a_roll"] else " "}] On a Roll (Win a total of 1,000 credits)
    [{ach_x if achievements["a_decent_sum"] else " "}] A Decent Sum (Win a total of 10,000 credits)
    [{ach_x if achievements["rolling_in_dough"] else " "}] Rolling in Dough (Win a total of 100,000 credits)
    [{ach_x if achievements["millionaire"] else " "}] Millionaire (Win a total of 1,000,000 credits)

    [{ach_x if achievements["oof_moment"] else " "}] Oof Moment (Lose a spin)
    [{ach_x if achievements["you_should_stop"] else " "}] You Should Stop (Lose a total of 1,000 credits)
    [{ach_x if achievements["you_should_REALLY_stop"] else " "}] You Should REALLY Stop (Lose a total of 10,000 credits)
    [{ach_x if achievements["you're_just_gonna_lose_more"] else " "}] You're Just Gonna Lose More (Lose a total of 100,000 credits)
    [{ach_x if achievements["rock_bottom"] else " "}] Rock Bottom (Lose a total of 1,000,000 credits)
    
    [{ach_x if achievements["confidence_is_key"] else " "}] Confidence is Key (Go all in on a spin)
    [{ach_x if achievements["i_can't_stop_winning"] else " "}] I Can't Stop Winning! (Win an all-in spin)
    [{ach_x if achievements["aw_dangit"] else " "}] Aw Dangit! (Lose an all-in spin)
    
    [{ach_x if achievements["at_least_i_still_have_clothes"] else " "}] At Least I Still Have Clothes (Take out a loan)
    [{ach_x if achievements["petty_cash"] else " "}] Petty Cash (Take out a loan less than or equal to 10 credits)
    [{ach_x if achievements["money_management"] else " "}] Money Management (Pay back a loan)
    [{ach_x if achievements["still_hanging_in_there"] else " "}] Still Hanging in There (Take out another loan) 
    [{ach_x if achievements["redemption_arc"] else " "}] Redemption Arc (Pay back three loans)

    [{ach_x if achievements["i_feel_funny"] else " "}] I Feel Funny (Buy from the bar)
    [{ach_x if achievements["big_spender"] else " "}] Big Spender (Spend 1,000 credits at the bar)
    [{ach_x if achievements["i'll_have_the_regular"] else " "}] I'll Have the Regular (Spend 10,000 credits at the bar)
    [{ach_x if achievements["writing_checks_left_and_right"] else " "}] Writing Checks Left and Right (Spend 100,000 credits at the bar)
    [{ach_x if achievements["overload"] else " "}] Overload (Max out on energy drinks)

    [{ach_x if achievements["insured"] else " "}] Insured (Purchase an insurance plan)
    [{ach_x if achievements["volatile"] else " "}] Volatile (Make your insurance rate rise)
    [{ach_x if achievements["the_bills_caught_up_to_you"] else " "}] The Bills Caught Up to You (Miss an insurance payment)

    [{ach_x if achievements["your_family_is_worried"] else " "}] Your Family is Worried (Spend 14 days gambling)
    [{ach_x if achievements["concerning_hygeine"] else " "}] Concerning Hygeine (Spend 50 days gambling)
    [{ach_x if achievements["what_year_is_it"] else " "}] What Year is It? (Spend 100 days gambling)""")

    if achievements["the_light_is_blinding"]:
        print(f"    [{Fore.MAGENTA}{Style.BRIGHT}x{Style.RESET_ALL}] The Light is {Fore.YELLOW}{Style.BRIGHT}Blinding{Style.RESET_ALL} (Leave the casino after 100 days)")

    b = 0 
    for i in bonus_achievements.keys():
        if bonus_achievements[i]:
            b += 1

    if b > 0:
        t = "?" if b < len(bonus_achievements) else len(bonus_achievements)
        if b == t:
            print(f"\nYou've unlocked [{Fore.GREEN}{b}/{t}{Style.RESET_ALL}] Bonus Achievements\n")    
        else:
            print(f"\nYou've unlocked [{b}/{t}] Bonus Achievements\n")

        if bonus_achievements["counting_cards"]:
            print(f"    [{Fore.CYAN}x{Style.RESET_ALL}] Counting Cards (Use the developer console, you nasty cheater)")
        if bonus_achievements["extra_zesty"]:
            print(f"    [{Fore.CYAN}x{Style.RESET_ALL}] Extra Zesty (See all flavor texts on the home screen)")
        if bonus_achievements["regular_patron"]:
            print(f"    [{Fore.CYAN}x{Style.RESET_ALL}] Regular Patron (See all Bartender dialogues)")
        if bonus_achievements["back_from_the_brink"]:
            print(f"    [{Fore.CYAN}x{Style.RESET_ALL}] Back from the Brink (Win 'The Deal')")
        if bonus_achievements["last_resort"]:
            print(f"    [{Fore.CYAN}x{Style.RESET_ALL}] Last Resort (Sell your kidney)")
        if bonus_achievements["shifty_business"]:
            print(f"    [{Fore.CYAN}x{Style.RESET_ALL}] Shifty Business (Buy a fake ID)")    


def get_variable_type(var):
    if isinstance(var, bool):
        return bool
    elif isinstance(var, int):
        return int
    elif isinstance(var, str):
        return str

    else:
        return type(var)


def devtools():
    global player_credits, console_used
    clear_screen()
    print("Welcome to the V.I.P. Club")
    while True:
        menu = input("\n>>> ")
        if menu == "variable":
            variable = input("Enter the variable name\n>> ")

            if variable not in globals():
                print(f"Variable '{variable}' not found")
                continue

            current_value = globals()[variable]
            _type = get_variable_type(current_value)

            menu = input(
                f"{variable} is currently set to {current_value}. Press {btn('enter')} to change it or 'cancel' to go back\n>> ")

            if menu.lower() == "cancel":
                continue

            if _type == int:
                while True:
                    try:
                        value = int(input("Enter an integer value\n>> "))
                        break
                    except ValueError:
                        print("Invalid input")
            elif _type == str:
                value = input("Enter a string value\n>> ")
            elif _type == bool:
                while True:
                    bool_input = input("Enter a boolean value\n>> ").lower()
                    if bool_input in ['true', '1', 'yes', 'y']:
                        value = True
                        break
                    if bool_input in ['false', '0', 'no', 'n']:
                        value = False
                        break
                    else:
                        print("Invalid input")
            else:
                break

            globals()[variable] = value
            print(f"{variable} is now set to {globals()[variable]}")
        if menu == "function":
            while True:
                try:
                    function = input("Enter the function name\n>> ")
                    exec(f"{function}()")
                    break
                except:
                    print(f"Function '{function}' not found")
                    break
        if menu == "completion":
            menu = input(f"Press {btn('enter')} to enable all achievements or 'cancel' to go back ")
            for i in achievements:
                achievements[i] = True
            for i in bonus_achievements:
                bonus_achievements[i] = True
        if menu == "achievement":
            while True:
                try:
                    achievement_name = input("Enter achievement name\n>> ")
                    menu = input(f"{achievement_name} is currently set to {achievements[achievement_name]}. Press {btn('enter')} to toggle it or 'cancel' to go back\n>> ")
                    if menu != "cancel":
                        if achievements[achievement_name]:
                            achievements[achievement_name] = False
                        elif not achievements[achievement_name]:
                            achievements[achievement_name] = True
                        print(
                            f"{achievement_name} is now set to {achievements[achievement_name]}")
                        break
                    else:
                        break
                except:
                    print(f"Achievement '{achievement_name}' not found")
                    break
        if menu == "bonus":
            while True:
                try:
                    achievement_name = input("Enter achievement name\n>> ")
                    menu = input(f"{achievement_name} is currently set to {bonus_achievements[achievement_name]}. Press {btn('enter')} to toggle it or 'cancel' to go back\n>> ")
                    if menu != "cancel":
                        if bonus_achievements[achievement_name]:
                            bonus_achievements[achievement_name] = False
                        elif not bonus_achievements[achievement_name]:
                            bonus_achievements[achievement_name] = True
                        print(
                            f"{achievement_name} is now set to {bonus_achievements[achievement_name]}")
                        break
                    else:
                        break
                except:
                    print(f"Achievement '{achievement_name}' not found")
                    break
        if menu == "jumpstart":
            player_credits = 1000000
            globals()["total_won"] = 50000
            globals()["luck"] = 1
            globals()["is_high_roller"] = True
        if menu == "dump":
            gl = globals()
            for g in gl.keys():
                if "__" in g or isinstance(gl[g], types.FunctionType) or isinstance(gl[g], types.ModuleType):
                    continue
                if len(g) <= 2:
                    continue
                if isinstance(gl[g], dict):
                    print(f"{g}: dictionary with {len(gl[g])} items")
                elif isinstance(gl[g], list):
                    print(f"{g}: list with {len(gl[g])} items")
                else:
                    print(f"{g}: {gl[g]}")
            
        if menu == "pass":
            clear_screen()
            break
    console_used = True
    if suppress:
        console_used = False


# Display the home screen
def display_home_screen():
    global insurance_payment
    while True:
        clear_screen()
        print(f"Credits: {Fore.YELLOW}{player_credits:,}{Style.RESET_ALL}")
        print("")
        print(("-" * 20))
        try:
            win_percentage = 100 * (wins / spins)
            print("\n" + Fore.GREEN + "Win%" + Style.RESET_ALL + ":               " + str(round(win_percentage, 2)) + "%")
        except ZeroDivisionError:
            print(f" \n{Fore.GREEN}Win%{Style.RESET_ALL}:               N/A")
        print(Fore.YELLOW + "Reward Multiplier" + Style.RESET_ALL + ": ", round(reward_multiplier, 2))
        print(Fore.MAGENTA + "Luck" + Style.RESET_ALL + ":              ", float(luck))
        print(Fore.CYAN + "Streak Multiplier" + Style.RESET_ALL + ": ", round(streak_multiplier, 1), "\n")
        print(("-" * 20))
        if has_insurance:
            if insurance_type == 1:
                plan = "Starter Plan"
            elif insurance_type == 2:
                plan = "Basic Plan"
            elif insurance_type == 3:
                plan = "Hobbyist Plan"
            elif insurance_type == 4:
                plan = "Gambler's Dream"

            if round(total_covered / 20) >= insurance_base:
                insurance_payment = round(total_covered / 20)

            print(
                f"\nInsurance Information:\n- Plan: {plan}\n- Payment: {insurance_payment:,} credits/day\n- Coverage: {insurance_coverage}%\n")
            print(("-" * 20))

        print(f"\n{pick_flavor_text()}\n")

        print(("-" * 20))

        if spins < 100:
            menu = input(
                f"\nType 'achievements' to view your achievements or press {btn('enter')} to spin\n>> ")

            if menu == "achievements":
                display_achievements()
                input(f"\nPress {btn('enter')} to continue\n")
            elif menu == cake:
                devtools()
            else:
                break
                return
        elif spins >= 100:
            menu_ = input(
                f"\nType 'achievements' to view your achievements, press {btn('enter')} to spin, or type '{Fore.GREEN}leave{Style.RESET_ALL}' to {Fore.GREEN}escape{Style.RESET_ALL}\n>> ")

            if menu_ == "achievements":
                display_achievements()
                input(f"\nPress {btn('enter')} to continue\n")
            elif menu_ == "thecakeisalie":
                devtools()
            elif menu_ == "leave":
                game_over(2)
                break
            else:
                break
                return


# Get random letters for spinning
def get_letters() -> list:
    a = letters[random.randint(0, 25)]
    b = a if random.randint(1, round(15 - luck / 2)
                            ) == 1 else letters[random.randint(0, 25)]
    if random.randint(1, 5) == 1:
        c = a if random.randint(1, round(15 - luck / 2)
                                ) == 1 else letters[random.randint(0, 25)]
    else:
        c = b if random.randint(1, round(15 - luck / 2)
                                ) == 1 else letters[random.randint(0, 25)]

        colora = a
        colorb = b
        colorc = c

    if (a + b + c).upper() in bonuses:
        colora = Fore.MAGENTA + a + Style.RESET_ALL
        colorb = Fore.MAGENTA + b + Style.RESET_ALL
        colorc = Fore.MAGENTA + c + Style.RESET_ALL

    print(f"""
    ===================
    |     |     |     |
    |  {colora}  |  {colorb}  |  {colorc}  |
    |     |     |     |
    ===================
    """)
    return [a, b, c]

# Calculate reward based on spin outcome and bet


def calculate_reward(spin: list, bet: int) -> int:
    global wins, streak, has_borrow
    double = False
    triple = False
    bonus = False
    reward = bet
    unique_letters = []

    for letter in spin:
        if letter not in unique_letters:
            unique_letters.append(letter)
        else:
            if spin.count(letter) == 3:
                triple = True
            else:
                double = True

    for bonus_word in bonuses:
        if f"{spin[0]}{spin[1]}{spin[2]}" == bonus_word:
            bonus = True

    if has_borrow:
        bonus = True

    if double:
        reward *= 2
        wins += 1
        streak += 1
    elif triple:
        reward *= 4
        wins += 1
        streak += 1
    if bonus:
        reward *= 4
        wins += 1
        streak += 1
    if not double and not triple and not bonus:
        reward = 0
        streak = 0

    if streak > 1:
        return int(reward * reward_multiplier * (streak * streak_multiplier))
    else:
        return int(reward * reward_multiplier)


# handle the insurance shop
def insurance_shop():
    global has_insurance, insurance_coverage, insurance_payment, insurance_type, player_credits, insurance_base
    clear_screen()
    print(
        f"""
Welcome to the {Fore.YELLOW}Gambler's Insurance{Style.RESET_ALL} Shop!

Credits: {Fore.YELLOW}{player_credits:,}{Style.RESET_ALL}

Here are our plans:
    [{ach_x if insurance_type == 0 else " "}] No Plan
    [{ach_x if insurance_type == 1 else " "}] Starter Plan (Starts at {Fore.YELLOW}5{Style.RESET_ALL} credits/day, {Fore.GREEN}5%{Style.RESET_ALL} coverage)
    [{ach_x if insurance_type == 2 else " "}] Basic Plan (Starts at {Fore.YELLOW}10{Style.RESET_ALL} credits/day, {Fore.GREEN}10%{Style.RESET_ALL} coverage)
    [{ach_x if insurance_type == 3 else " "}] Hobbyist Plan (Starts at {Fore.YELLOW}50{Style.RESET_ALL} credits/day, {Fore.GREEN}25%{Style.RESET_ALL} coverage)
    [{ach_x if insurance_type == 4 else " "}] Gambler's Dream (Starts at {Fore.YELLOW}250{Style.RESET_ALL} credits/day, {Fore.GREEN}50%{Style.RESET_ALL} coverage)

NOTE: All plans require a down payment equal to {Fore.YELLOW}10 times their starting rate{Style.RESET_ALL}
      Rate increases based on how much your insurance has covered
        """
    )
    while True:
        option = input(f"Choose a plan or type '{Style.DIM}pass{Style.RESET_ALL}' to leave\n>> ").lower()
        if option == "pass":
            return
        elif option == "no plan":
            has_insurance = False
            insurance_type = 0
            insurance_payment = 0
            insurance_coverage = 0
            break
        elif option == "starter plan" or option == "starter":
            if player_credits <= 50:
                print(f"{Fore.RED}You can't afford that plan!{Style.RESET_ALL}")
                continue
            has_insurance = True
            insurance_type = 1
            insurance_payment = 5
            insurance_coverage = 5
            player_credits -= 50
            break
        elif option == "basic plan" or option == "basic":
            if player_credits <= 100:
                print(f"{Fore.RED}You can't afford that plan!{Style.RESET_ALL}")
                continue
            has_insurance = True
            insurance_type = 2
            insurance_payment = 10
            insurance_coverage = 10
            player_credits -= 100
            break
        elif option == "hobbyist plan" or option == "hobbyist":
            if player_credits <= 500:
                print(f"{Fore.RED}You can't afford that plan!{Style.RESET_ALL}")
                continue
            has_insurance = True
            insurance_type = 3
            insurance_payment = 50
            insurance_coverage = 25
            player_credits -= 500
            break
        elif option == "gambler's dream" or option == "gambler's" or option == "gambler":
            if player_credits <= 2500:
                print(f"{Fore.RED}You can't afford that plan!{Style.RESET_ALL}")
                continue
            has_insurance = True
            insurance_type = 4
            insurance_payment = 250
            insurance_coverage = 50
            player_credits -= 2500
            break

    insurance_base = insurance_payment
    print(f"\nThank you for your business!\n\n{btn('enter')} to continue")
    input("")

def roulette_spin():
    color = "none"
    number = str(random.randint(0, 37))
    if number == "37":
        number = "00"
    if int(number) % 2 == 0:
        color = "red"
    if number == "0" or number == "00":
        color = "green"
    else:
        color = "black"
    return color, number
    

def get_roulette_reward(bet_type, x, bet_amount, color, number):
    # Roulette Wheel
    dozen_one = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    dozen_two = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
    dozen_three = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]

    column_one = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
    column_two = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
    column_three = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]

    low = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    high = [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]

    reds = [1, 3, 5, 7, 9, 12, 14, 16, 18, 21, 23, 25, 27, 28, 30, 32, 34, 36]  
    blacks = [a if a not in reds else None for a in range(1, 37)]

    
    if bet_type == "single":
        if bet_amount == int(number):
            return bet_amount * 35 + bet_amount
        else:
            return 0
    if bet_type == "column":
        if int(number) in x:
            return (bet_amount * 2) + bet_amount
        else:
            return 0
    if bet_type == "dozen":
        if int(number) in x:
            return bet_amount * 2 + bet_amount
        else:
            return 0
    if bet_type == "red":
        if int(number) in reds:
            return bet_amount * 2
        else:
            return 0
    if bet_type == "black":
        if int(number) in blacks:
            return bet_amount * 2
        else:
            return 0
    if bet_type == "low":
        if int(number) in low:
            return bet_amount * 2
        else:
            return 0
    if bet_type == "high":
        if int(number) in high:
            return bet_amount * 2
        else:
            return 0
    if bet_type == "odd":
        if int(number) % 2 != 0:
            return bet_amount * 2
        else:
            return 0
    if bet_type == "even":
        if int(number) % 2 == 0:
            return bet_amount * 2
        else:
            return 0

def play_roulette():
    global roulette_chips
    # Roulette Wheel
    dozen_one = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    dozen_two = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
    dozen_three = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]

    column_one = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
    column_two = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
    column_three = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]

    low = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    high = [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]

    reds = [1, 3, 5, 7, 9, 12, 14, 16, 18, 21, 23, 25, 27, 28, 30, 32, 34, 36]  
    blacks = [a if a not in reds else None for a in range(1, 37)]

    while True:
        clear_screen()
        print(f"""
Chips: {roulette_chips}

Bet on a category of numbers.
A number from 1 to 36 (plus 0 and 00) is chosen
If your category is chosen, you win!

- [[Bet Types]] -
Odd             (Odd numbers)
Even            (Even numbers)
Black           (Black numbers)
Red             (Red numbers)
Low             (1-18)
High            (19-36)
Column One      (1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34)
Column Two      (2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35)
Column Three    (3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36)
Dozen One       (1-12)
Dozen Two       (13-24)
Dozen Three     (25-36)
""")
        bet_type = input("\nBet Type: ").lower()
        if bet_type == "column one":
            x = column_one
        if bet_type == "column two":
            x = column_two
        if bet_type == "column three":
            x = column_three
        if bet_type == "dozen one":
            x = dozen_one
        if bet_type == "dozen two":
            x = dozen_two
        if bet_type == "dozen three":
            x = dozen_three
        if bet_type == "low":
            x = low
        if bet_type == "high":
            x = high
        if bet_type == "red":
            x = reds
        if bet_type == "black":
            x = blacks
        if bet_type == "odd":
            x = [a if a % 2 != 0 else None for a in range(1, 37)]
        if bet_type == "even":
            x = [a if a % 2 == 0 else None for a in range(1, 37)]

        while True:
            bet_amount = int(input("Bet Amount: "))

            if bet_amount <= 0 or bet_amount > roulette_chips:
                print("Enter a non-zero number of chips that you can afford.")
            else:
                break
            
        roulette_chips -= bet_amount

        clear_screen()

        color, number = roulette_spin()
        c = f"{Style.DIM}{Fore.BLACK}" if color == "black" else f"{Style.BRIGHT}{Fore.RED}"
        print("Spin: " + c + color.title() + " " + number + Style.RESET_ALL)

        reward = get_roulette_reward(bet_type, x, bet_amount, color, number)
        roulette_chips += reward

        print(Fore.GREEN + "Reward: " + str(reward) + Style.RESET_ALL)
        print(Fore.YELLOW + "Chips: " + str(roulette_chips) + Style.RESET_ALL)

        menu = input(f"'leave' to leave or {btn('enter')} to continue")

        clear_screen()

        if menu == "leave":
            clear_screen()
            break

        if roulette_chips <= 0:
            clear_screen()
            print(f"{Fore.RED}You have run out of roulette chips.{Style.RESET_ALL}")
            break


def high_rollers():
    global player_credits, is_high_roller, luck, roulette_chips

    clear_screen()

    if not is_high_roller:
        print(f"You don't have a {Fore.CYAN}membership card{Style.RESET_ALL}. \nThe bouncer {Fore.RED}turns you away{Style.RESET_ALL}.")
        input(f"\n{btn('enter')} to continue\n")
        return

    while True:
        clear_screen()
        print(f"Welcome to the {Fore.MAGENTA}High Rollers club!{Style.RESET_ALL}")
        print(f"You have {roulette_chips} chips")
        menu = input(f"\ntype 'chips' to buy more chips, 'credits' to cash in chips, 'spin' to play roulette, or '{Style.DIM}pass{Style.RESET_ALL}' to leave\n>> ")
        if menu == "chips":
            clear_screen()
            print(f"Credits: {Fore.YELLOW}{player_credits:,}{Style.RESET_ALL}")
            print("Exchange rate: 1 Chip for 5 Credits")
            while True:
                amount = input(f"Enter a number of chips to buy or '{Style.DIM}pass{Style.RESET_ALL}' to leave\n>> ")
                if amount == "pass" or (amount.isnumeric() and int(amount) > 0):
                    pass
                else:
                    print(f"Enter a non-zero numeric value or '{Style.DIM}pass{Style.RESET_ALL}'")
                    continue
                
                if amount == "pass": 
                    break
                else:
                    amount = round(int(amount))
                    if amount * 5 > player_credits:
                        print(f"{Fore.RED}You can't afford that many chips!{Style.RESET_ALL}")
                        continue
                    else:
                        player_credits -= amount * 5
                        roulette_chips += amount
        elif menu == "spin":
            clear_screen()
            play_roulette()
        elif menu == "credits":
            clear_screen()
            print(f"You have {roulette_chips} chips")
            while True:
                amount = input(f"Enter a number of chips to cash in or '{Style.DIM}pass{Style.RESET_ALL}' to leave\n>> ")
                if amount == "pass" or (amount.isnumeric() and int(amount) > 0):
                    pass
                else:
                    print(f"Enter a non-zero numeric value or '{Style.DIM}pass{Style.RESET_ALL}'")
                    continue
                if amount == "pass": break
                else:
                    amount = round(int(amount))
                    if amount > roulette_chips:
                        print(f"{Fore.RED}You can't afford that many chips!{Style.RESET_ALL}")
                        continue
                    else:
                        player_credits += round(amount / 5)
                        roulette_chips -= amount
        elif menu == "pass":
            break

# Handle the in-game shop for upgrades
def visit_shop():
    global reward_multiplier, luck, luck_upgrade_price, reward_upgrade_price, streak_multiplier, streak_upgrade_price, player_credits, speed_upgrade_price, speed_upgrades, total_spent_in_shop, achievements, bonus_achievements, bar_actions, bar_dialogue, bar_dialogue_count
    clear_screen()

    s = player_credits

    print("Welcome to the bar!")
    dialogue = random.randint(0,5)
    if dialogue == 0:
        print(f"{bar_actions[0]}{bar_dialogue[bar_dialogue_count]}")
        bar_dialogue_count += 1
        if bar_dialogue_count == len(bar_dialogue):
            bonus_achievements["regular_patron"] = True
            bar_dialogue_count = 0
    else:
        print(bar_actions[dialogue])

    print(f"\nCredits: {Fore.YELLOW}{player_credits:,}{Style.RESET_ALL}")
    print(f"""
    -- MENU --
    Beer: +{Fore.YELLOW}5% Reward Multiplier{Style.RESET_ALL} (Cost: {Fore.YELLOW}{reward_upgrade_price}{Style.RESET_ALL})
    Fries: +{Fore.MAGENTA}0.5 Luck{Style.RESET_ALL} (Cost: {Fore.YELLOW}{luck_upgrade_price}{Style.RESET_ALL})
    Hot Dog: +{Fore.CYAN}0.1 Streak Multiplier{Style.RESET_ALL} (Cost: {Fore.YELLOW}{streak_upgrade_price}{Style.RESET_ALL})
    Energy Drink: -{Fore.GREEN}1s Wheel Spin Time{Style.RESET_ALL} [{f"{Fore.GREEN}{Style.BRIGHT}" if speed_upgrades >= 5 else ""}{speed_upgrades if speed_upgrades < 5 else 5}/5{Style.RESET_ALL}] (Cost: {Fore.YELLOW}{speed_upgrade_price}{Style.RESET_ALL})
    """)
    print(f"Type 'buy <item name>' to buy an item or '{Style.DIM}pass{Style.RESET_ALL}' to leave")
    while True:
        in_ = input(">> ")
        if in_ == "pass":
            return
        purchase = in_[4:].lower()
        if purchase == "beer":
            if reward_upgrade_price > player_credits:
                print(f"{Fore.RED}You can't afford that!{Style.RESET_ALL}")
                continue
            else:
                player_credits -= reward_upgrade_price
                reward_multiplier += 0.1
                reward_upgrade_price = round(1.5*reward_upgrade_price)
                break
        if purchase == "fries":
            if luck_upgrade_price > player_credits:
                print(f"{Fore.RED}You can't afford that!{Style.RESET_ALL}")
                continue
            else:
                player_credits -= luck_upgrade_price
                luck += 0.5
                luck_upgrade_price = round(1.5*luck_upgrade_price)
                break
        if purchase == "hot dog":
            if streak_upgrade_price > player_credits:
                print(f"{Fore.RED}You can't afford that!{Style.RESET_ALL}")
                continue
            else:
                player_credits -= streak_upgrade_price
                streak_multiplier += 0.1
                streak_upgrade_price = round(1.5*streak_upgrade_price)
                break
        if purchase == "energy drink":
            if speed_upgrade_price > player_credits:
                print(f"{Fore.RED}You can't afford that!{Style.RESET_ALL}")
                continue
            elif speed_upgrades > 3:
                print(f"{Fore.GREEN}You can't upgrade this stat anymore!{Style.RESET_ALL}")
                achievements["overload"] = True
                continue
            else:
                player_credits -= speed_upgrade_price
                speed_upgrade_price = round(1.5*speed_upgrade_price)
                speed_upgrades += 1
                break
    total_spent_in_shop = (s - player_credits)
    if purchase in ["beer", "fries", "hot dog", "energy drink"] and kidneys == 1:
        game_over(4)

def black_market():
    global player_credits, fake_id, bonus_achievements
    if not fake_id:
        clear_screen()
        print(f"You notice a {Fore.CYAN}strange man{Style.RESET_ALL} hunched in a corner. He's {Fore.GREEN}waving{Style.RESET_ALL} at you.")
        choice = input(f"Approach him? ({Fore.GREEN}y{Style.RESET_ALL}/{Fore.RED}n{Style.RESET_ALL})\n>> ")
        if choice.lower() in ["y", "yes"]:
            print(f"As you get closer, he pulls a {Fore.CYAN}card{Style.RESET_ALL} out of his jacket and shows it to you. It's a {Fore.GREEN}fake ID{Style.RESET_ALL}.")
            print(f"""
{Back.WHITE}{Fore.BLACK}——————————————————————————————————————————————{Style.RESET_ALL}
{Back.WHITE}{Fore.BLACK}|    /--\     |                              |{Style.RESET_ALL}
{Back.WHITE}{Fore.BLACK}|    \__/     |  NAME: JOHN SMITH            |{Style.RESET_ALL}
{Back.WHITE}{Fore.BLACK}|  _/    \_   |  D.O.B: 9/11/01              |{Style.RESET_ALL}
{Back.WHITE}{Fore.BLACK}|   |    |    |  SEX: M                      |{Style.RESET_ALL}
{Back.WHITE}{Fore.BLACK}|——————————————                              |{Style.RESET_ALL}
{Back.WHITE}{Fore.BLACK}| ID: 841238800856874                        |{Style.RESET_ALL}
{Back.WHITE}{Fore.BLACK}| EYES: BRO                                  |{Style.RESET_ALL}
{Back.WHITE}{Fore.BLACK}| RACE: W                                    |{Style.RESET_ALL}
{Back.WHITE}{Fore.BLACK}| HEIGHT: 7' 25"                             |{Style.RESET_ALL}
{Back.WHITE}{Fore.BLACK}——————————————————————————————————————————————{Style.RESET_ALL}
            """)
            print(f"He says he'll {Fore.GREEN}sell it to you{Style.RESET_ALL} for the low, low price of {Fore.YELLOW}50,000 credits{Style.RESET_ALL}. Hand him the money? ({Fore.GREEN}y{Style.RESET_ALL}/{Fore.RED}n{Style.RESET_ALL})")
            choice = input(">> ")
            if choice.lower() in ["y", "yes"]:
                if player_credits >= 50000:
                    print(f"You hand over the credits and {Fore.YELLOW}recieve the card{Style.RESET_ALL} in return.")
                    fake_id = True
                    player_credits -= 50000
                    bonus_achievements["shifty_business"] = True
                else:
                    print(f"You want it, but you {Fore.RED}don't have enough money{Style.RESET_ALL}.")
            else:
                print("You back away without a word.")
        else:
            print("You carry on without stopping.")
            pass

    if random.randint(1, 2) == 2: # rolls a chance every visit
        n = random.randint(100, 200)
        if n >= player_credits: n = player_credits - 1
        player_credits -= n
        print(f"As you leave, you notice your wallet {Fore.RED}feels {n} credits lighter{Style.RESET_ALL} than it did a minute ago...")

# visit the in-game bank
def visit_bank():
    global player_credits, loan_amount, loan_payment, has_loan, interest_percent, achievements, loans_total, loans_paid, luck
    clear_screen()
    if not has_loan:
        while True:
            clear_screen()
            print(f"Credits: {Fore.YELLOW}{player_credits:,}{Style.RESET_ALL}")
            print(f"Welcome to {Fore.BLUE}World Liberty Financial{Style.RESET_ALL}!\nType 'loan <amount>' for a loan")
            in_ = input(">> ")
            if len(in_.split(" ")) == 1:
                continue
            if in_.split(" ")[0] == "loan":
                amount = int(in_.split(" ")[1])
                loan_amount = amount

                arrest_chance = (-1 * (3.874 * (10 ** -11))*(loan_amount ** 2)) + (0.0001111 * loan_amount) + 18.87
                arrest_chance -= 4(luck)

                arrest_chance = int(arrest_chance)

                if loan_amount >= 1434167:
                    arrest_chance = 99

                if fake_id and random.randint(0,100) <= arrest_chance:
                    game_over(5)
                else:
                    achievements["at_least_i_still_have_clothes"] = True
                    if loan_amount <= 10:
                        achievements["petty_cash"] = True
                    player_credits += amount
                    if len(str(amount)) < 8:
                        interest_percent = 0.05
                    else:
                        interest_percent = 0.05 + ((len(str(amount)) - 7) * 0.05)
                    days_passed = 0
                    loan_payment = amount
                    has_loan = True

                    loans_total += 1
                    if loans_total >= 2:
                        achievements["still_hanging_in_there"] = True

                    print(f"You took out a loan of {Fore.YELLOW}{amount:,}{Style.RESET_ALL} credits.")
                    if not fake_id:
                        print(f"Be prepared to pay it back in {Fore.YELLOW}three{Style.RESET_ALL} days.")
                    input(f"\nPress {btn('enter')} to continue\n")
                    return
    else:
        if fake_id:
            return
        else:
            print(
                f"Time to pay your loan back.\nYour loan payment is {Fore.YELLOW}{loan_payment:,}{Style.RESET_ALL} credits")
            print("Credits:", player_credits)
            input(f"\nPress {btn('enter')} to continue\n")
            if player_credits > loan_payment:
                player_credits -= loan_payment
                loans_paid += 1
                has_loan = False
                achievements["money_management"] = True
                if loans_paid == 3:
                    achievements["redemption_arc"] = True
                return
            else:
                loan_payment -= player_credits
                player_credits = 0


def sell_kidney():
    global kidneys, player_credits, spins
    kidney_value = 75000 + random.randint(-2000,2000)
    if random.randint(1,2) == 1:
        kidney = "right"
    else:
        kidney = "left"
    days_out = random.randint(5,10)
    for i in range(days_out):
        clear_screen()
        print(f"You decide to {Fore.GREEN}sell your {kidney} kidney{Style.RESET_ALL} to continue gambling.")
        print(f"You manage to get {Fore.YELLOW}{kidney_value:,}{Style.RESET_ALL} credits for it.")
        print(f"After {Fore.RED}{i} days in the hospital{Style.RESET_ALL}, you're back on your feet, itching for more {Fore.GREEN}gambling{Style.RESET_ALL}.")    
        time.sleep((random.randint(10,20))/10)
    input(f"Press {btn('enter')} to continue.\n")

    
    spins += days_out
    player_credits += kidney_value
    kidneys = 1
    bonus_achievements["last_resort"] = True


def borrow_from_spouse():
    global has_borrowed, has_borrow, player_credits
    clear_screen()
    borrow_amount = (spins * 1000)
    if spouse == "husband":
        print(
            f"You {Fore.RED}break away from the machine{Style.RESET_ALL} to call your husband. He says that he'll let you have {Fore.YELLOW}{borrow_amount:,}{Style.RESET_ALL} credits, but if you lose with them he'll {Fore.RED}leave you{Style.RESET_ALL}. Take his {Fore.YELLOW}deal{Style.RESET_ALL}?")
    if spouse == "wife":
        print(
            f"You {Fore.RED}break away from the machine{Style.RESET_ALL} to call your wife. She says that she'll let you have {Fore.YELLOW}{borrow_amount:,}{Style.RESET_ALL} credits, but if you lose with them she'll {Fore.RED}leave you{Style.RESET_ALL}. Take her {Fore.YELLOW}deal{Style.RESET_ALL}?")

    option = input(f"({Fore.GREEN}y{Style.RESET_ALL}/{Fore.RED}n{Style.RESET_ALL}) >> ")

    if option.lower() in ["", "y"]:
        if spouse == "husband":
            print(f"You take his {Fore.YELLOW}money{Style.RESET_ALL}, determined to {Fore.GREEN}win it all{Style.RESET_ALL}.")
        if spouse == "wife":
            print(f"You take her {Fore.YELLOW}money{Style.RESET_ALL}, determined to {Fore.GREEN}win it all{Style.RESET_ALL}.")
        has_borrow = True
        player_credits = borrow_amount
        return
    else:
        print(f"You {Fore.RED}hang up{Style.RESET_ALL} and decide to go to the bank instead.")
        has_borrowed = True
        visit_bank()


def game_over(source):
    global spins, spouse, achievements
    clear_screen()
    # end text conditions

    if spins != 1:
        s = "s"
    else:
        s = ""

    print(f"After {spins} day{s}...")

    if spouse == "wife":
        end_text_0 = f"\n{Fore.RED}You are broke :(\nYou lost your house\nYou lost your wife\nShe took the kids\n\n\nWas it worth it?{Style.RESET_ALL}"
        end_text_1 = f"\n{Fore.GREEN}You made it out!\nYour wife is waiting outside for you.\nShe hugs you and says, \"I'm glad you're back.\"{Style.RESET_ALL}"
        end_text_2 = f"\n{Fore.GREEN}You made it out!\nYour wife is waiting outside for you.\n{Fore.RED}She hands you a stack of papers\nShe says, \"I want a divorce.\"{Style.RESET_ALL}"
        end_text_3 = f"\n{Fore.RED}You lost the money your wife gave you! She calls, but you're too ashamed to pick up. You know it's over.{Style.RESET_ALL}"
    if spouse == "husband":
        end_text_0 = f"\n{Fore.RED}You are broke :(\nYou lost your house\nYou lost your husband\nHe took the kids\n\n\nWas it worth it?{Style.RESET_ALL}"
        end_text_1 = f"\n{Fore.GREEN}You made it out!\nYour husband is waiting outside for you.\nHe hugs you and says, \"I'm glad you're back.\"{Style.RESET_ALL}"
        end_text_2 = f"\n{Fore.GREEN}You made it out!\nYour husband is waiting outside for you.\n{Fore.RED}He hands you a stack of papers\nHe says, \"I want a divorce.\"{Style.RESET_ALL}"
        end_text_3 = f"\n{Fore.RED}You lost the money your husband gave you! He calls, but you're too ashamed to pick up. You know it's over.{Style.RESET_ALL}"
    end_text_4 = f"{Fore.RED}Unfortunately, your reduced number of kidneys couldn't handle your diet, and you have perished.{Style.RESET_ALL}"
    end_text_5 = f"{Fore.RED}Unfortunately, you got caught with a fake ID. You've been arrested and have no one to pay your bail. Guess that's it for you.{Style.RESET_ALL}"
    if source == 0:  # bankruptcy
        print(end_text_0)
    elif source == 1:  # loan payment
        print(f"{Fore.RED}You missed your loan payment by {Fore.YELLOW}{loan_payment:,}{Fore.RED} credits{Style.RESET_ALL}")
        print(end_text_0)
    elif source == 2:  # ESCAPE
        achievements["the_light_is_blinding"] = True
        calculate_achievements()

        a = 0
        for i in achievements.keys():
            if achievements[i]:
                a += 1
        try:
            # calculate percent of achievements
            p = round((100 * (a / len(achievements))))
        except ZeroDivisionError:
            p = 0

        if p >= 100:
            print(end_text_1)
        if p < 100:
            print(end_text_2)
    elif source == 3:  # Failed the deal
        print(end_text_3)
    elif source == 4: #kidney
        print(end_text_4)
    elif source == 5: #ID 
        print(end_text_5)

    display_achievements()
    while True:
        time.sleep(1)


clear_screen()
if IS_DEV_BUILD:
    print(f"Welcome to {Fore.CYAN}Gambling Simulator{Style.RESET_ALL} {Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}dev-1.12!{Style.RESET_ALL}\nThis is a developer build and may be {Fore.RED}unfinished or broken.{Style.RESET_ALL}\n\nPress {btn('enter')} to continue")
else:
    print(f"Welcome to {Fore.CYAN}Gambling Simulator{Style.RESET_ALL} {Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}v1.12!{Style.RESET_ALL}\n\nPress {btn('enter')} to continue")
input("")

try:
    while is_running:
        achievements_start = {}
        bonus_achievements_start = {}

        for i in achievements.keys():
            achievements_start.update({i: achievements[i]})
        for i in bonus_achievements.keys():
            bonus_achievements_start.update({i: bonus_achievements[i]})

        a_before = 0
        for i in achievements.keys():
            if achievements[i]:
                a_before += 1

        b_before = 0
        for i in bonus_achievements.keys():
            if bonus_achievements[i]:
                b_before += 1
        
        clear_screen()
        if player_credits < 0:
            player_credits = 0
        if has_loan:
            loan_payment += round((loan_payment * interest_percent))
            if days_passed == 3:
                print("You need to pay back your loan!")
                print(f"Your loan payment is: {Style.BRIGHT}{Fore.RED}{loan_payment:,}{Style.RESET_ALL} credits")
                print(f"Credits: {Fore.YELLOW}{player_credits:,}{Style.RESET_ALL}")
            if days_passed == 4:
                visit_bank()
            days_passed += 1
        if player_credits <= 0:
            if not has_loan:
                print(f"You have no credits. Choose an option:")
                print("    'bank' to visit the bank")
                if not has_borrowed and spins >= 10:
                    print(f"    'borrow' to borrow from your {spouse}")
                if kidneys == 2 and spins >= 50:
                    print("    'kidney' to sell a kidney")
                option = input(">> ")
                if option == "bank":
                    visit_bank()
                elif not has_borrowed and spins >= 10:
                    if option == "borrow":
                        borrow_from_spouse()
                elif kidneys == 2 and spins >= 50:
                    if option == "kidney":
                        sell_kidney()
                else:
                    game_over(0)
            else:
                clear_screen()
                if has_loan and days_passed > 3:
                    game_over(1)
        display_home_screen()
        if player_credits < 0:
            player_credits = 0
        clear_screen()
        bet = 0

        if has_borrow:
            bet = player_credits
            achievements["confidence_is_key"] = True
        else:
            while bet < 1 or not isinstance(bet, int) or bet > player_credits:
                try:
                    print(f"Credits: {Fore.YELLOW}{player_credits:,}{Style.RESET_ALL}")
                    bet = int(input(f"Bet: {Fore.YELLOW}"))
                    print(Style.RESET_ALL)
                    if bet > player_credits:
                        print(f"{Fore.RED}You don't have enough money for that.{Style.RESET_ALL}")
                    elif bet == player_credits:
                        achievements["confidence_is_key"] = True
                    elif bet == 0:
                        print("Bet must be a non-zero whole number")
                except ValueError:
                    print("Bet must be a non-zero whole number")

        clear_screen()

        print("Spinning...")
        
        if kidneys == 1:
            time.sleep(6 - speed_upgrades)
        else:
            time.sleep(5 - speed_upgrades)

        spin_result = get_letters()
        spins += 1
        reward = calculate_reward(spin_result, bet)

        if reward > 0:
            if has_borrow:
                bonus_achievements["back_from_the_brink"] = True
                has_borrow = False
                has_borrowed = True
            print(f"{Fore.GREEN}Reward: {reward}{Style.RESET_ALL}")
            if bet == player_credits:
                achievements["i_can't_stop_winning"] = True
            total_won += reward
        else:
            print(f"{Fore.RED}You Lost!{Style.RESET_ALL}")
            if bet == player_credits:
                achievements["aw_dangit"] = True
            if has_borrow:
                loss = bet
                total_lost += loss
                game_over(3)
            if has_insurance:
                covered = int(round(((0.01) * insurance_coverage) * bet))
                if covered <= 1:
                    covered = 1
                total_covered += covered
                print(f"Thankfully, your {Fore.GREEN}insurance{Style.RESET_ALL} covered " +
                    f"{Fore.YELLOW}{covered:,}{Style.RESET_ALL}" + " credit" + ("s" if covered > 1 else "") + ".")
                loss = int(bet - covered)
            else:
                loss = bet
            total_lost += loss

            player_credits -= loss


        if has_insurance:
            player_credits -= insurance_payment
            if player_credits < 0:
                player_credits = 0
                achievements["the_bills_caught_up_to_you"] = True

        player_credits += reward

        if player_credits < 0:
            player_credits = 0

        print(f"\nPress {btn('enter')} to continue")
        input("")

        clear_screen()

        calculate_achievements()

        has_unlocked_achievement = False
        a = 0
        for i in achievements.keys():
            if achievements[i]:
                a += 1

        if a > a_before:
            has_unlocked_achievement = True

        # BONUS Achievements
        has_unlocked_bonus_achievement = False
        b = 0
        for i in bonus_achievements.keys():
            if bonus_achievements[i]:
                b += 1

        if b > b_before:
            has_unlocked_bonus_achievement = True

        if has_unlocked_achievement or has_unlocked_bonus_achievement:
            if has_unlocked_achievement:
                # find newly unlocked achievements
                a = []
                for i in achievements.keys():
                    if (achievements[i]) != (achievements_start[i]):
                        a.append(i)

                # display achievements
                if a != []:
                    for i in a:
                        no_spaces = i.replace("_", " ")
                        l = []
                        name = ""
                        for i in no_spaces.split():
                            i.capitalize()
                            l.append(i)
                        for i in l:
                            name += f"{i.capitalize()} "
                        print(f"{Fore.MAGENTA}Achievement Unlocked: {name}{Style.RESET_ALL}")
            if has_unlocked_bonus_achievement:
                # find newly unlocked achievements
                b = []
                for i in bonus_achievements.keys():
                    if (bonus_achievements[i]) != (bonus_achievements_start[i]):
                        b.append(i)

                # display achievements
                if b != []:
                    for i in b:
                        no_spaces = i.replace("_", " ")
                        l = []
                        name = ""
                        for i in no_spaces.split():
                            i.capitalize()
                            l.append(i)
                        for i in l:
                            name += f"{i.capitalize()} "
                        print(f"{Fore.CYAN}Bonus Achievement Unlocked: {name}{Style.RESET_ALL}")

            input(f"\n{btn('enter')} to continue\n")

        if total_won >= 50000 and not is_high_roller:
                is_high_roller = True
                clear_screen()
                print(f"You can now visit the {Fore.MAGENTA}High Rollers club!{Style.RESET_ALL}")
                input(f"\n{btn('enter')} to continue\n")

        if player_credits <= 0:
            pass
        else:
            while True:
                clear_screen()
                if spins >= 25 and not fake_id and random.randint(1,4) == 3:
                    black_market()
                if not is_high_roller:
                    print(f"Type 'shop' to visit the shop, 'insurance' to buy insurance, or '{Style.DIM}pass{Style.RESET_ALL}' to leave")
                else:
                    print(f"Type 'shop' to visit the shop, 'insurance' to buy insurance, 'high roller' to visit the High Rollers club, or '{Style.DIM}pass{Style.RESET_ALL}' to leave")
                in_ = input(">> ")
                if in_ == "shop":
                    visit_shop()
                    break
                if in_ == "insurance":
                    insurance_shop()
                    break
                if in_ == "high roller":
                    high_rollers()
                if in_ == "pass":
                    break

        try:
            del no_spaces, name, in_
        except:
            pass
        clear_screen()
except Exception as e:
    print(f"The developers are idiots. Report this in a strongly worded email to {Fore.MAGENTA}chloe@tobark.org{Style.RESET_ALL}:\n{e}")