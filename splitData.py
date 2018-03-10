import csv


def split_csv_file(input_file, train_f, test_f):
    header_check = 0
    unique_user = 0
    list_of_rows = []
    train_data = []
    test_data = []

    with open(input_file, 'r') as f:
        for line in f:
            if header_check == 0:
                header_check += 1
                continue

            user, movie_id, rating, timestamp = line.split(',')
            timestamp = timestamp[:-2]  # to remove the /n and /r characters from the end

            if unique_user == 0:
                unique_user = user
                list_of_rows.append((user, movie_id, rating, timestamp))

            # we have reached a new user
            elif unique_user != user:
                split_proportion = int((1/3)*len(list_of_rows))

                #split_proportion = int((2/3)*len(list_of_rows))

                # test_half = list_of_rows[:split_proportion]
                # train_half = list_of_rows[split_proportion:]

                train_half = list_of_rows[:split_proportion]
                test_half = list_of_rows[split_proportion:int((2/3)*len(list_of_rows))]
                train_half.extend(list_of_rows[int((2/3)*len(list_of_rows)):])

                train_data.extend(train_half)
                test_data.extend(test_half)

                # flushing the list for new user
                list_of_rows = []
                unique_user = user
                list_of_rows.append((user, movie_id, rating, timestamp))

            else:
                list_of_rows.append((user, movie_id, rating, timestamp))

    with open(train_f,'w+', newline='') as out:
        csv_out=csv.writer(out)
        for row in train_data:
            csv_out.writerow(row)

    with open(test_f,'w+', newline='') as out:
        csv_out=csv.writer(out)
        for row in test_data:
            csv_out.writerow(row)



if __name__ == '__main__':
    ratings_file = "ml-20m/ratings.csv"
    train_file = "train_data.csv"
    test_file = "test_data.csv"
    split_csv_file(ratings_file, train_file, test_file)