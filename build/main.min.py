_A1='Bet must be a non-zero whole number'
_A0='counting_cards'
_z='thecakeisalie'
_y='husband'
_x='red'
_w='yes'
_v='shifty_business'
_u='last_resort'
_t='back_from_the_brink'
_s='regular_patron'
_r='extra_zesty'
_q='the_light_is_blinding'
_p='what_year_is_it'
_o='concerning_hygeine'
_n='your_family_is_worried'
_m='the_bills_caught_up_to_you'
_l='volatile'
_k='insured'
_j='overload'
_i='writing_checks_left_and_right'
_h="i'll_have_the_regular"
_g='big_spender'
_f='i_feel_funny'
_e='redemption_arc'
_d='still_hanging_in_there'
_c='money_management'
_b='petty_cash'
_a='at_least_i_still_have_clothes'
_Z='aw_dangit'
_Y="i_can't_stop_winning"
_X='rock_bottom'
_W="you're_just_gonna_lose_more"
_V='you_should_REALLY_stop'
_U='you_should_stop'
_T='oof_moment'
_S='millionaire'
_R='rolling_in_dough'
_Q='a_decent_sum'
_P='on_a_roll'
_O='getting_somewhere'
_N=None
_M='black'
_L='confidence_is_key'
_K='wife'
_J='>> '
_I='pass'
_H='text'
_G='days_end'
_F='days_start'
_E='displayed'
_D='enter'
_C=' '
_B=False
_A=True
import random,time,os,types
from colorama import Fore,Back,Style
IS_DEV_BUILD=_A
console_used=_B
suppress=_B
is_running=_A
player_credits=250
spins=0
wins=0
streak=0
jackpots=0
total_won=0
total_lost=0
kidneys=2
is_high_roller=_B
roulette_chips=0
spouse=_K
cake=_z
luck_upgrades=0
reward_upgrades=0
streak_upgrades=0
speed_upgrades=0
luck_upgrade_price=50
reward_upgrade_price=25
streak_upgrade_price=25
speed_upgrade_price=50
luck=0
reward_multiplier=1.
streak_multiplier=1.1
bar_dialogue_count=0
has_loan=_B
fake_id=_B
interest_percent=.05
loan_payment=0
loan_amount=0
days_passed=0
has_insurance=_B
insurance_coverage=0
insurance_payment=0
insurance_type=0
total_covered=0
insurance_base=0
total_won=0
total_lost=0
total_spent_in_shop=0
loans_total=0
loans_paid=0
has_borrow=_B
has_borrowed=_B
borrow_amount=0
ach_x=f"{Fore.MAGENTA}x{Style.RESET_ALL}"
achievements={_O:_B,_P:_B,_Q:_B,_R:_B,_S:_B,_T:_B,_U:_B,_V:_B,_W:_B,_X:_B,_L:_B,_Y:_B,_Z:_B,_a:_B,_b:_B,_c:_B,_d:_B,_e:_B,_f:_B,_g:_B,_h:_B,_i:_B,_j:_B,_k:_B,_l:_B,_m:_B,_n:_B,_o:_B,_p:_B,_q:_B}
bonus_achievements={_A0:_B,_r:_B,_s:_B,_t:_B,_u:_B,_v:_B}
bonuses=['WIN','FUN','FLY','ABC','AAA','DIE','ASS','AOL','HIT','BRO','BET','TIT','SCP','WHY','BOP','BEE','BUM','ZAP','DEW','MUM','HAG','WTF','PBS','POO']
letters=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
flavor_text=[{_F:0,_G:1,_H:f"You can practically taste your {Fore.GREEN}winnings{Style.RESET_ALL} already.",_E:_B},{_F:2,_G:5,_H:"You haven't been here very long, but you feel like you could stay forever.",_E:_B},{_F:6,_G:9,_H:'You begin to notice a regular deposit of crumbs at your machine. Are they yours?',_E:_B},{_F:10,_G:14,_H:f"The handle on the machine is getting {Style.DIM}greasy{Style.RESET_ALL}. You should wash your hands.",_E:_B},{_F:15,_G:19,_H:f"Your back is {Style.DIM}weary{Style.RESET_ALL} of hunching over the machine. Taking a walk might help.",_E:_B},{_F:20,_G:24,_H:f"You haven't seen the {Style.BRIGHT}{Fore.YELLOW}sun{Style.RESET_ALL} in quite a while.",_E:_B},{_F:25,_G:54,_H:'Are you satisfied yet?',_E:_B},{_F:55,_G:94,_H:f"Your committment would be inspiring, were it not an {Fore.RED}addiction{Style.RESET_ALL}.",_E:_B},{_F:95,_G:100,_H:'Is the casino still real?',_E:_B}]
bar_dialogue=['"Hey there, care for a drink?"',f'"How are the {Fore.GREEN}winnings{Style.RESET_ALL}?"','"Good day, huh?"','"Business is slow today. Take a look."','"What\'s new?"',f'"Every day\'s a good day to get {Fore.GREEN}drunk{Style.RESET_ALL}."','"How\'re the kids?"','"My husband says I need to get a real job."','"Rough day, huh?"',f'"Here, have a {Fore.YELLOW}beer{Style.RESET_ALL} on me."','"Kids these days..."',f'"Went to college for {Fore.BLUE}physics{Style.RESET_ALL}, why am I here?"','"Everyone leaves eventually. Will you?"']
bar_actions=['The bartender looks up and says, ',"The bartender doesn't look up when you enter.","The bartender seems engrossed in cleaning a glass. He doesn't appear to notice you.",f"The bartender is wiping down the counter - the room smells vaguely of {Fore.CYAN}cleaning chemicals{Style.RESET_ALL} and {Fore.GREEN}vomit{Style.RESET_ALL}.",f"The bartender isn't in. There's a sign that says: \"Leave the {Fore.YELLOW}money{Style.RESET_ALL} on the counter. Help yourself.\"",f"The bartender isn't in. There's a {Fore.RED}woman{Style.RESET_ALL} at the counter who eyes you with an {Fore.MAGENTA}emotion{Style.RESET_ALL} you can't decipher."]
def pick_flavor_text():
	A='Just another day in the casino.';global spins,flavor_text
	for f in flavor_text:
		if f[_F]<=spins<=f[_G]and not f[_E]:
			if random.randint(1,f[_G]-f[_F])==1:f[_E]=_A;return f[_H]
			else:return A
		return A
def clear_screen():
	if os.name=='nt':os.system('cls')
	else:os.system('clear')
def btn(label):return f"[{Style.BRIGHT}{Fore.CYAN}{label.upper()}{Style.RESET_ALL}]"
def calculate_achievements():
	if total_won>=1:achievements[_O]=_A
	if total_won>=1000:achievements[_P]=_A
	if total_won>=10000:achievements[_Q]=_A
	if total_won>=100000:achievements[_R]=_A
	if total_won>=1000000:achievements[_S]=_A
	if total_lost>=1:achievements[_T]=_A
	if total_lost>=1000:achievements[_U]=_A
	if total_lost>=10000:achievements[_V]=_A
	if total_lost>=100000:achievements[_W]=_A
	if total_lost>=1000000:achievements[_X]=_A
	if total_spent_in_shop>=1:achievements[_f]=_A
	if total_spent_in_shop>=1000:achievements[_g]=_A
	if total_spent_in_shop>=10000:achievements[_h]=_A
	if total_spent_in_shop>=100000:achievements[_i]=_A
	if has_insurance:achievements[_k]=_A
	if insurance_payment>insurance_base:achievements[_l]=_A
	if spins>=14:achievements[_n]=_A
	if spins>=50:achievements[_o]=_A
	if spins>=100:achievements[_p]=_A
	b=0
	for f in flavor_text:
		if f[_E]:b+=1
	if b==len(flavor_text):bonus_achievements[_r]=_A
def display_achievements():
	calculate_achievements();global achievements,console_used;a=0
	for i in achievements.keys():
		if achievements[i]:a+=1
	try:p=round(100*(a/len(achievements)))
	except ZeroDivisionError:p=0
	if p==100:p=f"{Fore.GREEN}100%{Style.RESET_ALL}"
	else:p=f"{p}%"
	print(f"""
You've Unlocked [{f"{Fore.GREEN}{a}/{len(achievements)}{Style.RESET_ALL}"if a==len(achievements)else f"{a}/{len(achievements)}"}] Achievements ({p}) {f"({Fore.RED}Cheats used{Style.RESET_ALL})"if console_used else""}
    
    [{ach_x if achievements[_O]else _C}] Getting Somewhere (Win a spin)
    [{ach_x if achievements[_P]else _C}] On a Roll (Win a total of 1,000 credits)
    [{ach_x if achievements[_Q]else _C}] A Decent Sum (Win a total of 10,000 credits)
    [{ach_x if achievements[_R]else _C}] Rolling in Dough (Win a total of 100,000 credits)
    [{ach_x if achievements[_S]else _C}] Millionaire (Win a total of 1,000,000 credits)

    [{ach_x if achievements[_T]else _C}] Oof Moment (Lose a spin)
    [{ach_x if achievements[_U]else _C}] You Should Stop (Lose a total of 1,000 credits)
    [{ach_x if achievements[_V]else _C}] You Should REALLY Stop (Lose a total of 10,000 credits)
    [{ach_x if achievements[_W]else _C}] You're Just Gonna Lose More (Lose a total of 100,000 credits)
    [{ach_x if achievements[_X]else _C}] Rock Bottom (Lose a total of 1,000,000 credits)
    
    [{ach_x if achievements[_L]else _C}] Confidence is Key (Go all in on a spin)
    [{ach_x if achievements[_Y]else _C}] I Can't Stop Winning! (Win an all-in spin)
    [{ach_x if achievements[_Z]else _C}] Aw Dangit! (Lose an all-in spin)
    
    [{ach_x if achievements[_a]else _C}] At Least I Still Have Clothes (Take out a loan)
    [{ach_x if achievements[_b]else _C}] Petty Cash (Take out a loan less than or equal to 10 credits)
    [{ach_x if achievements[_c]else _C}] Money Management (Pay back a loan)
    [{ach_x if achievements[_d]else _C}] Still Hanging in There (Take out another loan) 
    [{ach_x if achievements[_e]else _C}] Redemption Arc (Pay back three loans)

    [{ach_x if achievements[_f]else _C}] I Feel Funny (Buy from the bar)
    [{ach_x if achievements[_g]else _C}] Big Spender (Spend 1,000 credits at the bar)
    [{ach_x if achievements[_h]else _C}] I'll Have the Regular (Spend 10,000 credits at the bar)
    [{ach_x if achievements[_i]else _C}] Writing Checks Left and Right (Spend 100,000 credits at the bar)
    [{ach_x if achievements[_j]else _C}] Overload (Max out on energy drinks)

    [{ach_x if achievements[_k]else _C}] Insured (Purchase an insurance plan)
    [{ach_x if achievements[_l]else _C}] Volatile (Make your insurance rate rise)
    [{ach_x if achievements[_m]else _C}] The Bills Caught Up to You (Miss an insurance payment)

    [{ach_x if achievements[_n]else _C}] Your Family is Worried (Spend 14 days gambling)
    [{ach_x if achievements[_o]else _C}] Concerning Hygeine (Spend 50 days gambling)
    [{ach_x if achievements[_p]else _C}] What Year is It? (Spend 100 days gambling)""")
	if achievements[_q]:print(f"    [{Fore.MAGENTA}{Style.BRIGHT}x{Style.RESET_ALL}] The Light is {Fore.YELLOW}{Style.BRIGHT}Blinding{Style.RESET_ALL} (Leave the casino after 100 days)")
	b=0
	for i in bonus_achievements.keys():
		if bonus_achievements[i]:b+=1
	if b>0:
		t='?'if b<len(bonus_achievements)else len(bonus_achievements)
		if b==t:print(f"\nYou've unlocked [{Fore.GREEN}{b}/{t}{Style.RESET_ALL}] Bonus Achievements\n")
		else:print(f"\nYou've unlocked [{b}/{t}] Bonus Achievements\n")
		if bonus_achievements[_A0]:print(f"    [{Fore.CYAN}x{Style.RESET_ALL}] Counting Cards (Use the developer console, you nasty cheater)")
		if bonus_achievements[_r]:print(f"    [{Fore.CYAN}x{Style.RESET_ALL}] Extra Zesty (See all flavor texts on the home screen)")
		if bonus_achievements[_s]:print(f"    [{Fore.CYAN}x{Style.RESET_ALL}] Regular Patron (See all Bartender dialogues)")
		if bonus_achievements[_t]:print(f"    [{Fore.CYAN}x{Style.RESET_ALL}] Back from the Brink (Win 'The Deal')")
		if bonus_achievements[_u]:print(f"    [{Fore.CYAN}x{Style.RESET_ALL}] Last Resort (Sell your kidney)")
		if bonus_achievements[_v]:print(f"    [{Fore.CYAN}x{Style.RESET_ALL}] Shifty Business (Buy a fake ID)")
def get_variable_type(var):
	if isinstance(var,bool):return bool
	elif isinstance(var,int):return int
	elif isinstance(var,str):return str
	else:return type(var)
def devtools():
	C='Enter achievement name\n>> ';B='Invalid input';A='cancel';global player_credits,console_used;clear_screen();print('Welcome to the V.I.P. Club')
	while _A:
		menu=input('\n>>> ')
		if menu=='variable':
			variable=input('Enter the variable name\n>> ')
			if variable not in globals():print(f"Variable '{variable}' not found");continue
			current_value=globals()[variable];_type=get_variable_type(current_value);menu=input(f"{variable} is currently set to {current_value}. Press {btn(_D)} to change it or 'cancel' to go back\n>> ")
			if menu.lower()==A:continue
			if _type==int:
				while _A:
					try:value=int(input('Enter an integer value\n>> '));break
					except ValueError:print(B)
			elif _type==str:value=input('Enter a string value\n>> ')
			elif _type==bool:
				while _A:
					bool_input=input('Enter a boolean value\n>> ').lower()
					if bool_input in['true','1',_w,'y']:value=_A;break
					if bool_input in['false','0','no','n']:value=_B;break
					else:print(B)
			else:break
			globals()[variable]=value;print(f"{variable} is now set to {globals()[variable]}")
		if menu=='function':
			while _A:
				try:function=input('Enter the function name\n>> ');exec(f"{function}()");break
				except:print(f"Function '{function}' not found");break
		if menu=='completion':
			menu=input(f"Press {btn(_D)} to enable all achievements or 'cancel' to go back ")
			for i in achievements:achievements[i]=_A
			for i in bonus_achievements:bonus_achievements[i]=_A
		if menu=='achievement':
			while _A:
				try:
					achievement_name=input(C);menu=input(f"{achievement_name} is currently set to {achievements[achievement_name]}. Press {btn(_D)} to toggle it or 'cancel' to go back\n>> ")
					if menu!=A:
						if achievements[achievement_name]:achievements[achievement_name]=_B
						elif not achievements[achievement_name]:achievements[achievement_name]=_A
						print(f"{achievement_name} is now set to {achievements[achievement_name]}");break
					else:break
				except:print(f"Achievement '{achievement_name}' not found");break
		if menu=='bonus':
			while _A:
				try:
					achievement_name=input(C);menu=input(f"{achievement_name} is currently set to {bonus_achievements[achievement_name]}. Press {btn(_D)} to toggle it or 'cancel' to go back\n>> ")
					if menu!=A:
						if bonus_achievements[achievement_name]:bonus_achievements[achievement_name]=_B
						elif not bonus_achievements[achievement_name]:bonus_achievements[achievement_name]=_A
						print(f"{achievement_name} is now set to {bonus_achievements[achievement_name]}");break
					else:break
				except:print(f"Achievement '{achievement_name}' not found");break
		if menu=='jumpstart':player_credits=1000000;globals()['total_won']=50000;globals()['luck']=1;globals()['is_high_roller']=_A
		if menu=='dump':
			gl=globals()
			for g in gl.keys():
				if'__'in g or isinstance(gl[g],types.FunctionType)or isinstance(gl[g],types.ModuleType):continue
				if len(g)<=2:continue
				if isinstance(gl[g],dict):print(f"{g}: dictionary with {len(gl[g])} items")
				elif isinstance(gl[g],list):print(f"{g}: list with {len(gl[g])} items")
				else:print(f"{g}: {gl[g]}")
		if menu==_I:clear_screen();break
	console_used=_A
	if suppress:console_used=_B
def display_home_screen():
	B='achievements';A='-';global insurance_payment
	while _A:
		clear_screen();print(f"Credits: {Fore.YELLOW}{player_credits:,}{Style.RESET_ALL}");print('');print(A*20)
		try:win_percentage=100*(wins/spins);print('\n'+Fore.GREEN+'Win%'+Style.RESET_ALL+':               '+str(round(win_percentage,2))+'%')
		except ZeroDivisionError:print(f" \n{Fore.GREEN}Win%{Style.RESET_ALL}:               N/A")
		print(Fore.YELLOW+'Reward Multiplier'+Style.RESET_ALL+': ',round(reward_multiplier,2));print(Fore.MAGENTA+'Luck'+Style.RESET_ALL+':              ',float(luck));print(Fore.CYAN+'Streak Multiplier'+Style.RESET_ALL+': ',round(streak_multiplier,1),'\n');print(A*20)
		if has_insurance:
			if insurance_type==1:plan='Starter Plan'
			elif insurance_type==2:plan='Basic Plan'
			elif insurance_type==3:plan='Hobbyist Plan'
			elif insurance_type==4:plan="Gambler's Dream"
			if round(total_covered/20)>=insurance_base:insurance_payment=round(total_covered/20)
			print(f"""
Insurance Information:
- Plan: {plan}
- Payment: {insurance_payment:,} credits/day
- Coverage: {insurance_coverage}%
""");print(A*20)
		print(f"\n{pick_flavor_text()}\n");print(A*20)
		if spins<100:
			menu=input(f"\nType 'achievements' to view your achievements or press {btn(_D)} to spin\n>> ")
			if menu==B:display_achievements();input(f"\nPress {btn(_D)} to continue\n")
			elif menu==cake:devtools()
			else:break;return
		elif spins>=100:
			menu_=input(f"\nType 'achievements' to view your achievements, press {btn(_D)} to spin, or type '{Fore.GREEN}leave{Style.RESET_ALL}' to {Fore.GREEN}escape{Style.RESET_ALL}\n>> ")
			if menu_==B:display_achievements();input(f"\nPress {btn(_D)} to continue\n")
			elif menu_==_z:devtools()
			elif menu_=='leave':game_over(2);break
			else:break;return
def get_letters():
	a=letters[random.randint(0,25)];b=a if random.randint(1,round(15-luck/2))==1 else letters[random.randint(0,25)]
	if random.randint(1,5)==1:c=a if random.randint(1,round(15-luck/2))==1 else letters[random.randint(0,25)]
	else:c=b if random.randint(1,round(15-luck/2))==1 else letters[random.randint(0,25)];colora=a;colorb=b;colorc=c
	if(a+b+c).upper()in bonuses:colora=Fore.MAGENTA+a+Style.RESET_ALL;colorb=Fore.MAGENTA+b+Style.RESET_ALL;colorc=Fore.MAGENTA+c+Style.RESET_ALL
	print(f"""
    ===================
    |     |     |     |
    |  {colora}  |  {colorb}  |  {colorc}  |
    |     |     |     |
    ===================
    """);return[a,b,c]
def calculate_reward(spin,bet):
	global wins,streak,has_borrow;double=_B;triple=_B;bonus=_B;reward=bet;unique_letters=[]
	for letter in spin:
		if letter not in unique_letters:unique_letters.append(letter)
		elif spin.count(letter)==3:triple=_A
		else:double=_A
	for bonus_word in bonuses:
		if f"{spin[0]}{spin[1]}{spin[2]}"==bonus_word:bonus=_A
	if has_borrow:bonus=_A
	if double:reward*=2;wins+=1;streak+=1
	elif triple:reward*=4;wins+=1;streak+=1
	if bonus:reward*=4;wins+=1;streak+=1
	if not double and not triple and not bonus:reward=0;streak=0
	if streak>1:return int(reward*reward_multiplier*(streak*streak_multiplier))
	else:return int(reward*reward_multiplier)
def insurance_shop():
	global has_insurance,insurance_coverage,insurance_payment,insurance_type,player_credits,insurance_base;clear_screen();print(f"""
Welcome to the {Fore.YELLOW}Gambler's Insurance{Style.RESET_ALL} Shop!

Credits: {Fore.YELLOW}{player_credits:,}{Style.RESET_ALL}

Here are our plans:
    [{ach_x if insurance_type==0 else _C}] No Plan
    [{ach_x if insurance_type==1 else _C}] Starter Plan (Starts at {Fore.YELLOW}5{Style.RESET_ALL} credits/day, {Fore.GREEN}5%{Style.RESET_ALL} coverage)
    [{ach_x if insurance_type==2 else _C}] Basic Plan (Starts at {Fore.YELLOW}10{Style.RESET_ALL} credits/day, {Fore.GREEN}10%{Style.RESET_ALL} coverage)
    [{ach_x if insurance_type==3 else _C}] Hobbyist Plan (Starts at {Fore.YELLOW}50{Style.RESET_ALL} credits/day, {Fore.GREEN}25%{Style.RESET_ALL} coverage)
    [{ach_x if insurance_type==4 else _C}] Gambler's Dream (Starts at {Fore.YELLOW}250{Style.RESET_ALL} credits/day, {Fore.GREEN}50%{Style.RESET_ALL} coverage)

NOTE: All plans require a down payment equal to {Fore.YELLOW}10 times their starting rate{Style.RESET_ALL}
      Rate increases based on how much your insurance has covered
        """)
	while _A:
		option=input(f"Choose a plan or type '{Style.DIM}pass{Style.RESET_ALL}' to leave\n>> ").lower()
		if option==_I:return
		elif option=='no plan':has_insurance=_B;insurance_type=0;insurance_payment=0;insurance_coverage=0;break
		elif option=='starter plan'or option=='starter':
			if player_credits<=50:print(f"{Fore.RED}You can't afford that plan!{Style.RESET_ALL}");continue
			has_insurance=_A;insurance_type=1;insurance_payment=5;insurance_coverage=5;player_credits-=50;break
		elif option=='basic plan'or option=='basic':
			if player_credits<=100:print(f"{Fore.RED}You can't afford that plan!{Style.RESET_ALL}");continue
			has_insurance=_A;insurance_type=2;insurance_payment=10;insurance_coverage=10;player_credits-=100;break
		elif option=='hobbyist plan'or option=='hobbyist':
			if player_credits<=500:print(f"{Fore.RED}You can't afford that plan!{Style.RESET_ALL}");continue
			has_insurance=_A;insurance_type=3;insurance_payment=50;insurance_coverage=25;player_credits-=500;break
		elif option=="gambler's dream"or option=="gambler's"or option=='gambler':
			if player_credits<=2500:print(f"{Fore.RED}You can't afford that plan!{Style.RESET_ALL}");continue
			has_insurance=_A;insurance_type=4;insurance_payment=250;insurance_coverage=50;player_credits-=2500;break
	insurance_base=insurance_payment;print(f"\nThank you for your business!\n\n{btn(_D)} to continue");input('')
def roulette_spin():
	color='none';number=str(random.randint(0,37))
	if number=='37':number='00'
	if int(number)%2==0:color=_x
	if number=='0'or number=='00':color='green'
	else:color=_M
	return color,number
def get_roulette_reward(bet_type,x,bet_amount,color,number):
	dozen_one=[1,2,3,4,5,6,7,8,9,10,11,12];dozen_two=[13,14,15,16,17,18,19,20,21,22,23,24];dozen_three=[25,26,27,28,29,30,31,32,33,34,35,36];column_one=[1,4,7,10,13,16,19,22,25,28,31,34];column_two=[2,5,8,11,14,17,20,23,26,29,32,35];column_three=[3,6,9,12,15,18,21,24,27,30,33,36];low=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18];high=[19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36];reds=[1,3,5,7,9,12,14,16,18,21,23,25,27,28,30,32,34,36];blacks=[a if a not in reds else _N for a in range(1,37)]
	if bet_type=='single':
		if bet_amount==int(number):return bet_amount*35+bet_amount
		else:return 0
	if bet_type=='column':
		if int(number)in x:return bet_amount*2+bet_amount
		else:return 0
	if bet_type=='dozen':
		if int(number)in x:return bet_amount*2+bet_amount
		else:return 0
	if bet_type==_x:
		if int(number)in reds:return bet_amount*2
		else:return 0
	if bet_type==_M:
		if int(number)in blacks:return bet_amount*2
		else:return 0
	if bet_type=='low':
		if int(number)in low:return bet_amount*2
		else:return 0
	if bet_type=='high':
		if int(number)in high:return bet_amount*2
		else:return 0
	if bet_type=='odd':
		if int(number)%2!=0:return bet_amount*2
		else:return 0
	if bet_type=='even':
		if int(number)%2==0:return bet_amount*2
		else:return 0
def play_roulette():
	global roulette_chips;dozen_one=[1,2,3,4,5,6,7,8,9,10,11,12];dozen_two=[13,14,15,16,17,18,19,20,21,22,23,24];dozen_three=[25,26,27,28,29,30,31,32,33,34,35,36];column_one=[1,4,7,10,13,16,19,22,25,28,31,34];column_two=[2,5,8,11,14,17,20,23,26,29,32,35];column_three=[3,6,9,12,15,18,21,24,27,30,33,36];low=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18];high=[19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36];reds=[1,3,5,7,9,12,14,16,18,21,23,25,27,28,30,32,34,36];blacks=[a if a not in reds else _N for a in range(1,37)]
	while _A:
		clear_screen();print(f"""
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
""");bet_type=input('\nBet Type: ').lower()
		if bet_type=='column one':x=column_one
		if bet_type=='column two':x=column_two
		if bet_type=='column three':x=column_three
		if bet_type=='dozen one':x=dozen_one
		if bet_type=='dozen two':x=dozen_two
		if bet_type=='dozen three':x=dozen_three
		if bet_type=='low':x=low
		if bet_type=='high':x=high
		if bet_type==_x:x=reds
		if bet_type==_M:x=blacks
		if bet_type=='odd':x=[a if a%2!=0 else _N for a in range(1,37)]
		if bet_type=='even':x=[a if a%2==0 else _N for a in range(1,37)]
		while _A:
			bet_amount=int(input('Bet Amount: '))
			if bet_amount<=0 or bet_amount>roulette_chips:print('Enter a non-zero number of chips that you can afford.')
			else:break
		roulette_chips-=bet_amount;clear_screen();color,number=roulette_spin();c=f"{Style.DIM}{Fore.BLACK}"if color==_M else f"{Style.BRIGHT}{Fore.RED}";print('Spin: '+c+color.title()+_C+number+Style.RESET_ALL);reward=get_roulette_reward(bet_type,x,bet_amount,color,number);roulette_chips+=reward;print(Fore.GREEN+'Reward: '+str(reward)+Style.RESET_ALL);print(Fore.YELLOW+'Chips: '+str(roulette_chips)+Style.RESET_ALL);menu=input(f"'leave' to leave or {btn(_D)} to continue");clear_screen()
		if menu=='leave':clear_screen();break
		if roulette_chips<=0:clear_screen();print(f"{Fore.RED}You have run out of roulette chips.{Style.RESET_ALL}");break
def high_rollers():
	global player_credits,is_high_roller,luck,roulette_chips;clear_screen()
	if not is_high_roller:print(f"You don't have a {Fore.CYAN}membership card{Style.RESET_ALL}. \nThe bouncer {Fore.RED}turns you away{Style.RESET_ALL}.");input(f"\n{btn(_D)} to continue\n");return
	while _A:
		clear_screen();print(f"Welcome to the {Fore.MAGENTA}High Rollers club!{Style.RESET_ALL}");print(f"You have {roulette_chips} chips");menu=input(f"\ntype 'chips' to buy more chips, 'credits' to cash in chips, 'spin' to play roulette, or '{Style.DIM}pass{Style.RESET_ALL}' to leave\n>> ")
		if menu=='chips':
			clear_screen();print(f"Credits: {Fore.YELLOW}{player_credits:,}{Style.RESET_ALL}");print('Exchange rate: 1 Chip for 5 Credits')
			while _A:
				amount=input(f"Enter a number of chips to buy or '{Style.DIM}pass{Style.RESET_ALL}' to leave\n>> ")
				if amount==_I or amount.isnumeric()and int(amount)>0:0
				else:print(f"Enter a non-zero numeric value or '{Style.DIM}pass{Style.RESET_ALL}'");continue
				if amount==_I:break
				else:
					amount=round(int(amount))
					if amount*5>player_credits:print(f"{Fore.RED}You can't afford that many chips!{Style.RESET_ALL}");continue
					else:player_credits-=amount*5;roulette_chips+=amount
		elif menu=='spin':clear_screen();play_roulette()
		elif menu=='credits':
			clear_screen();print(f"You have {roulette_chips} chips")
			while _A:
				amount=input(f"Enter a number of chips to cash in or '{Style.DIM}pass{Style.RESET_ALL}' to leave\n>> ")
				if amount==_I or amount.isnumeric()and int(amount)>0:0
				else:print(f"Enter a non-zero numeric value or '{Style.DIM}pass{Style.RESET_ALL}'");continue
				if amount==_I:break
				else:
					amount=round(int(amount))
					if amount>roulette_chips:print(f"{Fore.RED}You can't afford that many chips!{Style.RESET_ALL}");continue
					else:player_credits+=round(amount/5);roulette_chips-=amount
		elif menu==_I:break
def visit_shop():
	D='energy drink';C='hot dog';B='fries';A='beer';global reward_multiplier,luck,luck_upgrade_price,reward_upgrade_price,streak_multiplier,streak_upgrade_price,player_credits,speed_upgrade_price,speed_upgrades,total_spent_in_shop,achievements,bonus_achievements,bar_actions,bar_dialogue,bar_dialogue_count;clear_screen();s=player_credits;print('Welcome to the bar!');dialogue=random.randint(0,5)
	if dialogue==0:
		print(f"{bar_actions[0]}{bar_dialogue[bar_dialogue_count]}");bar_dialogue_count+=1
		if bar_dialogue_count==len(bar_dialogue):bonus_achievements[_s]=_A;bar_dialogue_count=0
	else:print(bar_actions[dialogue])
	print(f"\nCredits: {Fore.YELLOW}{player_credits:,}{Style.RESET_ALL}");print(f"""
    -- MENU --
    Beer: +{Fore.YELLOW}5% Reward Multiplier{Style.RESET_ALL} (Cost: {Fore.YELLOW}{reward_upgrade_price}{Style.RESET_ALL})
    Fries: +{Fore.MAGENTA}0.5 Luck{Style.RESET_ALL} (Cost: {Fore.YELLOW}{luck_upgrade_price}{Style.RESET_ALL})
    Hot Dog: +{Fore.CYAN}0.1 Streak Multiplier{Style.RESET_ALL} (Cost: {Fore.YELLOW}{streak_upgrade_price}{Style.RESET_ALL})
    Energy Drink: -{Fore.GREEN}1s Wheel Spin Time{Style.RESET_ALL} [{f"{Fore.GREEN}{Style.BRIGHT}"if speed_upgrades>=5 else""}{speed_upgrades if speed_upgrades<5 else 5}/5{Style.RESET_ALL}] (Cost: {Fore.YELLOW}{speed_upgrade_price}{Style.RESET_ALL})
    """);print(f"Type 'buy <item name>' to buy an item or '{Style.DIM}pass{Style.RESET_ALL}' to leave")
	while _A:
		in_=input(_J)
		if in_==_I:return
		purchase=in_[4:].lower()
		if purchase==A:
			if reward_upgrade_price>player_credits:print(f"{Fore.RED}You can't afford that!{Style.RESET_ALL}");continue
			else:player_credits-=reward_upgrade_price;reward_multiplier+=.1;reward_upgrade_price=round(1.5*reward_upgrade_price);break
		if purchase==B:
			if luck_upgrade_price>player_credits:print(f"{Fore.RED}You can't afford that!{Style.RESET_ALL}");continue
			else:player_credits-=luck_upgrade_price;luck+=.5;luck_upgrade_price=round(1.5*luck_upgrade_price);break
		if purchase==C:
			if streak_upgrade_price>player_credits:print(f"{Fore.RED}You can't afford that!{Style.RESET_ALL}");continue
			else:player_credits-=streak_upgrade_price;streak_multiplier+=.1;streak_upgrade_price=round(1.5*streak_upgrade_price);break
		if purchase==D:
			if speed_upgrade_price>player_credits:print(f"{Fore.RED}You can't afford that!{Style.RESET_ALL}");continue
			elif speed_upgrades>3:print(f"{Fore.GREEN}You can't upgrade this stat anymore!{Style.RESET_ALL}");achievements[_j]=_A;continue
			else:player_credits-=speed_upgrade_price;speed_upgrade_price=round(1.5*speed_upgrade_price);speed_upgrades+=1;break
	total_spent_in_shop=s-player_credits
	if purchase in[A,B,C,D]and kidneys==1:game_over(4)
def black_market():
	global player_credits,fake_id,bonus_achievements
	if not fake_id:
		clear_screen();print(f"You notice a {Fore.CYAN}strange man{Style.RESET_ALL} hunched in a corner. He's {Fore.GREEN}waving{Style.RESET_ALL} at you.");choice=input(f"Approach him? ({Fore.GREEN}y{Style.RESET_ALL}/{Fore.RED}n{Style.RESET_ALL})\n>> ")
		if choice.lower()in['y',_w]:
			print(f"As you get closer, he pulls a {Fore.CYAN}card{Style.RESET_ALL} out of his jacket and shows it to you. It's a {Fore.GREEN}fake ID{Style.RESET_ALL}.");print(f"""
{Back.WHITE}{Fore.BLACK}——————————————————————————————————————————————{Style.RESET_ALL}
{Back.WHITE}{Fore.BLACK}|    /--\\     |                              |{Style.RESET_ALL}
{Back.WHITE}{Fore.BLACK}|    \\__/     |  NAME: JOHN SMITH            |{Style.RESET_ALL}
{Back.WHITE}{Fore.BLACK}|  _/    \\_   |  D.O.B: 9/11/01              |{Style.RESET_ALL}
{Back.WHITE}{Fore.BLACK}|   |    |    |  SEX: M                      |{Style.RESET_ALL}
{Back.WHITE}{Fore.BLACK}|——————————————                              |{Style.RESET_ALL}
{Back.WHITE}{Fore.BLACK}| ID: 841238800856874                        |{Style.RESET_ALL}
{Back.WHITE}{Fore.BLACK}| EYES: BRO                                  |{Style.RESET_ALL}
{Back.WHITE}{Fore.BLACK}| RACE: W                                    |{Style.RESET_ALL}
{Back.WHITE}{Fore.BLACK}| HEIGHT: 7' 25\"                             |{Style.RESET_ALL}
{Back.WHITE}{Fore.BLACK}——————————————————————————————————————————————{Style.RESET_ALL}
            """);print(f"He says he'll {Fore.GREEN}sell it to you{Style.RESET_ALL} for the low, low price of {Fore.YELLOW}50,000 credits{Style.RESET_ALL}. Hand him the money? ({Fore.GREEN}y{Style.RESET_ALL}/{Fore.RED}n{Style.RESET_ALL})");choice=input(_J)
			if choice.lower()in['y',_w]:
				if player_credits>=50000:print(f"You hand over the credits and {Fore.YELLOW}recieve the card{Style.RESET_ALL} in return.");fake_id=_A;player_credits-=50000;bonus_achievements[_v]=_A
				else:print(f"You want it, but you {Fore.RED}don't have enough money{Style.RESET_ALL}.")
			else:print('You back away without a word.')
		else:print('You carry on without stopping.')
	if random.randint(1,2)==2:
		n=random.randint(100,200)
		if n>=player_credits:n=player_credits-1
		player_credits-=n;print(f"As you leave, you notice your wallet {Fore.RED}feels {n} credits lighter{Style.RESET_ALL} than it did a minute ago...")
def visit_bank():
	global player_credits,loan_amount,loan_payment,has_loan,interest_percent,achievements,loans_total,loans_paid,luck;clear_screen()
	if not has_loan:
		while _A:
			clear_screen();print(f"Credits: {Fore.YELLOW}{player_credits:,}{Style.RESET_ALL}");print(f"Welcome to {Fore.BLUE}World Liberty Financial{Style.RESET_ALL}!\nType 'loan <amount>' for a loan");in_=input(_J)
			if len(in_.split(_C))==1:continue
			if in_.split(_C)[0]=='loan':
				amount=int(in_.split(_C)[1]);loan_amount=amount;arrest_chance=-1*(3.874*10**-11)*loan_amount**2+.0001111*loan_amount+18.87;arrest_chance-=4(luck);arrest_chance=int(arrest_chance)
				if loan_amount>=1434167:arrest_chance=99
				if fake_id and random.randint(0,100)<=arrest_chance:game_over(5)
				else:
					achievements[_a]=_A
					if loan_amount<=10:achievements[_b]=_A
					player_credits+=amount
					if len(str(amount))<8:interest_percent=.05
					else:interest_percent=.05+(len(str(amount))-7)*.05
					days_passed=0;loan_payment=amount;has_loan=_A;loans_total+=1
					if loans_total>=2:achievements[_d]=_A
					print(f"You took out a loan of {Fore.YELLOW}{amount:,}{Style.RESET_ALL} credits.")
					if not fake_id:print(f"Be prepared to pay it back in {Fore.YELLOW}three{Style.RESET_ALL} days.")
					input(f"\nPress {btn(_D)} to continue\n");return
	elif fake_id:return
	else:
		print(f"Time to pay your loan back.\nYour loan payment is {Fore.YELLOW}{loan_payment:,}{Style.RESET_ALL} credits");print('Credits:',player_credits);input(f"\nPress {btn(_D)} to continue\n")
		if player_credits>loan_payment:
			player_credits-=loan_payment;loans_paid+=1;has_loan=_B;achievements[_c]=_A
			if loans_paid==3:achievements[_e]=_A
			return
		else:loan_payment-=player_credits;player_credits=0
def sell_kidney():
	global kidneys,player_credits,spins;kidney_value=75000+random.randint(-2000,2000)
	if random.randint(1,2)==1:kidney='right'
	else:kidney='left'
	days_out=random.randint(5,10)
	for i in range(days_out):clear_screen();print(f"You decide to {Fore.GREEN}sell your {kidney} kidney{Style.RESET_ALL} to continue gambling.");print(f"You manage to get {Fore.YELLOW}{kidney_value:,}{Style.RESET_ALL} credits for it.");print(f"After {Fore.RED}{i} days in the hospital{Style.RESET_ALL}, you're back on your feet, itching for more {Fore.GREEN}gambling{Style.RESET_ALL}.");time.sleep(random.randint(10,20)/10)
	input(f"Press {btn(_D)} to continue.\n");spins+=days_out;player_credits+=kidney_value;kidneys=1;bonus_achievements[_u]=_A
def borrow_from_spouse():
	global has_borrowed,has_borrow,player_credits;clear_screen();borrow_amount=spins*1000
	if spouse==_y:print(f"You {Fore.RED}break away from the machine{Style.RESET_ALL} to call your husband. He says that he'll let you have {Fore.YELLOW}{borrow_amount:,}{Style.RESET_ALL} credits, but if you lose with them he'll {Fore.RED}leave you{Style.RESET_ALL}. Take his {Fore.YELLOW}deal{Style.RESET_ALL}?")
	if spouse==_K:print(f"You {Fore.RED}break away from the machine{Style.RESET_ALL} to call your wife. She says that she'll let you have {Fore.YELLOW}{borrow_amount:,}{Style.RESET_ALL} credits, but if you lose with them she'll {Fore.RED}leave you{Style.RESET_ALL}. Take her {Fore.YELLOW}deal{Style.RESET_ALL}?")
	option=input(f"({Fore.GREEN}y{Style.RESET_ALL}/{Fore.RED}n{Style.RESET_ALL}) >> ")
	if option.lower()in['','y']:
		if spouse==_y:print(f"You take his {Fore.YELLOW}money{Style.RESET_ALL}, determined to {Fore.GREEN}win it all{Style.RESET_ALL}.")
		if spouse==_K:print(f"You take her {Fore.YELLOW}money{Style.RESET_ALL}, determined to {Fore.GREEN}win it all{Style.RESET_ALL}.")
		has_borrow=_A;player_credits=borrow_amount;return
	else:print(f"You {Fore.RED}hang up{Style.RESET_ALL} and decide to go to the bank instead.");has_borrowed=_A;visit_bank()
def game_over(source):
	global spins,spouse,achievements;clear_screen()
	if spins!=1:s='s'
	else:s=''
	print(f"After {spins} day{s}...")
	if spouse==_K:end_text_0=f"""
{Fore.RED}You are broke :(
You lost your house
You lost your wife
She took the kids


Was it worth it?{Style.RESET_ALL}""";end_text_1=f"\n{Fore.GREEN}You made it out!\nYour wife is waiting outside for you.\nShe hugs you and says, \"I'm glad you're back.\"{Style.RESET_ALL}";end_text_2=f'\n{Fore.GREEN}You made it out!\nYour wife is waiting outside for you.\n{Fore.RED}She hands you a stack of papers\nShe says, "I want a divorce."{Style.RESET_ALL}';end_text_3=f"\n{Fore.RED}You lost the money your wife gave you! She calls, but you're too ashamed to pick up. You know it's over.{Style.RESET_ALL}"
	if spouse==_y:end_text_0=f"""
{Fore.RED}You are broke :(
You lost your house
You lost your husband
He took the kids


Was it worth it?{Style.RESET_ALL}""";end_text_1=f"\n{Fore.GREEN}You made it out!\nYour husband is waiting outside for you.\nHe hugs you and says, \"I'm glad you're back.\"{Style.RESET_ALL}";end_text_2=f'\n{Fore.GREEN}You made it out!\nYour husband is waiting outside for you.\n{Fore.RED}He hands you a stack of papers\nHe says, "I want a divorce."{Style.RESET_ALL}';end_text_3=f"\n{Fore.RED}You lost the money your husband gave you! He calls, but you're too ashamed to pick up. You know it's over.{Style.RESET_ALL}"
	end_text_4=f"{Fore.RED}Unfortunately, your reduced number of kidneys couldn't handle your diet, and you have perished.{Style.RESET_ALL}";end_text_5=f"{Fore.RED}Unfortunately, you got caught with a fake ID. You've been arrested and have no one to pay your bail. Guess that's it for you.{Style.RESET_ALL}"
	if source==0:print(end_text_0)
	elif source==1:print(f"{Fore.RED}You missed your loan payment by {Fore.YELLOW}{loan_payment:,}{Fore.RED} credits{Style.RESET_ALL}");print(end_text_0)
	elif source==2:
		achievements[_q]=_A;calculate_achievements();a=0
		for i in achievements.keys():
			if achievements[i]:a+=1
		try:p=round(100*(a/len(achievements)))
		except ZeroDivisionError:p=0
		if p>=100:print(end_text_1)
		if p<100:print(end_text_2)
	elif source==3:print(end_text_3)
	elif source==4:print(end_text_4)
	elif source==5:print(end_text_5)
	display_achievements()
	while _A:time.sleep(1)
clear_screen()
if IS_DEV_BUILD:print(f"Welcome to {Fore.CYAN}Gambling Simulator{Style.RESET_ALL} {Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}dev-1.12!{Style.RESET_ALL}\nThis is a developer build and may be {Fore.RED}unfinished or broken.{Style.RESET_ALL}\n\nPress {btn(_D)} to continue")
else:print(f"Welcome to {Fore.CYAN}Gambling Simulator{Style.RESET_ALL} {Style.BRIGHT}{Fore.LIGHTMAGENTA_EX}v1.12!{Style.RESET_ALL}\n\nPress {btn(_D)} to continue")
input('')
try:
	while is_running:
		achievements_start={};bonus_achievements_start={}
		for i in achievements.keys():achievements_start.update({i:achievements[i]})
		for i in bonus_achievements.keys():bonus_achievements_start.update({i:bonus_achievements[i]})
		a_before=0
		for i in achievements.keys():
			if achievements[i]:a_before+=1
		b_before=0
		for i in bonus_achievements.keys():
			if bonus_achievements[i]:b_before+=1
		clear_screen()
		if player_credits<0:player_credits=0
		if has_loan:
			loan_payment+=round(loan_payment*interest_percent)
			if days_passed==3:print('You need to pay back your loan!');print(f"Your loan payment is: {Style.BRIGHT}{Fore.RED}{loan_payment:,}{Style.RESET_ALL} credits");print(f"Credits: {Fore.YELLOW}{player_credits:,}{Style.RESET_ALL}")
			if days_passed==4:visit_bank()
			days_passed+=1
		if player_credits<=0:
			if not has_loan:
				print(f"You have no credits. Choose an option:");print("    'bank' to visit the bank")
				if not has_borrowed and spins>=10:print(f"    'borrow' to borrow from your {spouse}")
				if kidneys==2 and spins>=50:print("    'kidney' to sell a kidney")
				option=input(_J)
				if option=='bank':visit_bank()
				elif not has_borrowed and spins>=10:
					if option=='borrow':borrow_from_spouse()
				elif kidneys==2 and spins>=50:
					if option=='kidney':sell_kidney()
				else:game_over(0)
			else:
				clear_screen()
				if has_loan and days_passed>3:game_over(1)
		display_home_screen()
		if player_credits<0:player_credits=0
		clear_screen();bet=0
		if has_borrow:bet=player_credits;achievements[_L]=_A
		else:
			while bet<1 or not isinstance(bet,int)or bet>player_credits:
				try:
					print(f"Credits: {Fore.YELLOW}{player_credits:,}{Style.RESET_ALL}");bet=int(input(f"Bet: {Fore.YELLOW}"));print(Style.RESET_ALL)
					if bet>player_credits:print(f"{Fore.RED}You don't have enough money for that.{Style.RESET_ALL}")
					elif bet==player_credits:achievements[_L]=_A
					elif bet==0:print(_A1)
				except ValueError:print(_A1)
		clear_screen();print('Spinning...')
		if kidneys==1:time.sleep(6-speed_upgrades)
		else:time.sleep(5-speed_upgrades)
		spin_result=get_letters();spins+=1;reward=calculate_reward(spin_result,bet)
		if reward>0:
			if has_borrow:bonus_achievements[_t]=_A;has_borrow=_B;has_borrowed=_A
			print(f"{Fore.GREEN}Reward: {reward}{Style.RESET_ALL}")
			if bet==player_credits:achievements[_Y]=_A
			total_won+=reward
		else:
			print(f"{Fore.RED}You Lost!{Style.RESET_ALL}")
			if bet==player_credits:achievements[_Z]=_A
			if has_borrow:loss=bet;total_lost+=loss;game_over(3)
			if has_insurance:
				covered=int(round(.01*insurance_coverage*bet))
				if covered<=1:covered=1
				total_covered+=covered;print(f"Thankfully, your {Fore.GREEN}insurance{Style.RESET_ALL} covered "+f"{Fore.YELLOW}{covered:,}{Style.RESET_ALL}"+' credit'+('s'if covered>1 else'')+'.');loss=int(bet-covered)
			else:loss=bet
			total_lost+=loss;player_credits-=loss
		if has_insurance:
			player_credits-=insurance_payment
			if player_credits<0:player_credits=0;achievements[_m]=_A
		player_credits+=reward
		if player_credits<0:player_credits=0
		print(f"\nPress {btn(_D)} to continue");input('');clear_screen();calculate_achievements();has_unlocked_achievement=_B;a=0
		for i in achievements.keys():
			if achievements[i]:a+=1
		if a>a_before:has_unlocked_achievement=_A
		has_unlocked_bonus_achievement=_B;b=0
		for i in bonus_achievements.keys():
			if bonus_achievements[i]:b+=1
		if b>b_before:has_unlocked_bonus_achievement=_A
		if has_unlocked_achievement or has_unlocked_bonus_achievement:
			if has_unlocked_achievement:
				a=[]
				for i in achievements.keys():
					if achievements[i]!=achievements_start[i]:a.append(i)
				if a!=[]:
					for i in a:
						no_spaces=i.replace('_',_C);l=[];name=''
						for i in no_spaces.split():i.capitalize();l.append(i)
						for i in l:name+=f"{i.capitalize()} "
						print(f"{Fore.MAGENTA}Achievement Unlocked: {name}{Style.RESET_ALL}")
			if has_unlocked_bonus_achievement:
				b=[]
				for i in bonus_achievements.keys():
					if bonus_achievements[i]!=bonus_achievements_start[i]:b.append(i)
				if b!=[]:
					for i in b:
						no_spaces=i.replace('_',_C);l=[];name=''
						for i in no_spaces.split():i.capitalize();l.append(i)
						for i in l:name+=f"{i.capitalize()} "
						print(f"{Fore.CYAN}Bonus Achievement Unlocked: {name}{Style.RESET_ALL}")
			input(f"\n{btn(_D)} to continue\n")
		if total_won>=50000 and not is_high_roller:is_high_roller=_A;clear_screen();print(f"You can now visit the {Fore.MAGENTA}High Rollers club!{Style.RESET_ALL}");input(f"\n{btn(_D)} to continue\n")
		if player_credits<=0:0
		else:
			while _A:
				clear_screen()
				if spins>=25 and not fake_id and random.randint(1,4)==3:black_market()
				if not is_high_roller:print(f"Type 'shop' to visit the shop, 'insurance' to buy insurance, or '{Style.DIM}pass{Style.RESET_ALL}' to leave")
				else:print(f"Type 'shop' to visit the shop, 'insurance' to buy insurance, 'high roller' to visit the High Rollers club, or '{Style.DIM}pass{Style.RESET_ALL}' to leave")
				in_=input(_J)
				if in_=='shop':visit_shop();break
				if in_=='insurance':insurance_shop();break
				if in_=='high roller':high_rollers()
				if in_==_I:break
		try:del no_spaces,name,in_
		except:pass
		clear_screen()
except Exception as e:print(f"The developers are idiots. Report this in a strongly worded email to {Fore.MAGENTA}chloe@tobark.org{Style.RESET_ALL}:\n{e}")