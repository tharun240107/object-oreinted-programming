import java.util.*;

public class RoundRobin {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of processes: ");
        int n = sc.nextInt();

        int[] at = new int[n];
        int[] bt = new int[n];
        int[] remaining = new int[n];
        int[] ct = new int[n];
        int[] tat = new int[n];
        int[] wt = new int[n];

        // INPUT
        for(int i=0;i<n;i++){
            System.out.println("\nProcess " + (i+1));
            System.out.print("Arrival Time: ");
            at[i] = sc.nextInt();
            System.out.print("Burst Time: ");
            bt[i] = sc.nextInt();
            remaining[i] = bt[i];
        }

        System.out.print("\nEnter Time Quantum: ");
        int tq = sc.nextInt();

        int time = 0, completed = 0;

        while(completed < n){

            boolean executed = false;

            for(int i=0;i<n;i++){

                if(at[i] <= time && remaining[i] > 0){

                    executed = true;

                    if(remaining[i] > tq){
                        time += tq;
                        remaining[i] -= tq;
                    }
                    else{
                        time += remaining[i];
                        remaining[i] = 0;
                        ct[i] = time;
                        completed++;
                    }
                }
            }

            // CPU idle case
            if(!executed){
                time++;
            }
        }

        // Calculate TAT and WT
        for(int i=0;i<n;i++){
            tat[i] = ct[i] - at[i];
            wt[i] = tat[i] - bt[i];
        }

        // OUTPUT
        System.out.println("\nProcess\tAT\tBT\tCT\tTAT\tWT");

        for(int i=0;i<n;i++){
            System.out.println("P"+(i+1)+"\t"+at[i]+"\t"+bt[i]+"\t"+
                    ct[i]+"\t"+tat[i]+"\t"+wt[i]);
        }

        sc.close();
    }
}


