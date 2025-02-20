from prettytable import PrettyTable

table = PrettyTable()
# print(table)
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# print(table)
table.add_column("Type", ["Electric", "Water", "Fire"])
# print(table)
table.align = "l"
print(table)