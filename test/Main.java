public class Main {
    public static void main(String[] args) {
        System.out.println(args.length);
        if(args.length != 1) {
            System.out.println("Please enter only size of maze");
            System.exit(1);
        }
        try {
            Maze maze = new Maze(Integer.parseInt(args[0]));
            maze.printMaze();
        } catch(NumberFormatException ex) {
            System.out.println("Please enter a number for size");
            System.exit(2);
        }
    }
}