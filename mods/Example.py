class Example: # entire mod 
    # metadata methods
    def __str__(self): # mod name, plaintext
        return "Example" # expects string to be returned
    
    def name(self, globals): # mod name, formatting optional
        local_globals = globals # grab global vars from main
        Fore = local_globals["Fore"] # define colorama Fore to use for formatting (optional)
        Style = local_globals["Style"] # define colorama Style to use for formatting (optional)

        return f"{Fore.GREEN}Example{Style.RESET_ALL}" # expects string to be returned

    def description(self, globals): # mod description, formatting optional
        local_globals = globals # grab global vars from main
        Fore = local_globals["Fore"] # define colorama Fore to use for formatting (optional)
        Style = local_globals["Style"] # define colorama Style to use for formatting (optional)

        return f"{Fore.BLUE}Mod template{Style.RESET_ALL}" # expects string to be returned



    # scripting methods
    def onRun(self, globals): # on first load
        local_globals = globals # grab global vars from main

        btn = local_globals["btn"] # define btn function to print button prompts (optional)
        clear_screen = local_globals["clear_screen"] # define function to clear screen (optional)

        Fore = local_globals["Fore"] # define colorama Fore to use for formatting (optional)
        Style = local_globals["Style"] # define colorama Style to use for formatting (optional)

        # run code here

        return local_globals # expects local_globals to be returned

    def dayStart(self, globals): # beginning of every day
        local_globals = globals # grab global vars from main

        btn = local_globals["btn"] # define btn function to print button prompts (optional)
        clear_screen = local_globals["clear_screen"] # define function to clear screen (optional)

        Fore = local_globals["Fore"] # define colorama Fore to use for formatting (optional)
        Style = local_globals["Style"] # define colorama Style to use for formatting (optional)

        # run code here

        return local_globals # expects local_globals to be returned

    def dayEnd(self, globals): # end of every day
        local_globals = globals # grab global vars from main

        btn = local_globals["btn"] # define btn function to print button prompts (optional)
        clear_screen = local_globals["clear_screen"] # define function to clear screen (optional)

        Fore = local_globals["Fore"] # define colorama Fore to use for formatting (optional)
        Style = local_globals["Style"] # define colorama Style to use for formatting (optional)

        # run code here

        return local_globals # expects local_globals to be returned



    # text methods
    def barAction(self, globals): # actions for bartender
        local_globals = globals # grab global vars from main
        Fore = local_globals["Fore"] # define colorama Fore to use for formatting (optional)
        Style = local_globals["Style"] # define colorama Style to use for formatting (optional)

        return ["Example", f"{Fore.RED}Colored Example{Style.RESET_ALL}"] # expects list of strings to be returned

    def barDialogue(self, globals): # dialogue for bartender
        local_globals = globals # grab global vars from main
        Fore = local_globals["Fore"] # define colorama Fore to use for formatting (optional)
        Style = local_globals["Style"] # define colorama Style to use for formatting (optional)

        return ["Example", f"{Fore.RED}Colored Example{Style.RESET_ALL}"] # expects list of strings to be returned

    def flavorText(self, globals): # flavor text for home screen
        local_globals = globals # grab global vars from main
        Fore = local_globals["Fore"] # define colorama Fore to use for formatting (optional)
        Style = local_globals["Style"] # define colorama Style to use for formatting (optional)

        return [{"days_start": 0, "days_end": 1, "text": "Example", "displayed": False}] # expects list of dicts to be returned

    

    # item methods
    def barItem(self): # adds purchaseable items to bar
        return [{"name": "Cocktail", "stat": "days", "description": "Days", "change": 3, "price": 200, "maximum": -1}] # expects list of dicts to be returned