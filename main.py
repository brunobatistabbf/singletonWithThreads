from databaseAccessThread import DatabaseAccessThread

if __name__ == '__main__':
    threads = []

    for i in range(5):
        thread = DatabaseAccessThread()
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()