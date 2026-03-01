import java.util.*;

public class SJF_Dynamic {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of processes: ");
        int n = sc.nextInt();

        int[] at = new int[n];
        int[] bt = new int[n];
        int[] ct = new int[n];
        int[] tat = new int[n];
        int[] wt = new int[n];
        boolean[] done = new boolean[n];

        // INPUT
        for(int i=0;i<n;i++){
            System.out.println("\nProcess " + (i+1));
            System.out.print("Arrival Time: ");
            at[i] = sc.nextInt();
            System.out.print("Burst Time: ");
            bt[i] = sc.nextInt();
        }

        int completed = 0, time = 0;

        while(completed < n){

            int idx = -1;
            int minBT = Integer.MAX_VALUE;

            // Find shortest job among arrived processes
            for(int i=0;i<n;i++){
                if(!done[i] && at[i] <= time && bt[i] < minBT){
                    minBT = bt[i];
                    idx = i;
                }
            }

            // If no process arrived yet → CPU idle
            if(idx == -1){
                time++;
            }
            else{
                time += bt[idx];
                ct[idx] = time;
                tat[idx] = ct[idx] - at[idx];
                wt[idx] = tat[idx] - bt[idx];
                done[idx] = true;
                completed++;
            }
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
