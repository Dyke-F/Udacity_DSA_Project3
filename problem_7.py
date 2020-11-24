# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler = None):
        # Initialize the node with children as before, plus a handler
        self.handler = handler
        self.children = {}

    def insert(self, webpath):
        # Insert the node as before
        if webpath not in self.children:
            self.children[webpath] = RouteTrieNode()
            
    def set_handler(self, handler):
        self.handler = handler
        
        

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)
        
        
    def insert(self, subpath, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        curr_node = self.root
        for sp in subpath:
            if sp not in curr_node.children:
                curr_node.children[sp] = RouteTrieNode()
            curr_node = curr_node.children[sp]
        curr_node.handler = handler
                
    def find(self, subpath):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        curr_node = self.root
        for sp in subpath:
            if sp == -1:
                break
            if sp in curr_node.children:
                curr_node = curr_node.children[sp]
            else:
                return None
        return curr_node.handler
                

        
# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, handler, error_404_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route_trie = RouteTrie(handler)
        self.error_404_handler = error_404_handler

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        subpath = self.split_path(path)
        self.route_trie.insert(subpath, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        subpath = self.split_path(path)
        handler = self.route_trie.find(subpath)
        return handler if handler != None else self.error_404_handler
    
    @classmethod
    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and lookup functions:        
        path = path.strip("/")
        path = path.lower()
        return path.split("/") if path else [-1]
        
# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "Error 404: page not found") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one    