class Node:
    def __init__(self, name):
        self.name = name
        self.number = -1
        self.adjacent_nodes = dict()
        self.in_queue = False

    def connect_with(self, other):
        if not other.name in self.adjacent_nodes.keys():
            self.adjacent_nodes[other.name] = other

    def erdos_number(self):
        if self.number >= 0:
            return self.number
        else:
            return 'infinity'
    
def compute_erdos_numbers(node):

    # First node (Erdos)
    active_nodes = [node]
    node.in_queue = True

    while len (active_nodes) > 0:

        # Get current node to expand
        current_node = active_nodes.pop()

        for node in current_node.adjacent_nodes.values():
            
            # If not visited, add to queue
            if not node.in_queue:
                node.in_queue = True
                active_nodes.append(node)

            # If erdo number has not been calculated, update
            if node.number == -1:
                node.number = current_node.number + 1

            # Check for shorter path in graph
            elif node.number > current_node.number + 1:
                node.number = current_node.number + 1
                active_nodes.append(node)


    return

if __name__ == '__main__':
    scenarios = int(input().strip())
    for i in range(scenarios):
        papers, authors = [int(x) for x in input().strip().split()]
        d = dict()
        # load all papers from papers database
        for j in range(papers):
            line = input().strip().split(sep = ':')[0]
            parts = line.split(sep = ',')
            # prepare the list of authors of the current paper
            current_paper_author_list = list()
            for k in range(0, len(parts), 2):
                if k + 1 < len(parts):
                    author_name = parts[k].strip() + ', ' + parts[k+1].strip()
                else:
                    author_name = parts[k].strip()
                current_paper_author_list.append(author_name)

            # add to the nodes of the graph those authors that did not exist yet
            current_paper_node_list = list()
            for author_name in current_paper_author_list:
                if not author_name in d.keys():
                    d[author_name] = Node(author_name)
                    #print('*****', author_name)
                current_paper_node_list.append(d[author_name])

            # connect the co-authors (i.e., the nodes) 
            for k in range(len(current_paper_node_list)):
                for l in range(k + 1, len(current_paper_node_list)):
                    current_paper_node_list[k].connect_with(current_paper_node_list[l])
                    current_paper_node_list[l].connect_with(current_paper_node_list[k])
                    
            
        # compute the Erdos numbers for all the nodes
        d["Erdos, P."].number = 0
        compute_erdos_numbers(d["Erdos, P."])

        # print Erdos number of required authors
        print("Scenario %d" % (i+1))
        for j in range(authors):
            
            name = input().strip()
            print(name, d[name].erdos_number() if name in d.keys() else 'infinity')

        
