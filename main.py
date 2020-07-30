import airsim
import io
import PIL.Image as Image
import matplotlib.pyplot as plt
import math
import pprint
import time
import subprocess



def showImageByCam(cn):
    png_image = client.simGetImage(str(cn), airsim.ImageType.Scene)
    image = Image.open(io.BytesIO(png_image))
    imgplot = plt.imshow(image)
    plt.show()


def setHeight(z):
    vx = 0
    vy = 0
    duration = (-1 * z) + 1
    client.moveByVelocityZAsync(vx, vy, z, duration, airsim.DrivetrainType.MaxDegreeOfFreedom,
                                airsim.YawMode(False, 0)).join()


def moveForward(distance, speed, targetheight):
    z = -1 * targetheight
    vx = speed
    duration = distance / speed
    vy = 0
    client.moveByVelocityZAsync(vx, vy, z, duration, airsim.DrivetrainType.MaxDegreeOfFreedom,
                                airsim.YawMode(False, 0)).join()


def getDistance(lat1, lon1, lat2, lon2):
    R = 6373.0
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance * 21.075052889902892


def getLatLonAlt():
    gps_data = client.getGpsData().gnss.geo_point
    return (gps_data)


def getHeight():
    return (client.getDistanceSensorData().distance)



client = airsim.MultirotorClient(ip="192.168.0.7", port=41451)
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)
print(client.getGpsData())
setHeight(-1)
moveForward(30,5,1)
time.sleep(10)
client.reset()
