
public class ManipRob {

	public static void main(String[] args) {
		Robot Toto = new Robot("Toto",10,20,3);
		Robot Titi = new Robot("Titi");
		
		
		Toto.afficheToi();
		Titi.afficheToi();
		Toto.ChangeOrient(2);
		Titi.ChangeOrient(2);
		Toto.déplacer();
		Titi.déplacer();
		Toto.afficheToi();
		Titi.afficheToi();
		
		System.out.println(Toto);
		
	}

}
