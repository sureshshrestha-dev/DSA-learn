import queue
import threading
import time

class SimpleMessageQueue:
    def __init__(self):
        self.topics = {}
        self.lock = threading.Lock()

    def create_topic(self, topic_name):
        with self.lock:
            if topic_name not in self.topics:
                self.topics[topic_name] = queue.Queue()
                print(f"Topic '{topic_name}' created.")

    def publish(self, topic_name, message):
        if topic_name in self.topics:
            self.topics[topic_name].put(message)
            # print(f"Published to {topic_name}: {message}")
        else:
            print(f"Topic {topic_name} does not exist.")

    def subscribe(self, topic_name, subscriber_name):
        def worker():
            while True:
                msg = self.topics[topic_name].get()
                if msg == "SHUTDOWN":
                    break
                print(f"Subscriber {subscriber_name} received: {msg}")
                self.topics[topic_name].task_done()

        t = threading.Thread(target=worker, daemon=True)
        t.start()
        return t

if __name__ == "__main__":
    mq = SimpleMessageQueue()
    mq.create_topic("updates")
    
    sub1 = mq.subscribe("updates", "Sub1")
    sub2 = mq.subscribe("updates", "Sub2")
    
    mq.publish("updates", "Hello Message 1")
    mq.publish("updates", "Hello Message 2")
    
    time.sleep(1) # Give time for subscribers to process
    mq.publish("updates", "SHUTDOWN")
    print("Message Queue simulation finished.")
