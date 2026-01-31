import yaml

def fix_metadata(path):
    with open(path, 'r') as f:
        data = yaml.safe_load(f)
    
    new_topics = []
    for topic in data['rosbag2_bagfile_information']['topics_with_message_count']:
        tm = topic['topic_metadata']
        new_tm = {
            'name': tm['name'],
            'offered_qos_profiles': "",
            'serialization_format': tm['serialization_format'],
            'type': tm['type']
        }
        topic['topic_metadata'] = new_tm
        new_topics.append(topic)
    
    data['rosbag2_bagfile_information']['topics_with_message_count'] = new_topics
    
    # Also ensure version is 9 or whatever is in the good example
    data['rosbag2_bagfile_information']['version'] = 9

    with open(path, 'w') as f:
        # We need to manually dump to ensure offered_qos_profiles: ""
        # yaml.dump might dump it as offered_qos_profiles: ''
        # Let's try to use a custom dumper or just string replacement if needed.
        yaml.dump(data, f, default_flow_style=False)

if __name__ == "__main__":
    fix_metadata("/home/parag/li_slam_ws/src/li_slam_ros2/data/park_dataset_ros2_sqlite3/metadata.yaml")
