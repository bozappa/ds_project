# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stream.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='stream.proto',
  package='',
  syntax='proto3',
  serialized_options=b'P\001\242\002\003HLW',
  serialized_pb=b'\n\x0cstream.proto\"\x19\n\nMsgRequest\x12\x0b\n\x03img\x18\x01 \x01(\x0c\"\x19\n\x08MsgReply\x12\r\n\x05reply\x18\x01 \x01(\x05\x32\x34\n\tImageTest\x12\'\n\x07\x41nalyse\x12\x0b.MsgRequest\x1a\t.MsgReply\"\x00(\x01\x30\x01\x42\x08P\x01\xa2\x02\x03HLWb\x06proto3'
)




_MSGREQUEST = _descriptor.Descriptor(
  name='MsgRequest',
  full_name='MsgRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='img', full_name='MsgRequest.img', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=16,
  serialized_end=41,
)


_MSGREPLY = _descriptor.Descriptor(
  name='MsgReply',
  full_name='MsgReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reply', full_name='MsgReply.reply', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=43,
  serialized_end=68,
)

DESCRIPTOR.message_types_by_name['MsgRequest'] = _MSGREQUEST
DESCRIPTOR.message_types_by_name['MsgReply'] = _MSGREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MsgRequest = _reflection.GeneratedProtocolMessageType('MsgRequest', (_message.Message,), {
  'DESCRIPTOR' : _MSGREQUEST,
  '__module__' : 'stream_pb2'
  # @@protoc_insertion_point(class_scope:MsgRequest)
  })
_sym_db.RegisterMessage(MsgRequest)

MsgReply = _reflection.GeneratedProtocolMessageType('MsgReply', (_message.Message,), {
  'DESCRIPTOR' : _MSGREPLY,
  '__module__' : 'stream_pb2'
  # @@protoc_insertion_point(class_scope:MsgReply)
  })
_sym_db.RegisterMessage(MsgReply)


DESCRIPTOR._options = None

_IMAGETEST = _descriptor.ServiceDescriptor(
  name='ImageTest',
  full_name='ImageTest',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=70,
  serialized_end=122,
  methods=[
  _descriptor.MethodDescriptor(
    name='Analyse',
    full_name='ImageTest.Analyse',
    index=0,
    containing_service=None,
    input_type=_MSGREQUEST,
    output_type=_MSGREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_IMAGETEST)

DESCRIPTOR.services_by_name['ImageTest'] = _IMAGETEST

# @@protoc_insertion_point(module_scope)
