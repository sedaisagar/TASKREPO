# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: tasks/grpc/tasks.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'tasks/grpc/tasks.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16tasks/grpc/tasks.proto\x12\x1ctask_processing_system.tasks\x1a\x1cgoogle/protobuf/struct.proto\"B\n\x12TaskPayloadRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x0f\n\x07subject\x18\x02 \x01(\t\x12\x0c\n\x04\x62ody\x18\x03 \x01(\t\"C\n\x13TaskPayloadResponse\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x0f\n\x07subject\x18\x02 \x01(\t\x12\x0c\n\x04\x62ody\x18\x03 \x01(\t\"O\n\x10TasksListRequest\x12.\n\x08_filters\x18\x01 \x01(\x0b\x32\x17.google.protobuf.StructH\x00\x88\x01\x01\x42\x0b\n\tX_filters\"Q\n\x11TasksListResponse\x12<\n\x07results\x18\x01 \x03(\x0b\x32+.task_processing_system.tasks.TasksResponse\"f\n\x0cTasksRequest\x12\x0f\n\x02id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12>\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x30.task_processing_system.tasks.TaskPayloadRequestB\x05\n\x03_id\"\xd8\x01\n\rTasksResponse\x12\x0f\n\x02id\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12?\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x31.task_processing_system.tasks.TaskPayloadResponse\x12\x13\n\x06status\x18\x03 \x01(\tH\x01\x88\x01\x01\x12\x17\n\ncreated_at\x18\x04 \x01(\tH\x02\x88\x01\x01\x12\x17\n\nupdated_at\x18\x05 \x01(\tH\x03\x88\x01\x01\x42\x05\n\x03_idB\t\n\x07_statusB\r\n\x0b_created_atB\r\n\x0b_updated_at2\xe1\x01\n\x0fTasksController\x12\x63\n\x06\x43reate\x12*.task_processing_system.tasks.TasksRequest\x1a+.task_processing_system.tasks.TasksResponse\"\x00\x12i\n\x04List\x12..task_processing_system.tasks.TasksListRequest\x1a/.task_processing_system.tasks.TasksListResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tasks.grpc.tasks_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_TASKPAYLOADREQUEST']._serialized_start=86
  _globals['_TASKPAYLOADREQUEST']._serialized_end=152
  _globals['_TASKPAYLOADRESPONSE']._serialized_start=154
  _globals['_TASKPAYLOADRESPONSE']._serialized_end=221
  _globals['_TASKSLISTREQUEST']._serialized_start=223
  _globals['_TASKSLISTREQUEST']._serialized_end=302
  _globals['_TASKSLISTRESPONSE']._serialized_start=304
  _globals['_TASKSLISTRESPONSE']._serialized_end=385
  _globals['_TASKSREQUEST']._serialized_start=387
  _globals['_TASKSREQUEST']._serialized_end=489
  _globals['_TASKSRESPONSE']._serialized_start=492
  _globals['_TASKSRESPONSE']._serialized_end=708
  _globals['_TASKSCONTROLLER']._serialized_start=711
  _globals['_TASKSCONTROLLER']._serialized_end=936
# @@protoc_insertion_point(module_scope)
