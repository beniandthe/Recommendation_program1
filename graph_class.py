
from random import randrange

class Graph:
  def __init__(self, directed = False):
    self.graph_dict = {}
    self.directed = directed

  def add_vertex(self, vertex):
    self.graph_dict[vertex.value] = vertex

  def add_edge(self, from_vertex, to_vertex, weight = 0):
    self.graph_dict[from_vertex.value].add_edge(to_vertex.value, weight)
    if not self.directed:
      self.graph_dict[to_vertex.value].add_edge(from_vertex.value, weight)

  def find_path(self, start_vertex, end_vertex):
    start = [start_vertex]
    seen = {}
    while len(start) > 0:
      current_vertex = start.pop(0)
      seen[current_vertex] = True
      print("Visiting " + current_vertex)
      if current_vertex == end_vertex:
        return True
      else:
        vertices_to_visit = set(self.graph_dict[current_vertex].edges.keys())
        start += [vertex for vertex in vertices_to_visit if vertex not in seen]
    return False

  def print_graph(graph):
    for vertex in graph.graph_dict:
        print("")
        print(vertex + " connected to")
        vertex_neighbors = graph.graph_dict[vertex].edges
        if len(vertex_neighbors) == 0:
            print("No edges!")
        for adjacent_vertex in vertex_neighbors:
            print("=> " + adjacent_vertex)
            
    def seen(self, start_vertex, end_vertex):
      start = [start_vertex]
      seen = {}
      while len(start) > 0:
        current_vertex = start.pop(0)
        seen[current_vertex] = True
        print("Visiting " + current_vertex)
        if current_vertex == end_vertex:
          return True
        else:
          vertices_to_visit = set(self.graph_dict[current_vertex].edges.keys())
          start += [vertex for vertex in vertices_to_visit if vertex not in seen]
        return False
            
    def find_path(self, start_vertex, end_vertex, path = []):
      while len(start) > 0:
        current_vertex = start.pop(0)
        path += [current_vertex]
        if current_vertex == end_vertex:
          return path
        if current_vertex not in seen:
          seen[current_vertex] = True
          vertices_to_visit = set(self.graph_dict[current_vertex].edges.keys())
          start += [vertex for vertex in vertices_to_visit if vertex not in seen]
          return False
      return None
    
  def find_all_paths(self, start_vertex, end_vertex, path = []):    
    path = path + [start_vertex]
    if start_vertex == end_vertex:
      return [path]
    if start_vertex not in self.graph_dict:
      return []
    paths = []
    for vertex in self.graph_dict[start_vertex].edges:
      if vertex not in path:
        extended_paths = self.find_all_paths(vertex, end_vertex, path)
        for p in extended_paths: 
          paths.append(p)
    return paths
  
 
          
    def shortest_path(self, start_vertex, end_vertex, path = []):
      start = [start_vertex]
      while len(start) > 0:
        current_vertex = start.pop(0)
        path += [current_vertex]
        if current_vertex == end_vertex:
          return path
        if current_vertex not in seen:
          seen[current_vertex] = True
          vertices_to_visit = set(self.graph_dict[current_vertex].edges.keys())
          start += [vertex for vertex in vertices_to_visit if vertex not in seen]
          return False
        return None
    
    def longest_path(self, start_vertex, end_vertex, path = []):
      start = [start_vertex]
      while len(start) > 0:
        current_vertex = start.pop(0)
        path += [current_vertex]
        if current_vertex == end_vertex:
          return path
        if current_vertex not in seen:
          seen[current_vertex] = True
          vertices_to_visit = set(self.graph_dict[current_vertex].edges.keys())
          start += [vertex for vertex in vertices_to_visit if vertex not in seen]
          return False
        return None
    
    def random_path(self, start_vertex, end_vertex, path = []):
      start = [start_vertex]
      while len(start) > 0:
            current_vertex = start.pop(0)
            path += [current_vertex]
            if current_vertex == end_vertex:
                return path
            if current_vertex not in seen:
                seen[current_vertex] = True
                vertices_to_visit = set(self.graph_dict[current_vertex].edges.keys())
                start += [vertex for vertex in vertices_to_visit if vertex not in seen]
                return False
            return None
     
      def path_exists(self, start_vertex, end_vertex, path = []):
          start = [start_vertex]
          while len(start) > 0:
            current_vertex = start.pop(0)
            path += [current_vertex]
            if current_vertex == end_vertex:
              return path
            if current_vertex not in seen:
              seen[current_vertex] = True
              vertices_to_visit = set(self.graph_dict[current_vertex].edges.keys())
              start += [vertex for vertex in vertices_to_visit if vertex not in seen]
              return False
            return None
   
      #Display list of movies that are edges of that genre vertex. Suggestions for similar movies will be displayed for neighbor in edges.


def find_movie(graph, first_choice, second_choice):
    #find the shortest path between the two genres
    path = graph.shortest_path(first_choice, second_choice)
    if path is None:
        print("No path found")
    else:
        print("The shortest path between " + first_choice + " and " + second_choice + " is: ")
        print(path)
        print("\n")
        print("Here are some movies in the genre: ")
        for movie in graph.graph_dict[second_choice].edges:
            print(movie)
        print("\n")
        print("Here are some movies in the genre: ")
        for movie in graph.graph_dict[first_choice].edges:
            print(movie)
        print("\n")
        print("Would you like to select a movie from the list above?")
        user_input = input("Enter 'yes' or 'no': ")
        if user_input == 'yes':
            movie_choice = input("Enter the name of the movie: ")
            if movie_choice in graph.graph_dict[second_choice].edges:
                print("You selected: " + movie_choice)
                print("Here are some movies similar to " + movie_choice + ": ")
                for movie in graph.graph_dict[second_choice].edges:
                    print(movie)
            else:
                print("Invalid choice.")
        else:
            print("Would you like to try a different search?")
            user_input = input("Enter 'yes' or 'no': ")
            if user_input == 'yes':
                get_genres()
            else:
                print("Thank you for using Testflix!")
                return

def find_movie_by_name(graph, first_choice, second_choice):
    #find the shortest path between the two genres
    path = graph.shortest_path(first_choice, second_choice)
    if path is None:
        print("No path found")
    else:
        print("The shortest path between " + first_choice + " and " + second_choice + " is: ")
        print(path)
        print("\n")
        print("Here are some movies in the genre: ")
        for movie in graph.graph_dict[second_choice].edges:
            print(movie)
        print("\n")
        print("Here are some movies in the genre: ")
        for movie in graph.graph_dict[first_choice].edges:
            print(movie)
        print("\n")
        print("Would you like to select a movie from the list above?")
        user_input = input("Enter 'yes' or 'no': ")
        if user_input == 'yes':
            movie_choice = input("Enter the name of the movie: ")
            if movie_choice in graph.graph_dict[second_choice].edges:
                print("You selected: " + movie_choice)
                print("Here are some movies similar to " + movie_choice + ": ")
                for movie in graph.graph_dict[second_choice].edges:
                    print(movie)
            else:
                print("Invalid choice.")
        else:
            print("Would you like to try a different search?")
            user_input = input("Enter 'yes' or 'no': ")
            if user_input == 'yes':
                get_genres()
            else:
                print("Thank you for using Testflix!")

def find_movie_by_year(graph, first_choice, second_choice):
    #find the shortest path between the two genres
    path = graph.shortest_path(first_choice, second_choice)
    if path is None:
        print("No path found")
    else:
        print("The shortest path between " + first_choice + " and " + second_choice + " is: ")
        print(path)
        print("\n")
        print("Here are some movies in the genre: ")
        for movie in graph.graph_dict[second_choice].edges:
            print(movie)
        print("\n")
        print("Here are some movies in the genre: ")
        for movie in graph.graph_dict[first_choice].edges:
            print(movie)
        print("\n")
        print("Would you like to select a movie from the list above?")
        user_input = input("Enter 'yes' or 'no': ")
        if user_input == 'yes':
            movie_choice = input("Enter the name of the movie: ")
            if movie_choice in graph.graph_dict[second_choice].edges:
                print("You selected: " + movie_choice)
                print("Here are some movies similar to " + movie_choice + ": ")
                for movie in graph.graph_dict[second_choice].edges:
                    print(movie)
            else:
                print("Invalid choice.")
        else:
            print("Would you like to try a different search?")
            user_input = input("Enter 'yes' or 'no': ")
            if user_input == 'yes':
                get_genres()
            else:
                print("Thank you for using Testflix!")

def find_movie_by_genre(graph, first_choice, second_choice):
    #find the shortest path between the two genres
    path = graph.shortest_path(first_choice, second_choice)
    if path is None:
        print("No path found")
    else:
        print("The shortest path between " + first_choice + " and " + second_choice + " is: ")
        print(path)
        print("\n")
        print("Here are some movies in the genre: ")
        for movie in graph.graph_dict[second_choice].edges:
            print(movie)
        print("\n")
        print("Here are some movies in the genre: ")
        for movie in graph.graph_dict[first_choice].edges:
            print(movie)
        print("\n")
        print("Would you like to select a movie from the list above?")
        user_input = input("Enter 'yes' or 'no': ")
        if user_input == 'yes':
            movie_choice = input("Enter the name of the movie: ")
            if movie_choice in graph.graph_dict[second_choice].edges:
                print("You selected: " + movie_choice)
                print("Here are some movies similar to " + movie_choice + ": ")
                for movie in graph.graph_dict[second_choice].edges:
                    print(movie)
            else:
                print("Invalid choice.")
        else:
            print("Would you like to try a different search?")
            user_input = input("Enter 'yes' or 'no': ")
            if user_input == 'yes':
                get_genres()
            else:
                print("Thank you for using Testflix!")
    
    
    if movie.lower() in graph.graph_dict[first_choice].edges:
        print("You selected: " + movie)
        print("Here are some movies similar to " + movie + ": ")
        for movie in graph.graph_dict[first_choice].edges:
            print(movie)
    else:
        print("Invalid choice.")
        
        print("Would you like to try a different search?")
        user_input = input("Enter 'yes' or 'no': ")
        if user_input == 'yes':
            get_genres()
        else:
            print("Thank you for using Testflix!")
            return
        while True:
            print("Would you like to select a movie from the list above?")
            user_input = input("Enter 'yes' or 'no': ")
            if user_input == 'yes':
                movie_choice = input("Enter the name of the movie: ")
                if movie_choice in graph.graph_dict[first_choice].edges:
                    print("You selected: " + movie_choice)
                    print("Here are some movies similar to " + movie_choice + ": ")
                    for movie in graph.graph_dict[first_choice].edges:
                        print(movie)
                else:
                    print("Invalid choice.")
            else:
                print("Would you like to try a different search?")
                user_input = input("Enter 'yes' or 'no': ")
                if user_input == 'yes':
                    get_genres()
                else:
                    print("Thank you for using Testflix!")
                    return
        
    