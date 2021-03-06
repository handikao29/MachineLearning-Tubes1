from scipy.spatial import distance

class Agglomerative_hierarchical:
    def __init__(self, data, n_cluster, linkage):
        self.data = data
        self.linkage = linkage
        self.n_cluster = n_cluster
        self.n_iterate = len(self.data) - n_cluster

    def Agglo(self):
        # make 2d matrix
        length_data = len(self.data)
        self.matrix = [0] * (length_data-1)
        for i in range(length_data-1):
            self.matrix[i] = [0] * length_data

        for i in range(length_data-1):
            self.matrix[i][i] = float('inf')
        # list of index that's lost because of merging
        self.lost_index = []
        # create dict for save the cluster with the lowest index as key
        self.dict_list = {}
        self.last_cl = []
        # start compute
        for iterate in range(self.n_iterate):
            for row in range(length_data-1): #no need to compute the last index in matrix because it's all zero
                if row in self.lost_index:
                    continue
                x = self.dict_list.get(row, False)
                if (x==False):
                    # row is single
                    temp_list_x = []
                    temp_list_x.append(row)
                    self.calculate_distance(temp_list_x)
                else:
                    # row isnt single
                    self.calculate_distance(x)

            # merging two cluster
            self.merging()

        # singleton cluster
        for row in range(length_data):
            last = self.dict_list.get(row, True)
            if ((row not in self.lost_index) and (last==True)):
                self.last_cl.append(row)

        self.all_cluster = []
        if len(self.last_cl) > 0:
            self.last_cl.sort()
            for singleton in self.last_cl:
                temp_list = []
                temp_list.append(singleton)
                self.all_cluster.append(temp_list)

        for key, value in self.dict_list.items():
            self.all_cluster.append(value)

        self.label = []
        for i in range(length_data):
            for j in range(len(self.all_cluster)):
                lst = self.all_cluster[j]
                if i in lst:
                    self.label.append(j)
                    break




    def merging(self):
        min = float('inf')
        tuple_index = ()
        length_data = len(self.data)
        for row in range(length_data-1):
            if row in self.lost_index:
                continue
            for column in range(row+1, length_data):
                if column in self.lost_index:
                    continue
                if (self.matrix[row][column] < min):
                    min = self.matrix[row][column]
                    tuple_index = (row, column)

        # get minimum and the tuple
        x = tuple_index[0]
        y = tuple_index[1]

        map_x = self.dict_list.get(x, False)
        if map_x == False:
            map_y = self.dict_list.get(y, False)
            if map_y == False:
                list_of_x_y = []
                list_of_x_y.append(x)
                list_of_x_y.append(y)
                list_of_x_y.sort()
                self.dict_list[x] = list_of_x_y
            else:
                map_y.append(x)
                map_y.sort()
                self.dict_list[x] = map_y
                del self.dict_list[y]
        else:
            map_y = self.dict_list.get(y, False)
            if map_y == False:
                map_x.append(y)
                map_x.sort()
                self.dict_list[x] = map_x
            else:
                for col in map_y:
                    map_x.append(col)
                map_x.sort()
                self.dict_list[x] = map_x
                del self.dict_list[y]

        self.lost_index.append(y)
        self.lost_index.sort()


    def calculate_distance(self, cl1):
        length_data = len(self.data)
        index_row = cl1[0]
        for column in range(index_row+1, length_data):
            if column in self.lost_index:
                continue
            y = self.dict_list.get(column, False)
            if (y == False):
                list_y = []
                list_y.append(column)
                if self.linkage == "single":
                    self.dist_single(cl1, list_y)
                elif self.linkage == "complete":
                    self.dist_complete(cl1, list_y)
                elif self.linkage == "average":
                    self.dist_avg(cl1, list_y)
                    # self.dist_complete(cl1, list_y)
                elif self.linkage == "average_group":
                    self.dist_avg_group(cl1, list_y)
                    # self.dist_complete(cl1, list_y)
            else:
                if self.linkage == "single":
                    self.dist_single(cl1, y)
                elif self.linkage == "complete":
                    self.dist_complete(cl1, y)
                elif self.linkage == "average":
                    self.dist_avg(cl1, y)
                    # self.dist_complete(cl1, list_y)
                elif self.linkage == "average_group":
                    self.dist_avg_group(cl1, y)
                    # self.dist_complete(cl1, list_y)


                # self.dist_single(cl1, y)


    def dist_single(self, list_x, list_y):
        min = float('inf')
        for index_row in list_x:
            for index_column in list_y:
                dist = distance.euclidean(self.data[index_row], self.data[index_column])
                if (dist < min):
                    min = dist
        self.matrix[list_x[0]][list_y[0]] = min

    def dist_complete(self, list_x, list_y):
        max = float('-inf')
        for index_row in list_x:
            for index_column in list_y:
                dist = distance.euclidean(self.data[index_row], self.data[index_column])
                if (dist > max):
                    max = dist
        self.matrix[list_x[0]][list_y[0]] = max

    def dist_avg_group(self, list_x, list_y):
        list_cl1 = []
        list_cl2 = []
        for index in list_x:
            list_cl1.append(self.data[index])

        for index in list_y:
            list_cl2.append(self.data[index])

        avg_cl1 = np.mean(list_cl1, axis=0)
        avg_cl2 = np.mean(list_cl2, axis=0)
        dist = distance.euclidean(avg_cl1, avg_cl2)
        self.matrix[list_x[0]][list_y[0]] = dist

    def dist_avg(self, list_x, list_y):
        sum = 0
        n = len(list_x) + len(list_y)
        for row in list_x:
            for col in list_y:
                sum += distance.euclidean(self.data[row], self.data[col])

        dist = sum / n
        self.matrix[list_x[0]][list_y[0]] = dist
