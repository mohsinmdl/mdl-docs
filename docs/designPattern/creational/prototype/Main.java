public class Main {
    
    public static void main(String[] args) throws CloneNotSupportedException {   
    	
        Car honda = new Car();
        honda.setOwner("Mohsin Mahmood");
        
        
        Car hondacopy = (Car) honda.clone();
        
       
        
        System.out.println("Name of first owner " + honda.getOwner().getName());
        System.out.println("Name of first owner " + hondacopy.getOwner().getName());        
        
    }
                
}

