    def match_funct(choice:int):
        match choice:
            case 1:
                pass

    def run_dungeon():
    
        while True:
            print('<|Manage The Dungeon|>'.center(40," "))
            print('[1] Add items to the dungeon')
            print('[2] View items in the dungeon')
            print('[3] Let the hero enter the dungeon.')
            print('[0] Close the dungeon.')
            choice = input('Choice : ')
            match_funct(choice)