import pokemon


def calculate_bmi(weight, height):
    return round(weight / height ** 2, 2)


def get_health_feedback(bmi):
    if bmi < 18:
        return 'underweight'
    elif bmi < 25:
        return 'ideal weight for height'
    else:
        return 'overweight'


if __name__ == '__main__':
    pokemon = pokemon.get_random_pokemon()
    pokemon_bmi = calculate_bmi(pokemon['Weight'], pokemon['Height'])
    print(f"The BMI of {pokemon['Name']} is {get_health_feedback(pokemon_bmi)} when compared to human standards.")
