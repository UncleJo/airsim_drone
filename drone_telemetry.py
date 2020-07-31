import airsim

lat0 = 47.641193601334486
lon0 = -122.1399660110359
h0 = 122.5479507446289


class drone_data:
    gps_ts = []
    gps_xv = []
    gps_yv = []
    gps_zv = []
    imu_ts = []
    imu_ox = []
    imu_oy = []
    imu_oz = []
    imu_avx = []
    imu_avy = []
    imu_avz = []
    imu_lax = []
    imu_lay = []
    imu_laz = []
    lidar_ts = []
    lidar_ox = []
    lidar_oy = []
    lidar_oz = []
    lidar_px = []
    lidar_py = []
    lidar_pz = []
    line_done = 0

    def __init__(self):
        self.client = airsim.MultirotorClient(ip="192.168.0.7", port=41451)
        self.client.confirmConnection()
        self.client.enableApiControl(True)
        self.client.armDisarm(True)

    def get_gps_data(self):
        data = self.client.getGpsData()
        self.gps_ts.append(float(data.time_stamp) / 1000000000)
        self.gps_zv.append(float(data.gnss.velocity.z_val) * -1)
        self.gps_xv.append(float(data.gnss.velocity.x_val))
        self.gps_yv.append(float(data.gnss.velocity.y_val))

    def get_imu_data(self):
        data1 = self.client.getImuData()
        self.imu_ts.append(float(data1.time_stamp) / 1000000000)
        self.imu_ox.append(float(data1.orientation.x_val))
        self.imu_oy.append(float(data1.orientation.y_val))
        self.imu_oz.append(float(data1.orientation.z_val))
        self.imu_avx.append(float(data1.angular_velocity.x_val))
        self.imu_avy.append(float(data1.angular_velocity.y_val))
        self.imu_avz.append(float(data1.angular_velocity.z_val))
        self.imu_lax.append(float(data1.linear_acceleration.x_val))
        self.imu_lay.append(float(data1.linear_acceleration.y_val))
        self.imu_laz.append(float(data1.linear_acceleration.z_val) * -1)

    def get_lidar_data(self):
        data2 = self.client.getLidarData()
        self.lidar_ts.append(float(data2.time_stamp) / 1000000000)
        self.lidar_ox.append(float(data2.pose.orientation.x_val))
        self.lidar_oy.append(float(data2.pose.orientation.y_val))
        self.lidar_oz.append(float(data2.pose.orientation.z_val))
        self.lidar_px.append(float(data2.pose.position.x_val))
        self.lidar_py.append(float(data2.pose.position.y_val))
        self.lidar_pz.append(float(data2.pose.position.z_val) * -1)

