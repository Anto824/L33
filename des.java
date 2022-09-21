package exo1;

import java.util.Random;

public class des {
	private int nbFaces;
	private String nom;
	private static Random r = new Random();
	private final int min = 3;
	private final int max = 120;
	private int compteur=0;
	private int valmin;
	private boolean mem;
	private int memoire;
	
	
	public des(final String nom) {
		compteur++;
		setNbFaces(6);
		this.nom = nom;
		memoire = 0;
	}
	
	public des(final String nom, int nbFaces) {
		compteur++;
		setNbFaces(nbFaces);
		this.nom = nom;
	}
	public des() {
		compteur++;
		setNbFaces(6);
		this.nom = "De" + compteur; 
		valmin = 0;
	}
	public des(boolean mem) {
		compteur++;
		setNbFaces(6);
		this.nom = "De" + compteur; 
		valmin = 0;
		this.mem = mem;
	}
	
	
	
	public int getNbFaces() {
		return nbFaces;
	}
	
	private void setNbFaces(int nbFaces) {
		if (nbFaces<min || nbFaces>max) {
			System.out.println("erreur.");
		}
		else {
			this.nbFaces = nbFaces;
		}
	}
	
	public int lancer() {
		int nbAleatoire= r.nextInt(nbFaces)+1;

		while (nbAleatoire<valmin && nbAleatoire!=memoire) {
			nbAleatoire= r.nextInt(nbFaces)+1;
		}
		if (mem == true){
			memoire = nbAleatoire;
		}
		return nbAleatoire;
	}
	
	public boolean equals(des d) {
		if (getNbFaces() == d.getNbFaces()) {
			return true;
		}
		else {
			return false;
		}
	}
	
}









