# A programme to recommend a next film to watch based on word vector similarity
# between the descriptions of a most recently watched film and a range of
# candidate films.


# =================================== IMPORTS =================================

# Importing spaCy and its more sophisticated English language model.
import spacy
nlp = spacy.load('en_core_web_md')


# ================================== FUNCTIONS ================================

# Takes a film description as argument.  Reads in descriptions of various films
# from text file and saves to a list.  Compares description in argument to each
# description in list and reads semantic similarity comparisons into a list.
# Identifies largest value in list of similarity ratings and prints
# recommendation for film at the same index in the film list.
def get_rec(description):
    with open("movies.txt", "r") as f:
        films = []
        for line in f:
            film = line
            films.append(film)
        
    token = nlp(description)

    sim_ratings = []
    for token_ in films:
        token_ = nlp(token_)
        sim_rating = float(token.similarity(token_))
        sim_ratings.append(f"{sim_rating}")

    highest_rating = max(sim_ratings)
    for i in sim_ratings:
        if i == highest_rating:
            film_index = sim_ratings.index(i)

    recommended_film_full = films[film_index]
    recommended_film_title = recommended_film_full[0:7]

    print(f"You should next watch {recommended_film_title}.")


# ================================== PROGRAMME ================================

# Runs film recommendation function with description of Planet Hulk as
# argument.
planet_hulk = ("Will he save their world or destroy it? When the Hulk becomes "
              "too dangerous for the Earth, the Illuminati trick Hulk into a "
              "shuttle and launch him into space to a planet where the Hulk "
              "can live in peace. Unfortunately, Hulk land on the planet "
              "Sakaar where he is sold into slavery and trained as a "
              "gladiator.")

print()
get_rec(planet_hulk)
print()