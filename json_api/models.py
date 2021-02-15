from django.db import models

# Create your models here.
class User(models.Model):
    given_id = models.CharField(max_length=64 , primary_key=True)
    real_name = models.CharField(max_length=64)
    time_zone = models.CharField(max_length=64)

    def __str__(self):
        return (f"User_id : {self.given_id} name: {self.real_name} time_zone : {self.time_zone}")

class Activity_Periods(models.Model):
    start_time = models.CharField(max_length=64)
    end_time = models.CharField(max_length=64)
    user_id = models.ForeignKey(User , on_delete=models.CASCADE , related_name="user")

    def __str__(self):
        #string representaion of object
        return (f"start_time : {self.start_time} end_time: {self.end_time} for {self.user_id.real_name}")