import java.util.Random;
import java.util.ArrayList;

public class Maze {
    ArrayList<ArrayList<Cell>> mazeArray;
    int mazeSize;
    Random random;

    public Maze(int mazeSize) {
        this.mazeSize = mazeSize;
        this.mazeArray = new ArrayList<ArrayList<Cell>>();
        random = new Random();

        int[] startingPoint = createStartingPoint();
        generateMaze(startingPoint);
    }

    // coordinates are int arrays of the form: [row, col]
    private int[] createStartingPoint() {
        int startWall = random.nextInt(4); // 4 walls
        int[] output = new int[]{0, 0};
        switch(startWall) {
            case 0: // left wall
                output[0] = random.nextInt(mazeSize);
                output[1] = 0;
                break;
            case 1: // top wall
                output[0] = 0;
                output[1] = random.nextInt(mazeSize);
                break;
            case 2: // right wall
                output[0] = random.nextInt(mazeSize);
                output[1] = mazeSize-1;
                break;
            case 3: // bottom wall
                output[0] = mazeSize-1;
                output[1] = random.nextInt(mazeSize);
                break; 
        }

        return output;
    }

    /** 
     * @param startingPoint given in form: [row, col] 
     */
    private void generateMaze(int[] startingPoint) { 
        for(int i = 0; i < mazeSize; i++) {
            ArrayList<Cell> rowValues = new ArrayList<>();

            for(int j = 0; j < mazeSize; j++) {
                Cell cell = new Cell(i, j);
                if(i == startingPoint[0] && j == startingPoint[1]) {
                    cell.isStart = true;
                }

                if(!rowValues.isEmpty()) {
                    Cell previousCell = rowValues.get(rowValues.size() - 1);
                    cell.addNeighbor(previousCell);
                    previousCell.addNeighbor(cell);
                }
                rowValues.add(cell);
            }

            mazeArray.add(rowValues);
        }

        connectBottomRows();

        ArrayList<Cell> visited = new ArrayList<>();
        Cell current = mazeArray.get(startingPoint[0]).get(startingPoint[1]);
        while(visited.size() != mazeSize*mazeSize) {
            visited.add(current);
            int neighborIdx = random.nextInt(current.neighbors.size());
            Cell neighbor = current.neighbors.get(neighborIdx);
            current.makePathToNeighbor(neighbor);
            current = neighbor;
        }
    }

    // connects rows as neighbors
    private void connectBottomRows() {
        for(int i = 0; i < mazeArray.size(); i++) {

            if(i + 1 != mazeArray.size()) {

                for(int j = 0; j < mazeSize; j++) {
                    Cell currentCell = mazeArray.get(i).get(j);
                    currentCell.addNeighbor(mazeArray.get(i+1).get(j));
                }

            }
        }
    }

    public void printMaze() {
        String output = "";
        for(int i = 0; i < mazeArray.size(); i++) {
            output += "[";
            for(int j = 0; j < mazeSize; j++) {
                Cell cell = mazeArray.get(i).get(j);
                output += cell.toString() + ", ";
            }
            output += "]\n";
        }
        System.out.println(output);
    }
}