class DayCounter:
    def dayStart(self, globals):
        local_globals = globals

        btn = local_globals["btn"]
        clear_screen = local_globals["clear_screen"]

        clear_screen()

        print("Day:", local_globals["days"])

        input(f"\nPress {btn('enter')} to continue\n")

        return local_globals

    def __str__(self):
        return "DayCounter"

    def name(self, globals):
        return "DayCounter"

    def description(self, globals):
        return "Adds a day counter at the beginning of each day"