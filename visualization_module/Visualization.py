import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from drone_telemetry import drone_data
from matplotlib.gridspec import GridSpec

data = drone_data()
time_range_of_graphs = 50

style.use('ggplot')
fig = plt.figure()
gs = GridSpec(3, 3, figure=fig)

ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[0, 1])
ax3 = fig.add_subplot(gs[0, 2])
ax4 = fig.add_subplot(gs[1, 0])
ax5 = fig.add_subplot(gs[1, 1])
ax6 = fig.add_subplot(gs[1, 2])

fig.suptitle("Telemetry")


def animate(i):
    global x
    data.get_imu_data()
    data.get_gps_data()
    data.get_lidar_data()

    if len(data.lidar_ts) < time_range_of_graphs:
        no_of_data=0
    else:
        no_of_data=time_range_of_graphs
    ax1.cla()
    ax2.cla()
    ax3.cla()
    ax4.cla()
    ax5.cla()
    ax6.cla()

    ax1.set_title("IMU Linear Acceleration")
    ax2.set_title("IMU Orientation")
    ax3.set_title("IMU Angular Velocity")
    ax4.set_title("GPS Velocity")
    ax5.set_title("Lidar Position")
    ax6.set_title("Lidar Orientation")

    ax1.plot(data.imu_ts[-no_of_data:], data.imu_lax[-no_of_data:], label="Linear Acceleration X")
    ax1.plot(data.imu_ts[-no_of_data:], data.imu_lay[-no_of_data:], label="Linear Acceleration Y")
    ax1.plot(data.imu_ts[-no_of_data:], data.imu_laz[-no_of_data:], label="Linear Acceleration Z")

    ax2.plot(data.imu_ts[-no_of_data:], data.imu_ox[-no_of_data:], label="Orientation X")
    ax2.plot(data.imu_ts[-no_of_data:], data.imu_oy[-no_of_data:], label="Orientation Y")
    ax2.plot(data.imu_ts[-no_of_data:], data.imu_oz[-no_of_data:], label="Orientation Z")

    ax3.plot(data.imu_ts[-no_of_data:], data.imu_avx[-no_of_data:], label="Angular Velocity X")
    ax3.plot(data.imu_ts[-no_of_data:], data.imu_avy[-no_of_data:], label="Angular Velocity Y")
    ax3.plot(data.imu_ts[-no_of_data:], data.imu_avz[-no_of_data:], label="Angular Velocity  Z")

    ax4.plot(data.gps_ts[-no_of_data:], data.gps_xv[-no_of_data:], label="GPS X Velocity")
    ax4.plot(data.gps_ts[-no_of_data:], data.gps_yv[-no_of_data:], label="GPS Y Velocity")
    ax4.plot(data.gps_ts[-no_of_data:], data.gps_zv[-no_of_data:], label="GPS Z Velocity")

    ax5.plot(data.lidar_ts[-no_of_data:], data.lidar_px[-no_of_data:], label="Lidar X Position")
    ax5.plot(data.lidar_ts[-no_of_data:], data.lidar_py[-no_of_data:], label="Lidar Y Position")
    ax5.plot(data.lidar_ts[-no_of_data:], data.lidar_pz[-no_of_data:], label="Lidar Z Position")

    ax6.plot(data.lidar_ts[-no_of_data:], data.lidar_ox[-no_of_data:], label="Lidar X Orientation")
    ax6.plot(data.lidar_ts[-no_of_data:], data.lidar_oy[-no_of_data:], label="Lidar Y Orientation")
    ax6.plot(data.lidar_ts[-no_of_data:], data.lidar_oz[-no_of_data:], label="Lidar Z Orientation")

    ax1.legend(loc='best')
    ax2.legend(loc='best')
    ax3.legend(loc='best')
    ax4.legend(loc='best')
    ax5.legend(loc='best')
    ax6.legend(loc='best')


ani = animation.FuncAnimation(fig, animate, interval=200)

plt.show()
