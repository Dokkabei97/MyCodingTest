package Chapter4;

import java.util.Scanner;

public class ex4_1 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        // N울 입력받기
        int n = sc.nextInt();
        sc.nextLine(); // 버퍼 비우기
        String[] plans = sc.nextLine().split(" ");
        int x = 1, y = 1;

        // L, R, U, D 에 따른 이동 방향
        int[] dx = {0, 0, -1, 1};
        int[] dy = {-1, 1, 0, 0};
        char[] moveType = {'L', 'R', 'U', 'D'};

        // 이동 계획을 하나씩 확인
        for (int i = 0; i < plans.length; i ++) {
            char plan = plans[i].charAt(0);
            // 이동 후 좌표 구하기
            int nx = -1, ny = -1;
            for(int j = 0; j < 4; j ++) {
                if (plan == moveType[j]) {
                    nx = x + dx[j];
                    ny = y + dy[j];
                }
            }
            // 공간을 벗어나는 경우 무시
            if (nx < 1 || ny < 1 || nx > n || ny > n)
                continue;
            // 이동 수행
            x = nx;
            y = ny;
        }
        System.out.println(x + " " + y);
    }
}
