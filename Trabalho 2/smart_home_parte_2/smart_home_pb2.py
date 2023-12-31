# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: smart_home.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10smart_home.proto\x12\nsmart_home\")\n\x12TemperatureRequest\x12\x13\n\x0btemperature\x18\x01 \x01(\x02\"&\n\x13TemperatureResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"H\n\x0f\x41\x63tuatorRequest\x12&\n\x04type\x18\x01 \x01(\x0e\x32\x18.smart_home.ActuatorType\x12\r\n\x05value\x18\x02 \x01(\t\"5\n\rSensorRequest\x12$\n\x04type\x18\x01 \x01(\x0e\x32\x16.smart_home.SensorType\"*\n\x0bObjectValue\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"9\n\x0eObjectResponse\x12\'\n\x06values\x18\x01 \x03(\x0b\x32\x17.smart_home.ObjectValue*7\n\x0c\x41\x63tuatorType\x12\x08\n\x04LAMP\x10\x00\x12\x0e\n\nTHERMOSTAT\x10\x01\x12\r\n\tIRRIGATOR\x10\x02*9\n\nSensorType\x12\x0c\n\x08PRESENCE\x10\x00\x12\x0f\n\x0bTEMPERATURE\x10\x01\x12\x0c\n\x08HUMIDITY\x10\x02\x32\xc7\x01\n\x11ThermostatService\x12S\n\x0eSetTemperature\x12\x1e.smart_home.TemperatureRequest\x1a\x1f.smart_home.TemperatureResponse\"\x00\x12]\n\x18UpdateDesiredTemperature\x12\x1e.smart_home.TemperatureRequest\x1a\x1f.smart_home.TemperatureResponse\"\x00\x32\xf7\x01\n\rClientService\x12L\n\x11SetActuatorValues\x12\x1b.smart_home.ActuatorRequest\x1a\x1a.smart_home.ObjectResponse\x12L\n\x11GetActuatorValues\x12\x1b.smart_home.ActuatorRequest\x1a\x1a.smart_home.ObjectResponse\x12J\n\x0fGetSensorValues\x12\x19.smart_home.SensorRequest\x1a\x1a.smart_home.ObjectResponse0\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'smart_home_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_ACTUATORTYPE']._serialized_start=347
  _globals['_ACTUATORTYPE']._serialized_end=402
  _globals['_SENSORTYPE']._serialized_start=404
  _globals['_SENSORTYPE']._serialized_end=461
  _globals['_TEMPERATUREREQUEST']._serialized_start=32
  _globals['_TEMPERATUREREQUEST']._serialized_end=73
  _globals['_TEMPERATURERESPONSE']._serialized_start=75
  _globals['_TEMPERATURERESPONSE']._serialized_end=113
  _globals['_ACTUATORREQUEST']._serialized_start=115
  _globals['_ACTUATORREQUEST']._serialized_end=187
  _globals['_SENSORREQUEST']._serialized_start=189
  _globals['_SENSORREQUEST']._serialized_end=242
  _globals['_OBJECTVALUE']._serialized_start=244
  _globals['_OBJECTVALUE']._serialized_end=286
  _globals['_OBJECTRESPONSE']._serialized_start=288
  _globals['_OBJECTRESPONSE']._serialized_end=345
  _globals['_THERMOSTATSERVICE']._serialized_start=464
  _globals['_THERMOSTATSERVICE']._serialized_end=663
  _globals['_CLIENTSERVICE']._serialized_start=666
  _globals['_CLIENTSERVICE']._serialized_end=913
# @@protoc_insertion_point(module_scope)
