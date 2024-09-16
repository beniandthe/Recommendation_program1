#Testflix - a movie search algorithm that searches different types of movies and returns movies in aplhabetical order
#or searches movies based on name and returns a list with closest name
#Make a graph with genre as vertices and edges as the movies. The weight of the edges will be the similarity between the movies
#The graph will be directed because the similarity between two movies can be different
#The graph will use a depth-first search to find the shortest path between two movies starting with the type of movie

#Using user input, the program will search for movies based on the type of movie. 
#The program will then return a list of movies in alphabetical order.
#The program will then accept inout to either select a movie or try a different search
#If a movie is selected, the program will return that movie plus a list of movies that are similar to the selected movie
#The program will then accept input to either select a movie or try a different search
from typing import Any
from graph_class import Graph
from movie_list import movie_graph


# populate a list of genres and a printable list of genre choices   
genre_list = ['Action', 'Animated', 'Comedy', 'Crime', 'Drama', 'Fantasy', 'Historical', 'Horror', 'Romance', 'Sci-Fi', 'Thriller', 'Western' ]
read_list = ""
for word in genre_list:
    read_list += word + "\n"
    
# intro message
def greeting():
    print("""          *******   ******    ****  *******  ******   *        *   *      *    
                  *      *        *         *     *        *        *     *   *
                  *      *****     ***      *     ****     *        *       *
                  *      *            *     *     *        *        *     *   * 
                  *      ******   ****      *     *        ******   *    *     *
          
          \n\n""")
    print("""Welcome to Testflix! The best movie search algorithm in the world! 
        \nYou can search for movies by name, genre, or year. You can also search for movies that are similar to a specific movie. Let's get started!""")
 


    
# Get user input for 1 or more genres.    
def get_genres():
    user_input = []
    genre_choice = input("\nPlease enter genres separated by commas from the list below: \n\n" + "**************\n" + read_list + "**************\n\n")
    # split the user input by commas
    choices = genre_choice.split(",")
    for item in choices:
        if item.strip() in genre_list:
            user_input.append(item.strip())
        else:
            print("\nInvalid choice.")
            break
    print("\nSearching movies in the following genres: ")
    for item in user_input:
        print(item)
    return user_input

def display_movies(graph, first_choice):
    movies = graph.graph_dict[first_choice].edges
    print("Here are some movies in the genre: ")
    for movie in movies:
        print(movie)




            
    
    
    
    
def main():
    greeting()
    get_genres()
    
    
    
main()

    

