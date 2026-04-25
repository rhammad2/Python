import time
import random
from threading import Thread, current_thread, Condition

'''
condition is used to make the threads wait and notify each other.
It helps the LogGenerator and LogArchiver take turns safely.

is_empty keeps track of the buffer state.
If is_empty is True, the generator can write a log.
If is_empty is False, the archiver can process the log.
'''


class LogBuffer:
    def __init__(self):
        self.current_log = None
        self.is_empty = True
        self.condition = Condition()

    def write_log(self, log_msg):
        with self.condition:
            while not self.is_empty:
                self.condition.wait()

            print(f"{current_thread().name} writing: {log_msg}")
            self.current_log = log_msg
            self.is_empty = False

            self.condition.notify()

    def archive_log(self):
        with self.condition:
            while self.is_empty:
                self.condition.wait()

            print(f"{current_thread().name} archiving: {self.current_log}")
            archived_log = self.current_log
            self.current_log = None
            self.is_empty = True

            self.condition.notify()
            return archived_log


class LogGenerator(Thread):
    def __init__(self, buffer, log_count):
        super().__init__(name="LogGenerator")
        self.buffer = buffer
        self.log_count = log_count

    def run(self):
        for i in range(1, self.log_count + 1):
            time.sleep(random.random())
            log_msg = f"log_entry_{i}"
            self.buffer.write_log(log_msg)


class LogArchiver(Thread):
    def __init__(self, buffer, log_count):
        super().__init__(name="LogArchiver")
        self.buffer = buffer
        self.log_count = log_count

    def run(self):
        for _ in range(self.log_count):
            time.sleep(random.random())
            self.buffer.archive_log()


def main():
    LOG_COUNT = 5
    buffer = LogBuffer()

    gen = LogGenerator(buffer, LOG_COUNT)
    arc = LogArchiver(buffer, LOG_COUNT)

    gen.start()
    arc.start()

    gen.join()
    arc.join()
    print("\nLog Maintenance Complete.")


if __name__ == "__main__":
    main()