class MedicineStock { String name; int quantity; MedicineStock(String n,int q){name=n;quantity=q;} void display(){System.out.println(name+": "+quantity);} }
class Inventory { MedicineStock[] stock={new MedicineStock("Tablets",20),new MedicineStock("Syrup",10)}; void display(){for(MedicineStock item:stock)item.display();} }
// The Inventory class owns both the array and the loop.
public class Q04_PharmacyInventory { public static void main(String[] a){new Inventory().display();} }
