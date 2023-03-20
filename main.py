def parallel_processing(n, m, data):
    output = []
    time_arr = [0] * n

    for i in range(m):
        thread = min(range(n), key=lambda x: time_arr[x])
        output.append((thread, time_arr[thread]))
        time_arr[thread] += data[i]

    return output

def main():
    n, m = map(int, input("Input: ").split())
    data = list(map(int, input("Input: ").split()))

    result = parallel_processing(n,m,data)

    for thread, start_time in result:
        print(thread, start_time)

if __name__ == "__main__":
    main()
