if __name__ == '__main__':
    location_list = [ # [x,y,name]
  [75, 125, 'Arad'],
  [100, 75, 'Zerind'],
  [125, 25, 'Oradea'],
  [265, 175, 'Sibiu'],
  [425, 175, 'Fagaras'],
  [320, 230, 'Rimnicu Vilcea'],
  [475, 310, 'Pitesti'],
  [350, 465, 'Craiova'],
  [185, 450, 'Drobeta'],
  [190, 390, 'Mehadia'],
  [185, 335, 'Lugoj'],
  [85, 280, 'Timisoara'],
  [640, 390, 'Bucharest'],
  [575, 485, 'Giurgiu'],
  [745, 340, 'Urziceni'],
  [875, 340, 'Hirsova'],
  [935, 440, 'Eforie'],
  [850, 225, 'Vaslui'],
  [760, 120, 'Iasi'],
  [625, 60, 'Neamt']
]

    step_cost = [
  ['Arad', 'Zerind', 75],
  ['Zerind', 'Oradea', 71],
  ['Oradea', 'Sibiu', 151],
  ['Sibiu', 'Arad', 140],
  ['Sibiu', 'Fagaras', 99],
  ['Sibiu', 'Rimnicu Vilcea', 80],
  ['Fagaras', 'Bucharest', 211],
  ['Bucharest', 'Giurgiu', 90],
  ['Bucharest', 'Pitesti', 101],
  ['Pitesti', 'Rimnicu Vilcea', 97],
  ['Rimnicu Vilcea', 'Craiova', 146],
  ['Craiova', 'Pitesti', 138],
  ['Craiova', 'Drobeta', 120],
  ['Drobeta', 'Mehadia', 75],
  ['Mehadia', 'Lugoj', 70],
  ['Lugoj', 'Timisoara', 111],
  ['Arad', 'Timisoara', 118],
  ['Bucharest', 'Urziceni', 85],
  ['Urziceni', 'Vaslui', 142],
  ['Vaslui', 'Iasi', 92],
  ['Iasi', 'Neamt', 87],
  ['Urziceni', 'Hirsova', 98],
  ['Hirsova', 'Eforie', 86]
]

