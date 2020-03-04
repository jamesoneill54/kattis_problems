package Islands;

import java.util.LinkedHashSet;

public class IslandNode {

    int x;
    int y;
    NodeType nodeType;
    LinkedHashSet<IslandNode> neighbours;

    public IslandNode(int x, int y, char type) {
        this.x = x;
        this.y = y;
        this.nodeType = determineNodeType(type);
        this.neighbours = new LinkedHashSet<>();
    }

    public void combineNeighbours(IslandNode neighbour) {
        for(IslandNode newNeighbour: neighbour.getNeighbours()) {
            if(newNeighbour != this) {
                neighbours.add(newNeighbour);
            }
        }
    }

    public void findNeighbours(IslandNode[][] allNodes) {
        if(this.getY() > 0) {
            this.addNeighbour(allNodes[this.getY() - 1][this.getX()]);
        }
        if(this.getX() > 0) {
            this.addNeighbour(allNodes[this.getY()][this.getX() - 1]);
        }
    }

    private void addNeighbour(IslandNode neighbour) {
        neighbours.add(neighbour);
        if(!neighbour.hasNeighbour(this)) {
            neighbour.addNeighbour(this);
        }
    }

    private boolean hasNeighbour(IslandNode node) {
        return neighbours.contains(node);
    }

    public LinkedHashSet<IslandNode> getNeighbours() {
        return neighbours;
    }

    private static NodeType determineNodeType(char type) {
        if(type == 'C') {
            return NodeType.CLOUD;
        }
        else if(type == 'W') {
            return NodeType.WATER;
        }
        else {
            return NodeType.LAND;
        }
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    public NodeType getNodeType() {
        return nodeType;
    }

    @Override
    public String toString() {
        return "(" + x + ", " + y + ", " + nodeType + ")";
    }
}
