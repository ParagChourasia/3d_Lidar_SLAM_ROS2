# 3D LiDAR SLAM ROS 2 (Humble)

[![Link to Video](https://img.shields.io/badge/Demo-Video-red?style=for-the-badge&logo=youtube)](./src/li_slam_ros2/doc/li_slam.mkv)

This repository contains a comprehensive ROS 2 Humble workspace for 3D LiDAR-Inertial SLAM. It integrates [lidarslam_ros2](https://github.com/rsasaki0109/lidarslam_ros2) with [LIO-SAM](https://github.com/TixiaoShan/LIO-SAM)'s IMU preintegration techniques to provide robust mapping and localization in real-time.

## Key Features
- **LiDAR-Inertial Fusion**: Combines 3D LiDAR data with high-frequency IMU inputs.
- **Loop Closure**: Automated loop detection and pose-graph optimization using `g2o`.
- **NDT Matching**: High-performance scan matching using `ndt_omp_ros2`.
- **ROS 2 Humble Ready**: Fully compatible with the ROS 2 Humble Hawksbill distribution.

## Demo
A demo video of the SLAM system in action can be found here:
**[View Demo Video (li_slam.mkv)](./src/li_slam_ros2/doc/li_slam.mkv)**

> [!NOTE]  
> The video file is approximately 166MB. You may need to download it to view it properly if the browser preview does not support the .mkv format.

## Installation

### Prerequisites
1. **ROS 2 Humble**: [Installation Guide](https://docs.ros.org/en/humble/Installation.html)
2. **GTSAM**:
   ```bash
   sudo add-apt-repository ppa:borglab/gtsam-release-4.1
   sudo apt update
   sudo apt install libgtsam-dev libgtsam-unstable-dev
   ```

### Building the Workspace
```bash
# Clone the repository (if you haven't already)
git clone https://github.com/ParagChourasia/3d_Lidar_SLAM_ROS2.git
cd 3d_Lidar_SLAM_ROS2

# Install ROS dependencies
rosdep update
rosdep install --from-paths src --ignore-src -yr

# Build
colcon build --cmake-args -DCMAKE_BUILD_TYPE=Release
```

## Quick Start

### Launching the SLAM System
1. **Launch RViz**:
   ```bash
   rviz2 -d src/li_slam_ros2/scanmatcher/rviz/lio.rviz
   ```
2. **Launch LIO SLAM**:
   ```bash
   ros2 launch scanmatcher lio.launch.py
   ```
3. **Play a Bag File**:
   ```bash
   ros2 bag play <path_to_your_bag_directory>/
   ```

## References
- This project is a combination of [lidarslam_ros2](https://github.com/rsasaki0109/lidarslam_ros2) and [LIO-SAM](https://github.com/TixiaoShan/LIO-SAM).
- Special thanks to [rsasaki0109](https://github.com/rsasaki0109) for the base implementation.

## Repository Contents
- `src/li_slam_ros2`: Main SLAM packages.
- `src/li_slam_ros2/doc/`: Project documentation and demo videos.
- `inspect_bag.py` & `fix_metadata.py`: Utility scripts for ROS 2 bag management.
