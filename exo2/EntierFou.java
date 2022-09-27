package exo2;
import java.util.*;

public class EntierFou extends Entier{
	private int niveaudefolie;
	private static Random r = new Random();
	
	public EntierFou(int niveauDeFolie,int valeur,int bornemin,int bornemax) {
		super(valeur,bornemin,bornemax);
		this.niveaudefolie = niveauDeFolie;
	}
	
	public void incremente() {
		setValeur(valeur+r.nextInt(niveaudefolie));
	}
	
	
	
	
	
}
