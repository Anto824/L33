package vecteur3d;

public class vecteur3d {
	private float x;
	private float y;
	private float z;
	private double norme;
	private double ps;
	private float a;
	private float b;
	private float c;
	
	
	
	
	public vecteur3d(float x, float y, float z) {
		this.x = x;
		this.y = y;
		this.z = z;
	}
	public vecteur3d() {
		this.x = 0;
		this.y = 0;
		this.z = 0;
	}
	public void affiche() {
		System.out.println("<" + x + "," + y + "," + z + ">");
	}
	
	public double getNorme() {
		norme = x*x + y*y + z*z;
		norme = Math.sqrt(norme);
		return norme;
	}
	
	public double produitScal(vecteur3d v) {
		ps = x*v.x+y*v.y+z*v.z;
		return ps;
	}
	public vecteur3d somme(vecteur3d v) {
		a = x+v.x;
		b = y+v.y;
		c = z+v.z;
		vecteur3d s = new vecteur3d(a,b,c);
		return s;
	}
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
}
