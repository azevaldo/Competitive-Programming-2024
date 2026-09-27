import java.util.Scanner;


public class Main {
    public static void main(String[] args) {
           Scanner tec=new Scanner(System.in);
        String st=tec.next();
        String st2=tec.next();
        int t=st.compareToIgnoreCase(st2);
      
        if(t==0)
            System.out.println(t);
        else if(t>0)
            System.out.println(1);
        else if(t<0)
            System.out.println(-1);
    
}
    
}