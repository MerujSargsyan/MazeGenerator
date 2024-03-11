import java.util.ArrayList;
import java.util.Hashtable;

public class Cell {
    int row;
    int col;
    ArrayList<Cell> neighbors; 
    boolean isStart;
    Hashtable<String, Boolean> walls;


    public Cell(int row, int col) {
        this.row = row;
        this.col = col;
        this.neighbors = new ArrayList<Cell>();
        isStart = false;
        walls = new Hashtable<>();
        walls.put("top", true);
        walls.put("right", true);
        walls.put("bottom", true);
        walls.put("left", true);

    }

    public void addNeighbor(Cell neighbor) {
        this.neighbors.add(neighbor);
    }

    public void makePathToNeighbor(Cell neighbor) {
        if(this.col > neighbor.col) {
            walls.put("right", false);
            neighbor.walls.put("left", false);
            return;
        }
        if(this.col < neighbor.col) {
            walls.put("left", false);
            neighbor.walls.put("right", false);
            return;
        }
        if(this.row > neighbor.row) {
            walls.put("bottom", false);
            neighbor.walls.put("top", false);
            return;
        }
        if(this.row < neighbor.row) {
            walls.put("top", false);
            neighbor.walls.put("bottom", false);
        }
    }

    @Override
    public String toString() {
        String output = "";
        if(walls.get("left")) output += "|";
        if(walls.get("top")) output += "^";

        if(isStart) {
            output += "1";
        } else {
            output += "0";
        }

        if(walls.get("bottom")) output += "v";
        if(walls.get("right")) output += "|";

        return output;
    }
}