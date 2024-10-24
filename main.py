import random
import time
import os

# Debug
IS_DEV_BUILD = False
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
borrow_amount = 3

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

    "overload": False,  # max out energy drinks #
    "i_feel_funny": False,  # first shop purchase #
    "big_spender": False,  # spend 1,000 credits in the shop #
    "i'll_have_the_regular": False,  # spend 10,000 credits in the shop #
    "writing_checks_left_and_right": False,  # spend 100,000 credits in the shop #

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
    "regular_patron": False  # have every conversation with the bartender #
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
    {"days_start": 0, "days_end": 1, "text": "You can practically taste your winnings already.", "displayed": False},
    {"days_start": 2, "days_end": 5, "text": "You haven't been here very long, but you feel like you could stay forever.", "displayed": False},
    {"days_start": 6, "days_end": 9, "text": "You begin to notice a regular deposit of crumbs at your machine. Are they yours?", "displayed": False},
    {"days_start": 10, "days_end": 14, "text": "The handle on the machine is getting greasy. You should wash your hands.", "displayed": False},
    {"days_start": 15, "days_end": 19, "text": "Your back is weary of hunching over the machine. Taking a walk might help.", "displayed": False},
    {"days_start": 20, "days_end": 24, "text": "You haven't seen the sun in quite a while.", "displayed": False},
    {"days_start": 25, "days_end": 54, "text": "Are you satisfied yet?", "displayed": False},
    {"days_start": 55, "days_end": 94, "text": "Your committment would be inspiring, were it not an addiction.", "displayed": False},
    {"days_start": 95, "days_end": 100, "text": "Is the casino still real?", "displayed": False}
]

bar_dialogue = [
    '"Hey there, care for a drink?"',
    '"How are the winnings?"',
    '"Good day, huh?"',
    '"Business is slow today. Take a look."',
    '"What\'s new?"',
    '"Every day\'s a good day to get drunk."',
    '"How\'re the kids?"',
    '"My husband says I need to get a real job."',
    '"Rough day, huh?"',
    '"Here, have a beer on me."',
    '"Kids these days..."',
    '"Went to college for physics, why am I here?"',
    '"Everyone leaves eventually. Will you?"'
]

bar_actions = [
    "The bartender looks up and says, ",
    "The bartender doesn't look up when you enter.",
    "The bartender seems engrossed in cleaning a glass. He doesn't appear to notice you.",
    "The bartender is wiping down the counter - the room smells vaguely of cleaning chemicals and vomit.",
    "The bartender isn't in. There's a sign that says: \"Leave the money on the counter. Help yourself.\"",
    "The bartender isn't in. There's a woman at the counter who eyes you with an emotion you can't decipher."
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

    print(f"""
You've Unlocked [{a}/{len(achievements)}] Achievements ({p}%) {"(Cheats used)" if console_used else ""}
    
    [{"x" if achievements["getting_somewhere"] else " "}] Getting Somewhere (Win a spin)
    [{"x" if achievements["on_a_roll"] else " "}] On a Roll (Win a total of 1,000 credits)
    [{"x" if achievements["a_decent_sum"] else " "}] A Decent Sum (Win a total of 10,000 credits)
    [{"x" if achievements["rolling_in_dough"] else " "}] Rolling in Dough (Win a total of 100,000 credits)
    [{"x" if achievements["millionaire"] else " "}] Millionaire (Win a total of 1,000,000 credits)

    [{"x" if achievements["oof_moment"] else " "}] Oof Moment (Lose a spin)
    [{"x" if achievements["you_should_stop"] else " "}] You Should Stop (Lose a total of 1,000 credits)
    [{"x" if achievements["you_should_REALLY_stop"] else " "}] You Should REALLY Stop (Lose a total of 10,000 credits)
    [{"x" if achievements["you're_just_gonna_lose_more"] else " "}] You're Just Gonna Lose More (Lose a total of 100,000 credits)
    [{"x" if achievements["rock_bottom"] else " "}] Rock Bottom (Lose a total of 1,000,000 credits)
    
    [{"x" if achievements["confidence_is_key"] else " "}] Confidence is Key (Go all in on a spin)
    [{"x" if achievements["i_can't_stop_winning"] else " "}] I Can't Stop Winning! (Win an all-in spin)
    [{"x" if achievements["aw_dangit"] else " "}] Aw Dangit! (Lose an all-in spin)
    
    [{"x" if achievements["at_least_i_still_have_clothes"] else " "}] At Least I Still Have Clothes (Take out a loan)
    [{"x" if achievements["petty_cash"] else " "}] Petty Cash (Take out a loan less than or equal to 10 credits)
    [{"x" if achievements["money_management"] else " "}] Money Management (Pay back a loan)
    [{"x" if achievements["still_hanging_in_there"] else " "}] Still Hanging in There (Take out another loan) 
    [{"x" if achievements["redemption_arc"] else " "}] Redemption Arc (Pay back three loans)

    [{"x" if achievements["overload"] else " "}] Overload (Max out on energy drinks)
    [{"x" if achievements["i_feel_funny"] else " "}] I Feel Funny (Buy from the bar)
    [{"x" if achievements["big_spender"] else " "}] Big Spender (Spend 1,000 credits at the bar)
    [{"x" if achievements["i'll_have_the_regular"] else " "}] I'll Have the Regular (Spend 10,000 credits at the bar)
    [{"x" if achievements["writing_checks_left_and_right"] else " "}] Writing Checks Left and Right (Spend 100,000 credits at the bar)

    [{"x" if achievements["insured"] else " "}] Insured (Purchase an insurance plan)
    [{"x" if achievements["volatile"] else " "}] Volatile (Make your insurance rate rise)
    [{"x" if achievements["the_bills_caught_up_to_you"] else " "}] The Bills Caught Up to You (Miss an insurance payment)

    [{"x" if achievements["your_family_is_worried"] else " "}] Your Family is Worried (Spend 14 days gambling)
    [{"x" if achievements["concerning_hygeine"] else " "}] Concerning Hygeine (Spend 50 days gambling)
    [{"x" if achievements["what_year_is_it"] else " "}] What Year is It? (Spend 100 days gambling)""")

    if achievements["the_light_is_blinding"]:
        print("    [x] The Light is Blinding (Leave the casino after 100 days)")

    b = 0 
    for i in bonus_achievements.keys():
        if bonus_achievements[i]:
            b += 1

    if b > 0:
        t = "?" if b < len(bonus_achievements) else len(bonus_achievements)
        print(f"\nYou've unlocked [{b}/{t}] Bonus Achievements\n")

        if bonus_achievements["counting_cards"]:
            print("    [x] Counting Cards (Use the developer console, you nasty cheater)")
        if bonus_achievements["extra_zesty"]:
            print("    [x] Extra Zesty (See all flavor texts on the home screen)")
        if bonus_achievements["regular_patron"]:
            print("    [x] Regular Patron (See all Bartender dialogues)")


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
                f"{variable} is currently set to {current_value}. Press [ENTER] to change it or 'cancel' to go back\n>> ")

            if menu.lower() == "cancel":
                break

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
        if menu == "achievement":
            while True:
                try:
                    achievement_name = input("Enter achievement name\n>> ")
                    menu = input(f"{achievement_name} is currently set to {achievements[achievement_name]}. Press [ENTER] to toggle it or 'cancel' to go back\n>> ")
                    if menu != "cancel":
                        if achievements[achievement_name]:
                            achievements[achievement_name] = False
                        elif not achievements[achievement_name]:
                            achievements[achievement_name] = True
                        print(
                            f"{achievement_name} is now set to {achievements[achievement_name]}")
                        break
                except:
                    print(f"Achievement '{achievement_name}' not found")
                    break
        if menu == "bonus":
            while True:
                try:
                    achievement_name = input("Enter achievement name\n>> ")
                    menu = input(f"{achievement_name} is currently set to {bonus_achievements[achievement_name]}. Press [ENTER] to toggle it or 'cancel' to go back\n>> ")
                    if menu != "cancel":
                        if bonus_achievements[achievement_name]:
                            bonus_achievements[achievement_name] = False
                        elif not bonus_achievements[achievement_name]:
                            bonus_achievements[achievement_name] = True
                        print(
                            f"{achievement_name} is now set to {bonus_achievements[achievement_name]}")
                        break
                except:
                    print(f"Achievement '{achievement_name}' not found")
                    break
        if menu == "misc":
            submenu = input(">> ")
            
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
        print(f"Credits: {player_credits:,}")
        print("")
        print(("-" * 20))
        try:
            win_percentage = 100 * (wins / spins)
            print("\nWin%: " + str(round(win_percentage, 2)) + "%")
        except ZeroDivisionError:
            print("\nWin%: N/A")
        print("Reward Multiplier:", round(reward_multiplier, 2))
        print("Luck:", luck)
        print("Streak Multiplier:", round(streak_multiplier, 1), "\n")
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
                f"\nInsurance Information:\n- Plan: {plan}\n- Payment: {insurance_payment} credits/day\n- Coverage: {insurance_coverage}%")
            print(("-" * 20))

        print(f"\n{pick_flavor_text()}\n")

        print(("-" * 20))

        if spins < 100:
            menu = input(
                "\nType 'achievements' to view your achievements or press [ENTER] to spin\n>> ")

            if menu == "achievements":
                display_achievements()
                input("\nPress [ENTER] to continue\n")
            elif menu == cake:
                devtools()
            else:
                break
                return
        elif spins >= 100:
            menu_ = input(
                "\nType 'achievements' to view your achievements, press [ENTER] to spin, or type 'leave' to escape\n>> ")

            if menu_ == "achievements":
                display_achievements()
                input("\nPress [ENTER] to continue\n")
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
    print(f"""
    ===================
    |     |     |     |
    |  {a}  |  {b}  |  {c}  |
    |     |     |     |
    ===================
    """)
    return [a, b, c]

# Calculate reward based on spin outcome and bet


def calculate_reward(spin: list, bet: int) -> int:
    global wins, streak
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
Welcome to the Gambler's Insurance Shop!

Credits: {player_credits:,}

Here are our plans:
    [{"x" if insurance_type == 0 else " "}] No Plan
    [{"x" if insurance_type == 1 else " "}] Starter Plan (Starts at 5 credits/day, 5% coverage)
    [{"x" if insurance_type == 2 else " "}] Basic Plan (Starts at 10 credits/day, 10% coverage)
    [{"x" if insurance_type == 3 else " "}] Hobbyist Plan (Starts at 50 credits/day, 25% coverage)
    [{"x" if insurance_type == 4 else " "}] Gambler's Dream (Starts at 250 credits/day, 50% coverage)

NOTE: All plans require a down payment equal to 10 times their starting rate
      Rate increases based on how much your insurance has covered
        """
    )
    while True:
        option = input("Choose a plan or type 'pass' to leave\n>> ").lower()
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
                print("You can't afford that plan!")
                continue
            has_insurance = True
            insurance_type = 1
            insurance_payment = 5
            insurance_coverage = 5
            player_credits -= 50
            break
        elif option == "basic plan" or option == "basic":
            if player_credits <= 100:
                print("You can't afford that plan!")
                continue
            has_insurance = True
            insurance_type = 2
            insurance_payment = 10
            insurance_coverage = 10
            player_credits -= 100
            break
        elif option == "hobbyist plan" or option == "hobbyist":
            if player_credits <= 500:
                print("You can't afford that plan!")
                continue
            has_insurance = True
            insurance_type = 3
            insurance_payment = 50
            insurance_coverage = 25
            player_credits -= 500
            break
        elif option == "gambler's dream" or option == "gambler's" or option == "gambler":
            if player_credits <= 2500:
                print("You can't afford that plan!")
                continue
            has_insurance = True
            insurance_type = 4
            insurance_payment = 250
            insurance_coverage = 50
            player_credits -= 2500
            break

    insurance_base = insurance_payment
    print("\nThank you for your business!\n\n[ENTER] to continue")
    input("")


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

    print(f"\nCredits: {player_credits:,}")
    print(f"""
    -- MENU --
    Beer: +5% Reward Multiplier (Cost: {reward_upgrade_price})
    Fries: +0.5 Luck (Cost: {luck_upgrade_price})
    Hot Dog: +0.1 Streak Multiplier (Cost: {streak_upgrade_price})
    Energy Drink: -1s Wheel Spin Time [{speed_upgrades+1 if speed_upgrades < 5 else 5}/5] (Cost: {speed_upgrade_price})
    """)
    print("Type 'buy <item name>' to buy an item or 'pass' to leave")
    while True:
        in_ = input(">> ")
        if in_ == "pass":
            return
        purchase = in_[4:].lower()
        if purchase == "beer":
            if reward_upgrade_price > player_credits:
                print("You can't afford that!")
                continue
            else:
                player_credits -= reward_upgrade_price
                reward_multiplier += 0.1
                reward_upgrade_price = round(1.5*reward_upgrade_price)
                break
        if purchase == "fries":
            if luck_upgrade_price > player_credits:
                print("You can't afford that!")
                continue
            else:
                player_credits -= luck_upgrade_price
                luck += 0.5
                luck_upgrade_price = round(1.5*luck_upgrade_price)
                break
        if purchase == "hot dog":
            if streak_upgrade_price > player_credits:
                print("You can't afford that!")
                continue
            else:
                player_credits -= streak_upgrade_price
                streak_multiplier += 0.1
                streak_upgrade_price = round(1.5*streak_upgrade_price)
                break
        if purchase == "energy drink":
            if speed_upgrade_price > player_credits:
                print("You can't afford that!")
                continue
            elif speed_upgrades > 3:
                print("You can't upgrade this stat anymore!")
                achievements["overload"] = True
                continue
            else:
                player_credits -= speed_upgrade_price
                speed_upgrade_price = round(1.5*speed_upgrade_price)
                speed_upgrades += 1
                break
    total_spent_in_shop = (s - player_credits)


# visit the in-game bank
def visit_bank():
    global player_credits, loan_amount, loan_payment, has_loan, interest_percent, achievements, loans_total, loans_paid
    clear_screen()
    if not has_loan:
        while True:
            clear_screen()
            print("Credits:", player_credits)
            print("Welcome to World Liberty Financial!\nType 'loan <amount>' for a loan")
            in_ = input(">> ")
            if len(in_.split(" ")) == 1:
                continue
            if in_.split(" ")[0] == "loan":
                amount = int(in_.split(" ")[1])
                loan_amount = amount
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

                print(
                    f"You took out a loan of {amount:,} credits\nBe prepared to pay it back in three days")
                input("\nPress [ENTER] to continue\n")
                break
    else:
        print(
            f"Time to pay your loan back.\nYour loan payment is {loan_payment:,} credits")
        print("Credits:", player_credits)
        input("\nPress [ENTER] to continue\n")
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


def borrow_from_spouse():
    global has_borrowed, has_borrow, player_credits
    borrow_amount = (spins * 1000)
    if spouse == "husband":
        print(
            f"You break away from the machine to call your husband. He says that he'll let you have {borrow_amount:,} credits, but if you lose with them he'll leave you. Take his deal?")
    if spouse == "wife":
        print(
            f"You break away from the machine to call your wife. She says that she'll let you have {borrow_amount:,} credits, but if you lose with them she'll leave you. Take her deal?")

    option = input("(y/n) >> ")

    if option.lower() == "y":
        if spouse == "husband":
            print("You take his money, determined to win it all.")
        if spouse == "wife":
            print("You take her money, determined to win it all.")
        has_borrowed = True
        player_credits = borrow_amount
    else:
        print("You hang up and decide to go to the bank instead.")
        has_borrowed = True
        visit_bank()


def game_over(source):
    global spins, spouse, achievements
    # end text conditions

    print(f"After {spins} days...")

    if spouse == "wife":
        end_text_1 = "\nYou are broke :(\nYou lost your house\nYou lost your wife\nShe took the kids\n\n\nWas it worth it?"
        end_text_2 = "\nYou made it out!\nYour wife is waiting outside for you.\nShe hugs you and says, \"I'm glad you're back.\""
        end_text_3 = "\nYou made it out!\nYour wife is waiting outside for you.\nShe hands you a stack of papers\nShe says, \"I want a divorce.\""
        end_text_4 = "\nYou lost the money your wife gave you! She calls, but you're too ashamed to pick up. You know it's over."
    if spouse == "husband":
        end_text_1 = "\nYou are broke :(\nYou lost your house\nYou lost your husband\nHe took the kids\n\n\nWas it worth it?"
        end_text_2 = "\nYou made it out!\nYour husband is waiting outside for you.\nHe hugs you and says, \"I'm glad you're back.\""
        end_text_3 = "\nYou made it out!\nYour husband is waiting outside for you.\nHe hands you a stack of papers\nHe says, \"I want a divorce.\""
        end_text_4 = "\nYou lost the money your husband gave you! He calls, but you're too ashamed to pick up. You know it's over."
    if source == 0:  # bankruptcy
        print(end_text_1)
    elif source == 1:  # loan payment
        print(f"You missed your loan payment by {loan_payment:,} credits")
        print(end_text_1)
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
            print(end_text_2)
        if p < 100:
            print(end_text_3)
    elif source == 3:  # Failed lifeline
        print(end_text_4)

    display_achievements()
    while True:
        time.sleep(1)


clear_screen()
if IS_DEV_BUILD:
    print("Welcome to Gambling Simulator dev-1.10!\nThis is a developer build and may be unfinished or broken.\n\nPress [ENTER] to continue")
else:
    print("Welcome to Gambling Simulator v1.10!\n\nPress [ENTER] to continue")
m = input("")

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
            print(f"Your loan payment is: {loan_payment:,}")
            print(f"Credits: {player_credits:,}")
        if days_passed == 4:
            visit_bank()
        days_passed += 1
    if player_credits <= 0:
        if not has_loan:
            if not has_borrowed and spins >= 10:
                print(
                    f"You have no credits. Type 'bank' to visit the bank or 'borrow' to borrow money from your {spouse}.")
            else:
                print("You have no credits. Type 'bank' to visit the bank.")

            option = input(">> ")
            if option == "bank":
                visit_bank()
            elif not has_borrowed and spins >= 10:
                if option == "borrow":
                    borrow_from_spouse()
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
                print(f"Credits: {player_credits:,}")
                bet = int(input("Bet: "))
                if bet > player_credits:
                    print("You don't have enough money for that")
                elif bet == player_credits:
                    achievements["confidence_is_key"] = True
                elif bet == 0:
                    print("Bet must be a non-zero whole number")
            except ValueError:
                print("Bet must be a non-zero whole number")

    clear_screen()

    print("Spinning...")
    time.sleep(5 - speed_upgrades)

    spin_result = get_letters()
    spins += 1
    reward = calculate_reward(spin_result, bet)

    if reward > 0:
        has_borrow = False
        has_borrowed = True
        print("Reward:", reward)
        if bet == player_credits:
            achievements["i_can't_stop_winning"] = True
        total_won += reward
    else:
        print("You Lost!")
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
            print("Thankfully, your insurance covered " +
                  f"{covered:,}" + " credit" + ("s" if covered > 1 else "") + ".")
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

    print("\nPress [ENTER] to continue")
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
                    print("Achievement Unlocked:", name)
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
                    print("Bonus Achievement Unlocked:", name)

        input("\n[ENTER] to continue\n")

    if player_credits <= 0:
        pass
    else:
        while True:
            clear_screen()
            print(
                "Type 'shop' to visit the shop, 'insurance' to buy insurance, or pass to leave")
            in_ = input(">> ")
            if in_ == "shop":
                visit_shop()
                break
            if in_ == "insurance":
                insurance_shop()
                break
            if in_ == "pass":
                break
    clear_screen()
