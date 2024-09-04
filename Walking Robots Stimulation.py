class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        
        way = [[0,1] , [1,0] , [0,-1] , [-1,0]]

        mx = 0

        dis = 0

        x , y = 0 , 0 

        obstacle_set = {tuple(obstacle) for obstacle in obstacles}

        obstacle_set = set(obstacle_set)

        print(obstacles)

        for i in commands:

            if i == -1:

                dis = (dis + 1) %4

            elif i == -2:

                dis = (dis + 3) % 4

            else:

                for j in range(i):

                    # print(way[dis][0])

                    new_x , new_y = x + way[dis][0] , y + way[dis][1]

                    if (new_x , new_y) in obstacle_set:

                        break

                    x , y = new_x , new_y

                    val = x *x + y * y

                    mx = max(mx , val)

        return mx
