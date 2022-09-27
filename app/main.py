def calculate_team_total_rating(team_config: list) -> int:
    team_rating = 0
    for hero in team_config:
        team_rating += hero.get_rating()

    return team_rating


def elves_concert(elves: list) -> None:

    for elf in elves:
        elf.play_elf_song()


def feast_of_the_dwarves(dwarves: list) -> None:

    for dwarf in dwarves:
        dwarf.eat_favourite_dish()
