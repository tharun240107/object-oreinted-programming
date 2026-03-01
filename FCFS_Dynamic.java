import java.util.*;
public class FCFS_Dynamic {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of processes: ");
        int n = sc.nextInt();

        int[] arrival = new int[n];
        int[] burst = new int[n];
        int[] start = new int[n];
        int[] complete = new int[n];
        int[] tat = new int[n];
        int[] wt = new int[n];

        // INPUT
        for(int i=0;i<n;i++){
            System.out.println("\nProcess " + (i+1));
            System.out.print("Arrival Time: ");
            arrival[i] = sc.nextInt();
            System.out.print("Burst Time: ");
            burst[i] = sc.nextInt();
        }

        // Sort by arrival time (VERY IMPORTANT for FCFS)
        for(int i=0;i<n-1;i++){
            for(int j=i+1;j<n;j++){
                if(arrival[i] > arrival[j]){

                    int temp;

                    temp = arrival[i]; arrival[i]=arrival[j]; arrival[j]=temp;
                    temp = burst[i]; burst[i]=burst[j]; burst[j]=temp;
                }
            }
        }

        // FCFS CALCULATION
        int time = 0;

        for(int i=0;i<n;i++){

            if(time < arrival[i])
                time = arrival[i];

            start[i] = time;
            complete[i] = start[i] + burst[i];

            tat[i] = complete[i] - arrival[i];
            wt[i] = tat[i] - burst[i];

            time = complete[i];
        }

        // OUTPUT
        System.out.println("\nProcess\tAT\tBT\tST\tCT\tTAT\tWT");

        for(int i=0;i<n;i++){
            System.out.println("P"+(i+1)+"\t"+arrival[i]+"\t"+burst[i]+"\t"+
                    start[i]+"\t"+complete[i]+"\t"+tat[i]+"\t"+wt[i]);
        }

        sc.close();
    }
}