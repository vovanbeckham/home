from django.db import models




class Device(models.Model):
    device = models.PositiveIntegerField(default=0)
    room_name = models.CharField(max_length=200, default="комната")


    def __str__(self) -> str:
        return self.room_name
    

class Sensor(models.Model):
    sensor = models.PositiveIntegerField(default=0)
    name = models.CharField(max_length=200)
    unit = models.CharField(max_length=20)
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.name
    

class SensorValue(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=6, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return str(self.value)
    


class SensorValueAvgDay(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return str(self.value)


