#using genre list, make a vertex for each genre
#add edges to each genre vertex for similar genres

from vertex_class import Vertex
from graph_class import Graph
# Create instances of Vertex for each genre
action = Vertex("Action")
thriller = Vertex("Thriller")
scifi = Vertex("Sci-Fi")
adventure = Vertex("Adventure")
comedy = Vertex("Comedy")
romance = Vertex("Romance")
horror = Vertex("Horror")
fantasy = Vertex("Fantasy")
western = Vertex("Western")
historical = Vertex("Historical")
crime = Vertex("Crime")
animated = Vertex("Animated")
drama = Vertex("Drama")

#create a graph of genres as vertices
movie_graph = Graph(False)
movie_graph.add_vertex(action)
movie_graph.add_vertex(thriller)
movie_graph.add_vertex(scifi)
movie_graph.add_vertex(adventure)
movie_graph.add_vertex(comedy)
movie_graph.add_vertex(romance)
movie_graph.add_vertex(horror)
movie_graph.add_vertex(fantasy)
movie_graph.add_vertex(western)
movie_graph.add_vertex(historical)
movie_graph.add_vertex(crime)
movie_graph.add_vertex(animated)
movie_graph.add_vertex(drama)

movie_graph.add_edge(action, thriller)
movie_graph.add_edge(action, scifi)
movie_graph.add_edge(action, adventure)
movie_graph.add_edge(action, comedy)
movie_graph.add_edge(action, romance)
movie_graph.add_edge(action, fantasy)
movie_graph.add_edge(action, western)
movie_graph.add_edge(action, historical)
movie_graph.add_edge(action, crime)
movie_graph.add_edge(action, animated)
movie_graph.add_edge(action, drama)

movie_graph.add_edge(thriller, scifi)
movie_graph.add_edge(thriller, fantasy)
movie_graph.add_edge(thriller, western)
movie_graph.add_edge(thriller, historical)
movie_graph.add_edge(thriller, crime)
movie_graph.add_edge(thriller, drama)

movie_graph.add_edge(scifi, adventure)
movie_graph.add_edge(scifi, comedy)
movie_graph.add_edge(scifi, romance)
movie_graph.add_edge(scifi, fantasy)
movie_graph.add_edge(scifi, western)
movie_graph.add_edge(scifi, historical)
movie_graph.add_edge(scifi, crime)
movie_graph.add_edge(scifi, animated)
movie_graph.add_edge(scifi, drama)

movie_graph.add_edge(adventure, comedy)
movie_graph.add_edge(adventure, romance)
movie_graph.add_edge(adventure, fantasy)
movie_graph.add_edge(adventure, western)
movie_graph.add_edge(adventure, historical)
movie_graph.add_edge(adventure, crime)
movie_graph.add_edge(adventure, animated)
movie_graph.add_edge(adventure, drama)

movie_graph.add_edge(comedy, romance)
movie_graph.add_edge(comedy, fantasy)
movie_graph.add_edge(comedy, western)
movie_graph.add_edge(comedy, historical)
movie_graph.add_edge(comedy, crime)
movie_graph.add_edge(comedy, animated)
movie_graph.add_edge(comedy, drama)

movie_graph.add_edge(romance, fantasy)
movie_graph.add_edge(romance, western)
movie_graph.add_edge(romance, historical)
movie_graph.add_edge(romance, crime)
movie_graph.add_edge(romance, animated)
movie_graph.add_edge(romance, drama)

movie_graph.add_edge(fantasy, western)
movie_graph.add_edge(fantasy, historical)
movie_graph.add_edge(fantasy, crime)
movie_graph.add_edge(fantasy, animated)
movie_graph.add_edge(fantasy, drama)

movie_graph.add_edge(western, historical)
movie_graph.add_edge(western, crime)
movie_graph.add_edge(western, animated)
movie_graph.add_edge(western, drama)

movie_graph.add_edge(historical, crime)
movie_graph.add_edge(historical, animated)
movie_graph.add_edge(historical, drama)

movie_graph.add_edge(crime, animated)
movie_graph.add_edge(crime, drama)

movie_graph.add_edge(animated, drama)

# Print the graph
for key in movie_graph.graph_dict:
    print(key)
    print(movie_graph.graph_dict[key].edges)





# Add edges to each genre vertex for similar genres



