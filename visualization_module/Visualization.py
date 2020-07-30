import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from drone_telemetry import drone_data
from matplotlib.gridspec import GridSpec

data = drone_data()

style.use('ggplot')
fig = plt.figure()
gs = GridSpec(3, 3, figure=fig)

ax1 = fig.add_subplot(gs[0, 0])
ax2 = fig.add_subplot(gs[0, 1])
ax3 = fig.add_subplot(gs[0, 2])
ax4 = fig.add_subplot(gs[1, 0])
ax5 = fig.add_subplot(gs[1, 1])
ax5 = fig.add_subplot(gs[1, 2])

fig.suptitle("Telemetry")


def animate(i):
    global x
    data.get_imu_data()
    data.get_gps_data()

    ax1.cla()
    ax2.cla()
    ax3.cla()
    ax4.cla()

    ax1.set_title("IMU Linear Acceleration")
    ax2.set_title("IMU Orientation")
    ax3.set_title("IMU Angular Velocity")
    ax4.set_title("GPS Velocity")

    ax1.plot(data.imu_ts, data.imu_lax, label="Linear Acceleration X")
    ax1.plot(data.imu_ts, data.imu_lay, label="Linear Acceleration Y")
    ax1.plot(data.imu_ts, data.imu_laz, label="Linear Acceleration Z")

    ax2.plot(data.imu_ts, data.imu_ox, label="Orientation X")
    ax2.plot(data.imu_ts, data.imu_oy, label="Orientation Y")
    ax2.plot(data.imu_ts, data.imu_oz, label="Orientation Z")

    ax3.plot(data.imu_ts, data.imu_avx, label="Angular Velocity X")
    ax3.plot(data.imu_ts, data.imu_avy, label="Angular Velocity Y")
    ax3.plot(data.imu_ts, data.imu_avz, label="Angular Velocity  Z")

    ax4.plot(data.gps_ts, data.gps_xv, label="GPS X Velocity")
    ax4.plot(data.gps_ts, data.gps_yv, label="GPS Y Velocity")
    ax4.plot(data.gps_ts, data.gps_zv, label="GPS Z Velocity")

    ax1.legend(loc='best')
    ax2.legend(loc='best')
    ax3.legend(loc='best')
    ax4.legend(loc='best')


ani = animation.FuncAnimation(fig, animate, interval=200)

plt.show()
