from colorama import init, Fore

from graph import Graph

init(autoreset=True)

def show_menu(graph):
    while True:
        print("\nMenu:")
        print(f"{Fore.BLUE}1. Add city")
        print(f"{Fore.BLUE}2. Add route between cities")
        print(f"{Fore.BLUE}3. Show least costly path between two cities")
        print(f"{Fore.BLUE}4. Show all routes between two cities")
        print(f"{Fore.RED}5. Exit")
        choice = input(f"\n{Fore.YELLOW}Choose an option: ")

        if choice == '1':
            city = input(f"\nEnter the city name: ")
            new_node = graph.add_node(city)
            if new_node:
                print(f'City {city} added.')
        
        elif choice == '2':
            if len(graph.nodes) < 2:
                print("It is necessary to add at least two cities to add a route.")
                continue

            print(f"\n{Fore.BLUE}Available cities:")
            for id, node in graph.nodes.items():
                print(f"{Fore.GREEN}{id}: {node.content}")

            origin_id = int(input(f"\nEnter the origin city number: "))
            destination_id = int(input(f"\nEnter the destination city number: "))
            cost = float(input(f"\nEnter the distance in km: "))
            graph.add_route(origin_id, destination_id, cost)
            print(f'Route from {graph.nodes[origin_id].content} to {graph.nodes[destination_id].content} with distance {cost} km added.')

        elif choice == '3':
            if len(graph.nodes) < 2:
                print("It is necessary to add at least two cities to search for a path.")
                continue

            print(f"\n{Fore.BLUE}Available cities:")
            for id, node in graph.nodes.items():
                print(f"{Fore.GREEN}{id}: {node.content}")

            origin_id = int(input(f"\nEnter the origin city number: "))
            destination_id = int(input(f"\nEnter the destination city number: "))
            graph.show_least_costly_path(origin_id, destination_id)
        
        elif choice == '4':
            if len(graph.nodes) < 2:
                print("It is necessary to add at least two cities to search for routes.")
                continue

            print(f"\n{Fore.BLUE}Available cities:")
            for id, node in graph.nodes.items():
                print(f"{Fore.GREEN}{id}: {node.content}")

            origin_id = int(input(f"\nEnter the origin city number: "))
            destination_id = int(input(f"\nEnter the destination city number: "))
            graph.show_all_routes(origin_id, destination_id)

        elif choice == '5':
            print(f"{Fore.RED}Exiting...")
            break
        
        else:
            print(f"{Fore.RED}Invalid option. Try again.")

def main():
    graph = Graph()
    show_menu(graph)

if __name__ == "__main__":
    main()
