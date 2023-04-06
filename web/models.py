# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class InfoDevice(models.Model):
    id_device = models.IntegerField(primary_key=True)
    status_device = models.IntegerField()
    production_time_device = models.DateTimeField()
    accuracy_device = models.FloatField()
    num_device = models.IntegerField()
    name_device = models.CharField(max_length=255)
    workshop_id_device = models.IntegerField()
    tel = models.CharField(max_length=255)
    product_by = models.CharField(max_length=255)
    specification_device = models.CharField(max_length=255)
    model_device = models.CharField(max_length=255)
    reliability_device = models.CharField(max_length=255)
    use_process_id_device = models.IntegerField()
    type_device = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'info_device'


class InfoProcess(models.Model):
    id_process = models.IntegerField()
    id_production = models.IntegerField()
    id_worker = models.IntegerField()
    id_line = models.IntegerField()
    id_device = models.IntegerField(primary_key=True)
    name_process = models.CharField(max_length=255)
    needed_time_process = models.DateTimeField()
    needed_tool_process = models.CharField(max_length=255)
    craft_process = models.CharField(max_length=255)

    class Meta:
        managed = True
        db_table = 'info_process'
        unique_together = (('id_device', 'id_line', 'id_process', 'id_production', 'id_worker'),)


class InfoProduct(models.Model):
    id_product = models.IntegerField(primary_key=True)
    name_product = models.CharField(max_length=255)
    part_composition_product = models.CharField(max_length=255)
    specification_product = models.CharField(max_length=255)
    model_product = models.CharField(max_length=255)
    planned_production = models.IntegerField()
    size_production = models.FloatField()
    order_number_production = models.CharField(max_length=255)
    weight_production = models.FloatField()
    produce_process_id_production = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'info_product'


class InfoProductLine(models.Model):
    id_line = models.IntegerField(primary_key=True)
    status_line = models.IntegerField()
    shift_system_line = models.CharField(max_length=255)
    current_time_line = models.DateTimeField()
    quality_line = models.CharField(max_length=255)
    reliability_line = models.FloatField()
    num_ingress_entities_line = models.IntegerField()
    num_egress_entities_line = models.IntegerField()
    efficiency = models.FloatField()
    cost_line = models.FloatField()
    energy_consumption_line = models.FloatField()
    actual_capacity_line = models.FloatField()
    design_capacity_line = models.FloatField()
    responsibility_process_id_line = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'info_product_line'


class InfoWorker(models.Model):
    id_worker = models.IntegerField(primary_key=True)
    name_worker = models.CharField(max_length=255)
    tel_worker = models.CharField(max_length=255)
    worktime_worker = models.DateTimeField()
    department_worker = models.CharField(max_length=255)
    attendence_state = models.IntegerField()
    sex_worker = models.CharField(max_length=16)
    team_id = models.IntegerField()
    workshop_id = models.IntegerField()
    category_worker = models.CharField(max_length=255)
    responsibility_process_id_worker = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'info_worker'
