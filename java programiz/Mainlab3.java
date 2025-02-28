class FibanocciSeries{
public static void main(String[]args){
int n=100;
int first=0,second=1;
System.out.println("Fibanocci Series  up to "+n+" terms:");
System.out.println("T.v.Tharun");
for(int i=1;i<=n;i++){
System.out.print(first+"");
int next=first + second;
first= second;
second= next;
}
}
}
