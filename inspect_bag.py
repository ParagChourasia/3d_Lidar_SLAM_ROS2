from rosbags.rosbag1 import Reader

def inspect_bag(path):
    with Reader(path) as reader:
        print(f"Bag: {path}")
        print(f"Duration: {reader.duration / 1e9:.2f}s")
        print(f"Messages: {reader.message_count}")
        print("\nTopics:")
        for topic, info in reader.topics.items():
            print(f"  {topic}: {info.msgtype} ({info.msgcount} msgs)")

if __name__ == "__main__":
    inspect_bag("/home/parag/li_slam_ws/src/li_slam_ros2/data/park_dataset.bag")
