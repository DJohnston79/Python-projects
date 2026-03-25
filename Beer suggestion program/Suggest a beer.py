# Comprehensive Beer Pairing Script 
# Based on: Different Types & Styles of Beer: The Ultimate Guide

# Nested dictionaries of beer types with examples and info from the guide
lager_pils = {
    'american_lager': {
        'color': 'light_gold',
        'abv': ['3.2', '4.0'],
        'ibu': ['5', '15'],
        'examples': ['Budweiser', 'Coors', 'Pabst'],
        'food_pair': ['spicy', 'american', 'muenster_cheese'],
        'serving_temp': ['30', '40'],
    },
    'german_helles': {
        'color': 'bright_gold',
        'abv': ['4.8', '5.6'],
        'ibu': ['18', '25'],
        'examples': ['Victory Helles Lager', 'Stoudts Gold Lager'],
        'food_pair': ['german', 'pork', 'brie'],
        'serving_temp': ['40', '45'],
    },
    'german_pilsner': {
        'color': 'pale-gold',
        'abv': ['4.6', '5.3'],
        'ibu': ['25', '40'],
        'examples': ['Tröegs Sunshine Pils', 'Sierra Nevada Nooner Pilsner'],
        'food_pair': ['german', 'poultry', 'fish', 'spicy_cheese'],
        'serving_temp': ['40', '45'],
    },
    'bohemian_pilsner': {
        'color': 'pale-yellow',
        'abv': ['4.1', '5.1'],
        'ibu': ['30', '45'],
        'examples': ['Lagunitas Pils', 'Dogfish Head Piercing Pils'],
        'food_pair': ['spicy', 'asian', 'mild_cheese'],
        'serving_temp': ['40', '45'],
    }
}

dark_lagers = {
    'amber_lager': {
        'color': 'gold-copper',
        'abv': ['4.8', '5.4'],
        'ibu': ['18', '30'],
        'examples': ['Yuengling Lager', 'Brooklyn Lager'],
        'food_pair': ['burgers', 'grilled_chicken', 'white_cheddar'],
        'serving_temp': ['45', '50'],
    },
    'oktoberfest': {
        'color': 'amber-red',
        'abv': ['5.1', '6.0'],
        'ibu': ['18', '25'],
        'examples': ['Samuel Adams Octoberfest', 'Great Lakes Oktoberfest'],
        'food_pair': ['veggies', 'meat', 'pork', 'chicken'],
        'serving_temp': ['45', '50'],
    }
}

ales = {
    'american_pale_ale': {
        'color': 'deep-golden',
        'abv': ['4.4', '5.4'],
        'ibu': ['30', '50'],
        'examples': ['Sierra Nevada Pale Ale', 'Oskar Blues Dale\'s Pale Ale'],
        'food_pair': ['spicy', 'burgers', 'pepper_jack'],
        'serving_temp': ['45', '50'],
    },
    'american_ipa': {
        'color': 'gold-copper',
        'abv': ['6.3', '7.5'],
        'ibu': ['50', '70'],
        'examples': ['Lagunitas IPA', 'Stone IPA'],
        'food_pair': ['spicy', 'curry', 'strong_blue_cheese'],
        'serving_temp': ['45', '50'],
    },
    'imperial_double_ipa': {
        'color': 'gold-copper',
        'abv': ['7.0', '14.0'],
        'ibu': ['65', '100'],
        'examples': ['Russian River Pliny the Elder', 'Dogfish Head 90 Minute IPA'],
        'food_pair': ['sharp_cheddar', 'smoked_beef', 'sweet_desserts'],
        'serving_temp': ['40', '45'],
    },
    'american_stout': {
        'color': 'black',
        'abv': ['5.0', '7.0'],
        'ibu': ['35', '60'],
        'examples': ['Highland Black Mocha Stout', 'Bell\'s Kalamazoo Stout'],
        'food_pair': ['heavy_foods', 'meat', 'oysters', 'chocolate', 'brie'],
        'serving_temp': ['45', '50'],
    }
}

wheat_wild_specialty = {
    'belgian_witbier': {
        'color': 'pale-straw',
        'abv': ['4.8', '5.2'],
        'ibu': ['10', '17'],
        'examples': ['Blue Moon', 'Hoegaarden'],
        'food_pair': ['seafood', 'citrus_salads', 'mascarpone'],
        'serving_temp': ['40', '45'],
    },
    'berliner_weisse': {
        'color': 'straw',
        'abv': ['2.8', '3.4'],
        'ibu': ['3', '6'],
        'examples': ['Dogfish Head Festina Peche', 'Freetail Yo Soy'],
        'food_pair': ['fruit', 'aged_ham', 'havarti'],
        'serving_temp': ['40', '45'],
    },
    'smoked_beer': {
        'color': 'varies',
        'abv': ['varies'],
        'ibu': ['varies'],
        'examples': ['Ithaca Gorges Smoked Porter', 'Goose Island Prairie Smoke'],
        'food_pair': ['roasted_vegetables', 'bbq', 'smoked_meats'],
        'serving_temp': ['50', '55'],
    }
}

logging_active = True

while logging_active:
    name = input("\nWhat is your name? ")
    print("Hello", name.title())
    
    prompt = "\nPlease select a food category: "
    prompt += "\ngerman, mexican, meat, veggies, spicy_cheese, poultry, fish, pork, brie, "
    prompt += "american, spicy, asian, burgers, curry, seafood, fruit, bbq, chocolate.\n> "

    response = input(prompt).lower()
    
    if response == 'german':
        print("I suggest you try a German Helles, a German Pilsner, or an Oktoberfest.") [cite: 2]
        
    elif response == 'veggies':
        print("Veggies pair well with Oktoberfest Beers.") [cite: 2]
        if input("Would you like a list of Oktoberfest beers? ").lower() == 'yes':
            print(dark_lagers['oktoberfest']['examples'])
        
        if input("Would you like more details (abv, serving temp)? ").lower() == 'yes':
            print(f"ABV: {dark_lagers['oktoberfest']['abv']}%, Serving Temp: {dark_lagers['oktoberfest']['serving_temp']}F.") [cite: 2]

    elif response == 'meat' or response == 'heavy_foods':
        print("I suggest an American Stout or an Oktoberfest.") [cite: 2]
        if input("See Stout details? ").lower() == 'yes':
            print(f"ABV: {ales['american_stout']['abv']}%, Examples: {ales['american_stout']['examples']}") [cite: 2]

    elif response in ['poultry', 'fish', 'spicy_cheese']:
        print("A German Pilsner is a great choice.") [cite: 2]
        if input("See examples? ").lower() == 'yes':
            print(lager_pils['german_pilsner']['examples'])

    elif response in ['spicy', 'asian']:
        print("Try an American Lager or a Bohemian Pilsner.") [cite: 2]

    elif response in ['burgers', 'american']:
        print("An American Pale Ale or Amber Lager pairs well with burgers.") [cite: 2]

    elif response in ['seafood', 'fruit']:
        print("Try a Belgian Witbier or a Berliner Weisse.") [cite: 2]

    elif response == 'bbq':
        print("A Smoked Beer is highly recommended for BBQ.") [cite: 2]

    elif response == 'chocolate' or response == 'oysters':
        print("An American Stout is the perfect pairing.") [cite: 2]

    else:
        print("Please make a choice from the list.")
        continue 
          
    repeat = input("\nWould anybody else like suggestions? (yes/no) ").lower()
    if repeat == 'no':
        logging_active = False
