from colorama import init, Fore

from node import Node

class Graph:
    def __init__(self):
        self.nodes = {}
        self.next_id = 1

    def add_node(self, name):
        if any(name == node.content for node in self.nodes.values()):
            print(f"{Fore.RED}Error: The city '{name}' already exists in the graph.")
            return None
        
        node = Node(name)
        self.nodes[self.next_id] = node
        self.next_id += 1
        return node

    def add_route(self, origin_id, destination_id, cost):
        if origin_id in self.nodes and destination_id in self.nodes:
            origin = self.nodes[origin_id].content
            destination = self.nodes[destination_id].content
            self.nodes[origin_id].add_neighbor(self.nodes[destination_id], cost)
        else:
            print("One of the cities was not found in the graph.")

    def _find_path_recursive(self, current_node, destination, distances, previous_path, current_cost):
        if current_node == destination:
            return

        for neighbor, cost in current_node.neighbors.items():
            total_cost = current_cost + cost
            if total_cost < distances[neighbor]:
                distances[neighbor] = total_cost
                previous_path[neighbor] = current_node
                self._find_path_recursive(neighbor, destination, distances, previous_path, total_cost)

    def _find_least_costly_path(self, origin_id, destination_id):
        origin = self.nodes[origin_id]
        destination = self.nodes[destination_id]
        
        distances = {node: float('inf') for node in self.nodes.values()}
        distances[origin] = 0

        previous_path = {origin: None}

        self._find_path_recursive(origin, destination, distances, previous_path, 0)

        path = []
        current_node = destination

        while current_node is not None:
            path.insert(0, current_node)
            current_node = previous_path[current_node]
        
        return path, distances[destination]

    def show_least_costly_path(self, origin_id, destination_id):
        path, total_cost = self._find_least_costly_path(origin_id, destination_id)

        if total_cost != float('inf'):
            print(f'Least costly path from {self.nodes[origin_id].content} to {self.nodes[destination_id].content}:')
            for i, node in enumerate(path):
                if i < len(path) - 1:
                    print(f'{node.content} -> ', end='')
                else:
                    print(f'{node.content}')
            print(f'Total cost: {total_cost} km')
        else:
            print(f'There is no path from {self.nodes[origin_id].content} to {self.nodes[destination_id].content}')

    def show_path(self, origin_id, destination_id):
        origin = self.nodes[origin_id]
        destination = self.nodes[destination_id]
        
        current_path = [origin]
        self._traverse(origin.neighbors, origin, destination, origin.content, current_path)

    def _traverse(self, neighbors, origin, destination, path, current_path):
        for neighbor, _ in neighbors.items():
            if destination.content in path:
                break

            if neighbor == destination:
                updated_path = path + " -> " + destination.content
                print(updated_path)
                break

            if neighbor not in current_path:
                current_path.append(neighbor)
                self._traverse(
                    neighbor.neighbors, origin, destination, path + " -> " + neighbor.content, current_path
                )
                current_path.remove(neighbor)

    def show_all_routes(self, origin_id, destination_id):
        if origin_id in self.nodes and destination_id in self.nodes:
            origin = self.nodes[origin_id]
            destination = self.nodes[destination_id]
            
            all_routes = []
            self._search_all_routes(origin, destination, [], 0, all_routes)
            if all_routes:
                print(f'All routes from {origin.content} to {destination.content} and their costs:')
                for route, cost in all_routes:
                    print(f'Route: {" -> ".join(node.content for node in route)}, Cost: {cost} km')
            else:
                print(f'There are no routes from {origin.content} to {destination.content}')
        else:
            print("One of the cities was not found in the graph.")

    def _search_all_routes(self, current_node, destination, current_path, current_cost, all_routes):
        current_path.append(current_node)
        if current_node == destination:
            all_routes.append((list(current_path), current_cost))
        else:
            for neighbor, cost in current_node.neighbors.items():
                if neighbor not in current_path:
                    self._search_all_routes(neighbor, destination, current_path, current_cost + cost, all_routes)
        current_path.pop()
