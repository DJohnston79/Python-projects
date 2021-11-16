 #code to be edited later once I get to it


#nested dictionaries of beer types with examples and info
lager_pils = {
    'american_lager': {
        'color': 'light_gold',
        'abv': ['3.2', '4.0'],
        'ibu': ['5', '15'],
        'examples': ['budweiser', 'coors', 'pabst'],
        'food_pair': ['spicy', 'american'],
        'serving_temp': ['30', '40'],
        },

    'german_helles': {
        'color': 'bright_gold',
        'abv': ['4.8', '5.6'],
        'ibu': ['18', '25'],
        'examples': ['victory_helles_lager', 'stoudts_gold_lager'],
        'food_pair': ['german', 'pork', 'brie'],
        'serving_temp': ['40', '45'],
        },

    'german_pilsner': {
        'color': 'pale-gold',
        'abv': ['4.6', '5.3'],
        'ibu': ['25', '40'],
        'examples': ['tröegs_sunshine_pils', 'sierra_nevada_nooner_pilsner'],
        'food_pair': [' german', 'poultry', 'fish', 'spicy_cheese'],
        'serving_temp': ['40', '45'],
        },

    'bohemian pilsner': {
        'color': 'pale-yellow',
        'abv': ['4.1', '5.1'],
        'ibu': ['30', '45'],
        'examples': ['Lagunitas_pils', 'dogfish_head_piercing_pils'],
        'food_pair': ['spicy', 'asian', 'sharp_cheddar'],
        'serving_temp': ['40', '45'],
        },
    }

dark_lagers = {
    'amber_american': {
        'color': 'caramel',
        'abv': ['4.8', '5.4'],
        'ibu': ['18', '30'],
        'examples': ['yuengling_lager', 'samuel_adams_boston_lager'],
        'food_pair': ['american', 'poultry', 'beef', 'cheddar'],
        'serving_temp': ['45', '50'],
        },

    'oktoberfest': {
        'color': 'copper',
        'abv': ['5.1', '6.0'],
        'ibu': ['18', '25'],
        'examples': ['paulaner_oktoberfest-märzen', 'victory_brewing_company_festbier'],
        'food_pair': ['german', 'meat', 'veggies', 'spicy_cheese'],
        'serving_temp': ['45', '50'],
        },

    'german_schwarzbier': {
        'color': 'brown',
        'abv': ['3.8', '4.9'],
        'ibu': ['22', '30'],
        'examples': ['shiner_bohemian_black_lager', 'guinness_black_lager'],
        'food_pair': ['german', 'spicy', 'muenster_cheese'],
        'serving_temp': ['40', '45'],
        },

    'vienna_lager': {
        'color': 'red',
        'abv': ['4.5', '5.5'],
        'ibu': ['22', '28'],
        'examples': ['dos_equis_amber_lager', 'great_lakes_eliot_ness', 'blue_point_toasted_lager'],
        'food_pair': ['german', 'mexican', 'spicy_cheese'],
        'serving_temp': ['40', '45'],
        },
    }

german_bocks = {
    'traditional_bock': {
        'color': 'dark_copper',
        'abv': ['6.3', '7.5'],
        'ibu': ['20', '30'],
        'examples': ['samuel_adams_winter_lager', 'great_lakes_rockfeller_bock'],
        'food_pair': ['german_cuisine', 'meat', 'vegetables', 'chocolate', 'camembert_cheese'],
        'serving_temp': ['40', '45'],
    }
}


    
        


# Set a flag to indicate that logging is active.
logging_active = True

while logging_active:
    prompt = "Hello. I can help you choose a beer. "
    prompt += "Please type 'quit' when finished. "
    prompt += "\nFirst question: How old are you ?  "
    age = input(prompt)
    age = int(age)

    if age <= 20:
        print("Sorry. you are not old enough. ")
        break 
        

    else:
        print("Okay. Let's continue.")

    name = input("\nWhat is your name? ")

    print("Hello", name.title())
    
    prompt = "Please select one of the following: "

    prompt += "\ngerman, mexican, meat, veggies, spicy_cheese, poultry, beef, cheddar, pork, brie, american, spicy, muenster_cheese.\n>"

    response = input((prompt))
    response = response.lower()
    
    if response == 'german':
        #if using ftring, will have to reference dictionary of beers somehow 
        print("I suggest you try a German Helles, a German Pilsner, or an Octoberfest.")
        
    elif response == 'veggies':
      print("Veggies pair well with Oktoberfest Beers.")
      prompt = "Would you like a list of Oktoberfest beers?"
      answer = input((prompt))
      answer = answer.lower()
      if answer == 'yes':
          print(dark_lagers['oktoberfest']['examples'])
    

      else:
          print("Okay then.")
    
    

      details = input("Would you like more details about this beer, such as serving temp, abv, etc? yes/no ")
      
     

      details = details.lower()

      if details == 'yes':
          print('The abv is' + str(dark_lagers['oktoberfest']['abv']))

      else:
          print("Okay then.")
    #safguard against no selection
    else:
      print("Please make a choice.") 
      continue 
          
            

    

    #See if anyone else needs beer suggestions
    repeat = input("Would anybody else like suggestions?  (yes/ no) ")
    if repeat == 'no':
        logging_active = False
        # Logging is complete. Show the results
        
