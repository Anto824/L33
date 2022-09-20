
public class Robot {
	private String reference;
	private String name;
	private int x;
	private int y;
	private int orient;
	private int nbRobot = 0;
	private String pp;
	private String oo;
	
	public Robot(String name,int x,int y,int orient) {
		nbRobot++;
		this.name = name;
		this.x = x;
		this.y = y;
		this.orient = orient;
		this.reference = "ROB" + nbRobot;
		System.out.println(nbRobot);
	}
	public Robot(String name) {
		nbRobot++;
		this.x = 0;
		this.y = 0;
		this.orient = 1;
		this.name = name;
		this.reference = "ROB" + nbRobot;
		System.out.println(nbRobot);
	}
	public void ChangeOrient(int orient) {
		this.orient = orient;
	}
	
	public void déplacer() {
		if (orient == 1) {
			y++;
		}
		else {
			if (orient == 2) {
				x++;
			}
			else {
				if (orient == 3) {
					if (y!=0) {
						y--;
					}
				}
				else {
					if (x!=0) {
						x--;
					}
				}
			}
		}
	}
	
	public int getx() {
		return x;
	}
	public int gety() {
		return y;
	}
	public int getorient() {
		return orient;
	}
	public String getName() {
		return name;
	}
	public void afficheToi() {
		System.out.println(name);
		System.out.println("x = " + x);
		System.out.println("y = "+y);
		System.out.println("orienté vers " +orient);
		System.out.println("");
	}
	public String chaineOrientation() {
		if(orient == 1) {
			oo="NORD";
		}
		else {
			if(orient == 2) {
				oo = "EST";
			}
			else {
				if(orient == 3) {
					oo = "SUD";
				}
				else {
					oo = "OUEST";
				}
			}
		}
		return oo;
	}
	public String toString() {
		pp = "nom: " + name + "\n référence: " + reference + "\n abscisse: " + x + ", ordonnée: " + y + "\n direction: " + chaineOrientation() + "\n";
		return pp;
	}
	
	
}
