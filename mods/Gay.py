class Gay:
    def onRun(self, globals):
        local_globals = globals

        btn = local_globals["btn"]
        clear_screen = local_globals["clear_screen"]

        local_globals["spouse"] = "husband"

        return local_globals
    
    def __str__(self):
        return "GayMod"
        
    def description(self, globals):
        return "Makes you gay"

    def name(self, globals):
        local_globals = globals
        Fore = local_globals["Fore"]
        Style = local_globals["Style"]

        return f"{Fore.RED}G{Fore.YELLOW}a{Fore.GREEN}y{Fore.BLUE}M{Fore.MAGENTA}o{Fore.MAGENTA}{Style.DIM}d{Style.RESET_ALL}"