package vecteur3d;

public class testVecteur {

	public static void main(String[] args) {
		vecteur3d v1 = new vecteur3d(3,2,5);
		vecteur3d v2 = new vecteur3d(1,2,3);
		v1.affiche();
		System.out.println(v1.getNorme());
		v2.affiche();
		System.out.println(v2.getNorme());
		System.out.print("v1 + v2 = ");
		v1.somme(v2).affiche();
		System.out.print("v1.v2 = ");
		System.out.println(v1.produitScal(v2));

	}

}
