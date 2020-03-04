package Islands;

import java.util.*;

/*
* Problem description can be found at the following link:
*   https://open.kattis.com/problems/islands3
*/

public class Islands {

    public static void printNodes(int columns, IslandNode[][] nodes) {
        int i = 0;
        for (IslandNode[] row: nodes) {
            for (IslandNode node: row) {
                if (i % columns == 0 && i != 0) {
                    System.out.println();
                }
                System.out.print(node);
                i++;
            }
        }
        System.out.println();
    }

    public static void printNeighbours(IslandNode[][] nodes) {
        for(IslandNode[] row: nodes) {
            for(IslandNode node: row) {
                System.out.print(node + ": ");
                for(IslandNode neighbour: node.getNeighbours()) {
                    System.out.print(neighbour + "; ");
                }
                System.out.println();
            }
        }
    }

    public static int findMinimumIslands(ArrayList<IslandNode> landNodes) {
        ArrayList<IslandNode> checkedLandNodes = new ArrayList<>();
        for(IslandNode node: landNodes) {
            if(!checkedLandNodes.contains(node)) {
                ArrayList<IslandNode> neighbours = new ArrayList<>(node.getNeighbours());
                for(int i = 0; i < neighbours.size(); i++) {
                    IslandNode neighbour = neighbours.get(i);
                    if(neighbour.getNodeType() != NodeType.WATER) {
                        node.combineNeighbours(neighbour);
                    }
                    if(neighbour.getNodeType() == NodeType.LAND) {
                        checkedLandNodes.add(neighbour);
                    }
                    neighbours = new ArrayList<>(node.getNeighbours());
                }
            }
        }
        return landNodes.size() - checkedLandNodes.size();
    }

    public static ArrayList<IslandNode> findLandNodes(Scanner scanner) {
        int rows = scanner.nextInt();
        int columns = scanner.nextInt();
        scanner.nextLine();
        IslandNode[][] allNodes = new IslandNode[rows][columns];
        ArrayList<IslandNode> landNodes = new ArrayList<>();
        int y = 0;
        while(scanner.hasNextLine()) {
            char[] line = scanner.nextLine().toCharArray();
            for(int x = 0; x < line.length; x++) {
                IslandNode islandNode = new IslandNode(x, y, line[x]);
                islandNode.findNeighbours(allNodes);
                allNodes[y][x] = islandNode;
                if(islandNode.getNodeType() == NodeType.LAND) {
                    landNodes.add(islandNode);
                }
            }
            y++;
        }
        return landNodes;
    }

    public static void main(String[] args) {
        ArrayList<IslandNode> landNodes = findLandNodes(new Scanner(System.in));
        int numberOfIslands = findMinimumIslands(landNodes);
        System.out.println(numberOfIslands);
    }
}
