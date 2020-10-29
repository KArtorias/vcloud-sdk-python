# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: base.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='base.proto',
  package='Vcloud.Models.Base',
  syntax='proto3',
  serialized_options=b'\n\035com.bytedanceapi.model.commonB\004BaseP\001Z\010.;models\240\001\001\330\001\001\302\002\000\312\002\022Vcloud\\Models\\Base\342\002\031Vcloud\\Models\\GPBMetadata',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nbase.proto\x12\x12Vcloud.Models.Base\"\x99\x01\n\x10ResponseMetadata\x12\x11\n\tRequestId\x18\x01 \x01(\t\x12\x0e\n\x06\x41\x63tion\x18\x02 \x01(\t\x12\x0f\n\x07Version\x18\x03 \x01(\t\x12\x0f\n\x07Service\x18\x04 \x01(\t\x12\x0e\n\x06Region\x18\x05 \x01(\t\x12\x30\n\x05\x45rror\x18\x06 \x01(\x0b\x32!.Vcloud.Models.Base.ResponseError\".\n\rResponseError\x12\x0c\n\x04\x43ode\x18\x01 \x01(\t\x12\x0f\n\x07Message\x18\x02 \x01(\tBk\n\x1d\x63om.bytedanceapi.model.commonB\x04\x42\x61seP\x01Z\x08.;models\xa0\x01\x01\xd8\x01\x01\xc2\x02\x00\xca\x02\x12Vcloud\\Models\\Base\xe2\x02\x19Vcloud\\Models\\GPBMetadatab\x06proto3'
)




_RESPONSEMETADATA = _descriptor.Descriptor(
  name='ResponseMetadata',
  full_name='Vcloud.Models.Base.ResponseMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='RequestId', full_name='Vcloud.Models.Base.ResponseMetadata.RequestId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Action', full_name='Vcloud.Models.Base.ResponseMetadata.Action', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Version', full_name='Vcloud.Models.Base.ResponseMetadata.Version', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Service', full_name='Vcloud.Models.Base.ResponseMetadata.Service', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Region', full_name='Vcloud.Models.Base.ResponseMetadata.Region', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Error', full_name='Vcloud.Models.Base.ResponseMetadata.Error', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=35,
  serialized_end=188,
)


_RESPONSEERROR = _descriptor.Descriptor(
  name='ResponseError',
  full_name='Vcloud.Models.Base.ResponseError',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Code', full_name='Vcloud.Models.Base.ResponseError.Code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='Message', full_name='Vcloud.Models.Base.ResponseError.Message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=190,
  serialized_end=236,
)

_RESPONSEMETADATA.fields_by_name['Error'].message_type = _RESPONSEERROR
DESCRIPTOR.message_types_by_name['ResponseMetadata'] = _RESPONSEMETADATA
DESCRIPTOR.message_types_by_name['ResponseError'] = _RESPONSEERROR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ResponseMetadata = _reflection.GeneratedProtocolMessageType('ResponseMetadata', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSEMETADATA,
  '__module__' : 'base_pb2'
  # @@protoc_insertion_point(class_scope:Vcloud.Models.Base.ResponseMetadata)
  })
_sym_db.RegisterMessage(ResponseMetadata)

ResponseError = _reflection.GeneratedProtocolMessageType('ResponseError', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSEERROR,
  '__module__' : 'base_pb2'
  # @@protoc_insertion_point(class_scope:Vcloud.Models.Base.ResponseError)
  })
_sym_db.RegisterMessage(ResponseError)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)