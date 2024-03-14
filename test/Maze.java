import java.util.Random;
import java.util.ArrayList;
import java.util.Stack;

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

        Cell current = mazeArray.get(startingPoint[0]).get(startingPoint[1]);
        Stack<Cell> stack = new Stack<>();
        int visited = 0;

        stack.push(current);
        while(!stack.isEmpty()) {
            current.isVisited = true;
            visited++;
            Cell neighbor = getViableNeighbor(current);
            if(neighbor == null) {
                if(visited == mazeSize*mazeSize) {
                    current.isStart = true;
                }
                current = stack.pop();
            } else {
                current.makePathToNeighbor(neighbor);
                stack.push(current);
                current = neighbor;
            }
            
        }
    }

    private Cell getViableNeighbor(Cell current) {
        ArrayList<Cell> validNeighbors = new ArrayList<Cell>();
        for(Cell neighbor : current.neighbors) {
            if(!neighbor.isVisited) {
                validNeighbors.add(neighbor);
            }
        }

        if(!validNeighbors.isEmpty()) {
            int neighborIdx = random.nextInt(validNeighbors.size());
            return validNeighbors.get(neighborIdx);
        }
        return null;
    }

    // connects rows as neighbors
    private void connectBottomRows() {
        for(int i = 0; i < mazeArray.size(); i++) {

            if(i + 1 < mazeArray.size()) {

                for(int j = 0; j < mazeSize; j++) {
                    Cell currentCell = mazeArray.get(i).get(j);
                    Cell neighbor = mazeArray.get(i+1).get(j);
                    currentCell.addNeighbor(neighbor);
                    neighbor.addNeighbor(currentCell);
                }

            }
        }
    }

    public void printMaze() {
        String output = "\n";
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