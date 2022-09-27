package exo2;

public class Entier {
	protected int valeur;
	private int bornemin;
	private int bornemax;
	
	public Entier(int valeur,int bornemin,int bornemax) {
		this.valeur = valeur;
		this.bornemin = bornemin;
		this.bornemax = bornemax;
	}
	
	public Entier(int bornemin,int bornemax) {
		this.valeur = 0;
		this.bornemin = bornemin;
		this.bornemax = bornemax;
	}
	public void setValeur(int valeur) {
		if(valeur>bornemin && valeur<bornemax) {
			this.valeur = valeur;
		}
		else {
			System.out.println("erreur");
		}
	}
	public void incremente() {
		setValeur(getvaleur()+1);
	}
	public void incremente(int n) {
		setValeur(valeur+n);
	}
	public String toString() {
		return "la valeur est " + getvaleur();
	}
	public int getvaleur() {
		return valeur;
	}
	public boolean equals(Entier n) {
		if(getvaleur() == n.getvaleur()) {
			return true;
		}
		else {
			return false;
		}
	}
	
	
	
	
}
