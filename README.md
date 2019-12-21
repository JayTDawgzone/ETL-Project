# ETL-Project
In this project I explored the ETL (Extract, Transform, Load) process with Pokemon data, and then created an API.


## Extracting Data
The data sources I used were [PokeAPI.co](https://pokeapi.co) and [PokemonTCG.io](https://pokemontcg.io/). My goal was to combine trading card game data with data from the console games to create a unique dataset.

First, I pulled data from PokemonTCG. PokemonTCG has an SDK available that could be imported into my application. Every single Pokemon card was pulled into a dataframe. The dataframe had almost 12,000 Pokemon cards.



The PokemonTCG dataset had a National Pokedex Number that I knew would allow me to merge data with the PokeAPI data later. The PokeAPI endpoint also requires a Pokedex ID in its queries. Knowing this, I created a list of unique National Pokedex Numbers. The unique National Pokedex Numbers were then used to make queries to PokeAPI.




The PokemonTCG data was then left-joined by the PokemonAPI data on the National Pokedex Number. The resulting dataframe had every single Pokemon card with its corresponding console game data.

```
card_name                      10078 non-null object
card_id                        10078 non-null object
national_pokedex_number        10078 non-null float64
image_url                      10078 non-null object
image_url_hi_res               10078 non-null object
card_subtype                   10078 non-null object
card_ability                   2388 non-null object
card_ancient_trait             39 non-null object
card_hp                        10069 non-null object
card_number                    10078 non-null object
card_artist                    9984 non-null object
card_rarity                    9840 non-null object
card_series                    10078 non-null object
card_set                       10078 non-null object
card_set_code                  10078 non-null object
card_converted_retreat_cost    9895 non-null float64
card_text                      1247 non-null object
card_types                     10078 non-null object
card_attacks                   10039 non-null object
card_weaknesses                9799 non-null object
card_resistances               3314 non-null object
card_evolves_from              4265 non-null object
sprite                         10034 non-null object
pokemon_name                   10063 non-null object
pokemon_weight                 10063 non-null float64
pokemon_height                 10063 non-null float64
speed                          10063 non-null float64
special_defense                10063 non-null float64
special_attack                 10063 non-null float64
defense                        10063 non-null float64
attack                         10063 non-null float64
hp                             10063 non-null float64
pokemon_type1                  10063 non-null object
pokemon_type2                  5030 non-null object
base_hapiness                  10063 non-null float64
color_group                    10063 non-null object
egg_group                      10063 non-null object
generation                     10063 non-null object
shape                          10063 non-null object
```

## Transforming Data


The first thing I noticed about my dataframe was that some rows had dictionaries in them. For example, each row in the 'card_attacks' column will generally have a list containing a dictionary of attack moves. This was a relief to me because I wouldn't have to do much data cleaning. If the multiple attack moves were stored as comma separated values, I would have had to spend much more time cleaning the data.  The only data cleaning I had to do was to remove all non-Pokemon card types from the datafrane so the two datasets would merge properly.


Overall, the data sources I used had relatively clean data and I didn't spend much time on making it perfect.

## Loading Data

I wasn't sure which type of database to use for my project, so I tried both.

The database would need to provide me:

* A table (or document) for each Pokemon with every card (and card data) associated with that Pokemon
* A table (or document) for each Card with the Pokemon (and Pokemon data) associated with that Card.


First, I tried a SQL database. I knew both datasets had a relationship by their National Pokedex Number so I thought it would be a smart choice for my data. However, I found creating tables to be a painful experience and it seemed unnecessary. As I was working with the SQL database a clearer picture came into my head of how I wanted to present the data and I decided to switch to MongoDB.


Using MongoDB, the setup process was immensely easier. For the Card tables, I was able to loop through each row of the merged dataframe and create dictionaries from each row. Each row was then converted into a document and inserted into the card collection. For the Pokemon documents, I used a similar process of looping through rows that contained the Pokemon's name and creating dictionaries of each row.


## Flask App & API

The Flask app I created for this project is my first attempt at making an API, and I definitely learned a lot from it. I wanted to test what I have learned so far and create something useful out of the database I had created.

While making the Flask app there were a few features I had in mind:

* Create a web app to browse data
* Web app must have a route for each Pokemon and Card
* Create an endpoint that returns json data for each Pokemon and Card

I followed a few tutorials online and was able to create the application with reasonable success.
##### Pokemon.html Example
![pokemon](/images/pokemon.PNG)
##### Endpoint Example
![API](/images/api.PNG)



## Issues & Troubleshooting

This project was pretty straight-forward until I tried using the data that I had stored in my database. I had created a cute web app that displays Pokemon & Pokemon Card information and was pretty satisfied with my work. However, I realized I needed to rethink my database structure when I was creating the pokemon.html file.

The way I had structured each document did not allow for nested loops in jinja2. This meant that I couldn't add an anchor tag to each Pokemon card Image that showed up in the /pokemon/pokemon_name route. The anchor tag was supposed to be attached to each Pokemon Card image and route the user to the /card/card HTML page. This was a very important feature to me and the issue could have been avoided if the document had been structured differently.

Some other tasks I wish I could have accomplished are:

* Replacing card energy data with images so they look better  <img src="images/pokemon_energy_detailed_symbols_by_dbizal_ddihkfk-fullview.png" width="75" height="50" />
* Proper case Pokemon names
* Incorporate card market value to the dataset
* Incorporate top-tier decklists from [LimitlessTCG.com](https://limitlesstcg.com/decks/)


## Conclusion

Overall, I have learned that choosing the correct database for your project from the beginning, and structuring your data correctly, can save you copious amounts of time in the future. I will take what I've learned from this project and spend more time understanding the data that I'm working with before going head-first into my next project.
