import datetime
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from home.forms import EditDeviceForm
from home.models import Device, Sensor, SensorValue
from home.serializers import SensorValueSerializer

# Create your views here.



def home(request):
    device = Device.objects.all()
    today = datetime.date.today()
    for d in device:
        d.sensors = Sensor.objects.filter(device_id=d)

        for sensor in d.sensors:
            sensor.values = SensorValue.objects.filter(created__gte=today, sensor_id=sensor).order_by('-created').first()
            
    return render(request, "home/home.html", locals())


def graph_device(request, device_id):
    device = Device.objects.get(pk=device_id)
    today = datetime.date.today()
    sensors = Sensor.objects.filter(device_id=device)
    sensors_dict = {}
    for sensor in sensors:
        if not sensor.name in sensors_dict.keys():
            sensors_dict[sensor.name] = {}
            data = sensor.sensorvalue_set.filter(created__gte=today).order_by('created')
            if data:
                sensors_dict[sensor.name]['value'] = [
                    float(value.value) for value in data
                    ]
                sensors_dict[sensor.name]['date'] = [
                    str(date.created.strftime("%H-%M")) for date in data
                    ]
                sensors_dict[sensor.name]['max'] = int(max(sensors_dict[sensor.name]['value']))+5
                sensors_dict[sensor.name]['min'] = int(min(sensors_dict[sensor.name]['value']))-5
    return render(request, "home/charts.html", locals())



def edit_device(request, device_id):
    device = Device.objects.get(pk=device_id)
    today = datetime.date.today()
    sensors = Sensor.objects.filter(device_id=device)
    sensors_dict = {}
    dict_form = []
    for index, sensor in enumerate(sensors):
        dict_form.append(EditDeviceForm(request.POST or None, instance=sensor, prefix='%s' % (index)))
    
    if request.method == 'POST':
        for form in dict_form:
            obj = form.save()
    return render(request, "home/edit-device.html", locals())





#API


def add_sensor_value(request):

    return render(request, "index.html", locals())


"""
{
"device": 1,
	"sensors": [
			{
				"name": "температура",
				"value": 22.05,
				"sensor": 1234567890,
				"unit": "*C"
			},
			{
				"name": "температура в воде",
				"value": 20.05,
				"sensor": 1234555890,
				"unit": "*C"
			},
			{
				"name": "Влажность",
				"value": 59.05,
				"sensor": 1237867890,
				"unit": "%"
			},
		]
}   
"""

class AddSensorValue(APIView):
    def get(self, request):
        today = datetime.date.today()
        all_data = SensorValue.objects.filter(created__gte=today).order_by("-created")
        serializer = SensorValueSerializer(all_data, many=True)
        return Response({'posts': serializer.data})
 
 
    def post(self, request):
        device = request.data.get("device", None)
        if device is None:
            return Response({"status": "Нет данных устройства"})
        device_db = Device.objects.filter(device=device).first()
        if not device_db:
            device_db = Device.objects.create(
                device=device
            )
            device_db.save()
        sensors = request.data.get("sensors", None)
        if sensors is None:
            return Response({"status": "Нет данных датчиков"})
        for sensor in sensors:
            sensor_db = Sensor.objects.filter(device_id=device_db,sensor=sensor["sensor"]).first()
            if not sensor_db:
                sensor_db = Sensor.objects.create(
                    sensor=sensor["sensor"],
                    name = sensor["name"],
                    unit = sensor["unit"],
                    device_id=device_db
                )
                sensor_db.save()
            sensor_value_db = SensorValue.objects.create(
                sensor_id=sensor_db,
                value=sensor["value"],
            )
            sensor_value_db.save()
        return Response({'post': "test post"})