#################################################################################
#     File Name           :     InstanceGenerator.py
#     Created By          :     Youcef Magnouche
#     Creation Date       :     [2020-07-07 11:00]
#     Description         :     Generate instances for Load Balancing problem
#     Company             :     Huawei Technologies France (FRC)
#################################################################################

import os
import sys
import math  
import networkx as nx
import numpy as np  


def createGraph(type, nbTunnels, nbunnelEndNodes, nbNeighbours, path):

    # Graph definition
    graph = nx.MultiGraph()

    # Create the graph
    if type == "Type0":
        # Add source nodes
        for pos in range(nbunnelEndNodes):
            graph.add_node(pos, name = str(pos))

        # Add nodes adjacent to source nodes
        pos = nbunnelEndNodes
        for tunnelNode in range(nbunnelEndNodes):
            for neighbour in range(nbNeighbours):
                graph.add_node(pos, name = str(pos))
                pos += 1

        # Link source nodes with their adjacent nodes
        for tunnelNode in range(nbunnelEndNodes):
            for neighbour in range(nbNeighbours):
                graph.add_edge(tunnelNode, nbunnelEndNodes + nbNeighbours * tunnelNode + neighbour)

        # Link the neighbours of the source nodes
        for tunnelNode in range(1, nbunnelEndNodes):
            for neighbour in range(nbNeighbours):
                graph.add_edge(nbunnelEndNodes + neighbour, nbunnelEndNodes + nbNeighbours * tunnelNode + neighbour)


    if type == "Type1":
        # Add source nodes
        for pos in range(nbunnelEndNodes):
            graph.add_node(pos, name = str(pos))

        # Add nodes of the clique
        pos = nbunnelEndNodes
        for tunnelNode in range(nbunnelEndNodes):
            for neighbour in range(nbNeighbours):
                graph.add_node(pos, name = str(pos))
                pos += 1

        # Link source nodes with their adjacent nodes
        for tunnelNode in range(nbunnelEndNodes):
            for neighbour in range(nbNeighbours):
                graph.add_edge(tunnelNode, nbunnelEndNodes + nbNeighbours * tunnelNode + neighbour)

        # Link the neighbours of the source nodes
        for neighbour1 in range(nbNeighbours * nbunnelEndNodes):
            for neighbour2 in range(neighbour1 + 1, nbNeighbours * nbunnelEndNodes):
                graph.add_edge(nbunnelEndNodes + neighbour1, nbunnelEndNodes + neighbour2)

    print("Number of nodes ", len(graph.nodes))
    print("Number of Links ", len(graph.edges))

    # Export files
    topo_generator(graph, path)
    tunnels_generator(graph, nbTunnels, nbunnelEndNodes, nbNeighbours, path) 
 

def topo_generator(G, path, minCap = 1000, maxCap = 2000):  

    # Initialize the topology file
    filename = path + "/topo.csv"
    file = open(filename,"w+")

    # Write the header of the file
    file.write("LinkID,src,dst,cap")

    # Write the edges 
    pos = 0
    for edge in G.edges: 
        file.write("\n" + str(pos) + "," + str(G.nodes[edge[0]]['name']) + "," +  str(G.nodes[edge[1]]['name']) + "," + str(np.random.randint(minCap, maxCap)))
        pos += 1

    # Close file
    file.close() 

def tunnels_generator(G, nbTunnels, nbunnelEndNodes, nbNeighbours, path, min_bw = 100, max_bw = 200):

    # Generate files with head
    filename_tunnel = path + "/Tunnel.csv"
    file = open(filename_tunnel,"w+") 

    # Write the header of the file
    file.write("tunnelID,src,dst,bandwidth") 

    # Write Data in files
    for tunnel in range(nbTunnels): 

        # Select one source and one destination 
        src = np.random.randint(0, nbunnelEndNodes)
        dst = np.random.randint(0, nbunnelEndNodes)
        while src == dst:
            dst = np.random.randint(0, nbunnelEndNodes)
   
        #Generation of diurnal traffic for a tunnel
        alpha = np.random.random_sample()*(max_bw - min_bw)
        w = 2 * math.pi / 24 # period
        mu = 0
        sigma = 0.1
        phy = np.random.normal(mu, sigma,1)[0] # phase shift
        noise = np.random.normal(0, 0.1, 1)[0]
        value = alpha * (1 + math.sin(w + phy) + noise) + min_bw
        file.write("\n{0},{1},{2},{3}".format(tunnel, src, dst, value) )
        file.write("\n{0},{1},{2},{3}".format(tunnel, dst, src, value) )

    # Close file
    file.close()   

def main():
 
    type = sys.argv[1] # 'Type0', 'Type1'
    nbunnelEndNodes = int(sys.argv[2])
    nbTunnels = int(sys.argv[3])
    nbNeighbours = int(sys.argv[4])
    path = sys.argv[5] 

    createGraph(type, nbTunnels, nbunnelEndNodes, nbNeighbours, path)

 
if __name__== "__main__":
    main()