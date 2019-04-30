# Copyright (c) 2016-2017 Anki, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Autogenerated python message buffer code.
Source: clad/robotInterface/messageToActiveObject.clad
Full command line: ../tools/message-buffers/emitters/Python_emitter.py -C ../robot/clad/src/ -o ../generated/cladPython// clad/robotInterface/messageToActiveObject.clad
"""

from __future__ import absolute_import
from __future__ import print_function

def _modify_path():
  import inspect, os, sys
  search_paths = [
    '../..',
    '../../../../tools/message-buffers/support/python',
  ]
  currentpath = os.path.abspath(os.path.dirname(inspect.getfile(inspect.currentframe())))
  for search_path in search_paths:
    search_path = os.path.normpath(os.path.abspath(os.path.realpath(os.path.join(currentpath, search_path))))
    if search_path not in sys.path:
      sys.path.insert(0, search_path)
_modify_path()

import msgbuffers

Anki = msgbuffers.Namespace()
Anki.Cozmo = msgbuffers.Namespace()

from clad.types.ledTypes import Anki as _Anki
Anki.update(_Anki.deep_clone())

class SetAccessoryDiscovery(object):
  "Generated message-passing message."

  __slots__ = (
    '_enable', # bool
  )

  @property
  def enable(self):
    "bool enable struct property."
    return self._enable

  @enable.setter
  def enable(self, value):
    self._enable = msgbuffers.validate_bool(
      'SetAccessoryDiscovery.enable', value)

  def __init__(self, enable=False):
    self.enable = enable

  @classmethod
  def unpack(cls, buffer):
    "Reads a new SetAccessoryDiscovery from the given buffer."
    reader = msgbuffers.BinaryReader(buffer)
    value = cls.unpack_from(reader)
    if reader.tell() != len(reader):
      raise msgbuffers.ReadError(
        ('SetAccessoryDiscovery.unpack received a buffer of length {length}, ' +
        'but only {position} bytes were read.').format(
        length=len(reader), position=reader.tell()))
    return value

  @classmethod
  def unpack_from(cls, reader):
    "Reads a new SetAccessoryDiscovery from the given BinaryReader."
    _enable = bool(reader.read('b'))
    return cls(_enable)

  def pack(self):
    "Writes the current SetAccessoryDiscovery, returning bytes."
    writer = msgbuffers.BinaryWriter()
    self.pack_to(writer)
    return writer.dumps()

  def pack_to(self, writer):
    "Writes the current SetAccessoryDiscovery to the given BinaryWriter."
    writer.write(int(self._enable), 'b')

  def __eq__(self, other):
    if type(self) is type(other):
      return self._enable == other._enable
    else:
      return NotImplemented

  def __ne__(self, other):
    if type(self) is type(other):
      return not self.__eq__(other)
    else:
      return NotImplemented

  def __len__(self):
    return (msgbuffers.size(self._enable, 'b'))

  def __str__(self):
    return '{type}(enable={enable})'.format(
      type=type(self).__name__,
      enable=self._enable)

  def __repr__(self):
    return '{type}(enable={enable})'.format(
      type=type(self).__name__,
      enable=repr(self._enable))

Anki.Cozmo.SetAccessoryDiscovery = SetAccessoryDiscovery
del SetAccessoryDiscovery


class CubeID(object):
  "Generated message-passing message."

  __slots__ = (
    '_objectID',              # uint_32
    '_rotationPeriod_frames', # uint_8
  )

  @property
  def objectID(self):
    "uint_32 objectID struct property."
    return self._objectID

  @objectID.setter
  def objectID(self, value):
    self._objectID = msgbuffers.validate_integer(
      'CubeID.objectID', value, 0, 4294967295)

  @property
  def rotationPeriod_frames(self):
    "uint_8 rotationPeriod_frames struct property."
    return self._rotationPeriod_frames

  @rotationPeriod_frames.setter
  def rotationPeriod_frames(self, value):
    self._rotationPeriod_frames = msgbuffers.validate_integer(
      'CubeID.rotationPeriod_frames', value, 0, 255)

  def __init__(self, objectID=0, rotationPeriod_frames=0):
    self.objectID = objectID
    self.rotationPeriod_frames = rotationPeriod_frames

  @classmethod
  def unpack(cls, buffer):
    "Reads a new CubeID from the given buffer."
    reader = msgbuffers.BinaryReader(buffer)
    value = cls.unpack_from(reader)
    if reader.tell() != len(reader):
      raise msgbuffers.ReadError(
        ('CubeID.unpack received a buffer of length {length}, ' +
        'but only {position} bytes were read.').format(
        length=len(reader), position=reader.tell()))
    return value

  @classmethod
  def unpack_from(cls, reader):
    "Reads a new CubeID from the given BinaryReader."
    _objectID = reader.read('I')
    _rotationPeriod_frames = reader.read('B')
    return cls(_objectID, _rotationPeriod_frames)

  def pack(self):
    "Writes the current CubeID, returning bytes."
    writer = msgbuffers.BinaryWriter()
    self.pack_to(writer)
    return writer.dumps()

  def pack_to(self, writer):
    "Writes the current CubeID to the given BinaryWriter."
    writer.write(self._objectID, 'I')
    writer.write(self._rotationPeriod_frames, 'B')

  def __eq__(self, other):
    if type(self) is type(other):
      return (self._objectID == other._objectID and
        self._rotationPeriod_frames == other._rotationPeriod_frames)
    else:
      return NotImplemented

  def __ne__(self, other):
    if type(self) is type(other):
      return not self.__eq__(other)
    else:
      return NotImplemented

  def __len__(self):
    return (msgbuffers.size(self._objectID, 'I') +
      msgbuffers.size(self._rotationPeriod_frames, 'B'))

  def __str__(self):
    return '{type}(objectID={objectID}, rotationPeriod_frames={rotationPeriod_frames})'.format(
      type=type(self).__name__,
      objectID=self._objectID,
      rotationPeriod_frames=self._rotationPeriod_frames)

  def __repr__(self):
    return '{type}(objectID={objectID}, rotationPeriod_frames={rotationPeriod_frames})'.format(
      type=type(self).__name__,
      objectID=repr(self._objectID),
      rotationPeriod_frames=repr(self._rotationPeriod_frames))

Anki.Cozmo.CubeID = CubeID
del CubeID


class CubeLights(object):
  "Generated message-passing message."

  __slots__ = (
    '_lights', # LightState[4]
  )

  @property
  def lights(self):
    "LightState[4] lights struct property."
    return self._lights

  @lights.setter
  def lights(self, value):
    self._lights = msgbuffers.validate_farray(
      'CubeLights.lights', value, 4,
      lambda name, value_inner: msgbuffers.validate_object(
        name, value_inner, Anki.Cozmo.LightState))

  def __init__(self, lights=(Anki.Cozmo.LightState(),) * 4):
    self.lights = lights

  @classmethod
  def unpack(cls, buffer):
    "Reads a new CubeLights from the given buffer."
    reader = msgbuffers.BinaryReader(buffer)
    value = cls.unpack_from(reader)
    if reader.tell() != len(reader):
      raise msgbuffers.ReadError(
        ('CubeLights.unpack received a buffer of length {length}, ' +
        'but only {position} bytes were read.').format(
        length=len(reader), position=reader.tell()))
    return value

  @classmethod
  def unpack_from(cls, reader):
    "Reads a new CubeLights from the given BinaryReader."
    _lights = reader.read_object_farray(Anki.Cozmo.LightState.unpack_from, 4)
    return cls(_lights)

  def pack(self):
    "Writes the current CubeLights, returning bytes."
    writer = msgbuffers.BinaryWriter()
    self.pack_to(writer)
    return writer.dumps()

  def pack_to(self, writer):
    "Writes the current CubeLights to the given BinaryWriter."
    writer.write_object_farray(self._lights, 4)

  def __eq__(self, other):
    if type(self) is type(other):
      return self._lights == other._lights
    else:
      return NotImplemented

  def __ne__(self, other):
    if type(self) is type(other):
      return not self.__eq__(other)
    else:
      return NotImplemented

  def __len__(self):
    return (msgbuffers.size_object_farray(self._lights, 4))

  def __str__(self):
    return '{type}(lights={lights})'.format(
      type=type(self).__name__,
      lights=msgbuffers.shorten_sequence(self._lights))

  def __repr__(self):
    return '{type}(lights={lights})'.format(
      type=type(self).__name__,
      lights=repr(self._lights))

Anki.Cozmo.CubeLights = CubeLights
del CubeLights


class FlashObjectIDs(object):
  "Generated message-passing message."

  __slots__ = (
    '_objectID', # uint_32
  )

  @property
  def objectID(self):
    "uint_32 objectID struct property."
    return self._objectID

  @objectID.setter
  def objectID(self, value):
    self._objectID = msgbuffers.validate_integer(
      'FlashObjectIDs.objectID', value, 0, 4294967295)

  def __init__(self, objectID=0):
    self.objectID = objectID

  @classmethod
  def unpack(cls, buffer):
    "Reads a new FlashObjectIDs from the given buffer."
    reader = msgbuffers.BinaryReader(buffer)
    value = cls.unpack_from(reader)
    if reader.tell() != len(reader):
      raise msgbuffers.ReadError(
        ('FlashObjectIDs.unpack received a buffer of length {length}, ' +
        'but only {position} bytes were read.').format(
        length=len(reader), position=reader.tell()))
    return value

  @classmethod
  def unpack_from(cls, reader):
    "Reads a new FlashObjectIDs from the given BinaryReader."
    _objectID = reader.read('I')
    return cls(_objectID)

  def pack(self):
    "Writes the current FlashObjectIDs, returning bytes."
    writer = msgbuffers.BinaryWriter()
    self.pack_to(writer)
    return writer.dumps()

  def pack_to(self, writer):
    "Writes the current FlashObjectIDs to the given BinaryWriter."
    writer.write(self._objectID, 'I')

  def __eq__(self, other):
    if type(self) is type(other):
      return self._objectID == other._objectID
    else:
      return NotImplemented

  def __ne__(self, other):
    if type(self) is type(other):
      return not self.__eq__(other)
    else:
      return NotImplemented

  def __len__(self):
    return (msgbuffers.size(self._objectID, 'I'))

  def __str__(self):
    return '{type}(objectID={objectID})'.format(
      type=type(self).__name__,
      objectID=self._objectID)

  def __repr__(self):
    return '{type}(objectID={objectID})'.format(
      type=type(self).__name__,
      objectID=repr(self._objectID))

Anki.Cozmo.FlashObjectIDs = FlashObjectIDs
del FlashObjectIDs


class ObjectBeingCarried(object):
  "Generated message-passing message."

  __slots__ = (
    '_objectID',       # uint_32
    '_isBeingCarried', # bool
  )

  @property
  def objectID(self):
    "uint_32 objectID struct property."
    return self._objectID

  @objectID.setter
  def objectID(self, value):
    self._objectID = msgbuffers.validate_integer(
      'ObjectBeingCarried.objectID', value, 0, 4294967295)

  @property
  def isBeingCarried(self):
    "bool isBeingCarried struct property."
    return self._isBeingCarried

  @isBeingCarried.setter
  def isBeingCarried(self, value):
    self._isBeingCarried = msgbuffers.validate_bool(
      'ObjectBeingCarried.isBeingCarried', value)

  def __init__(self, objectID=0, isBeingCarried=False):
    self.objectID = objectID
    self.isBeingCarried = isBeingCarried

  @classmethod
  def unpack(cls, buffer):
    "Reads a new ObjectBeingCarried from the given buffer."
    reader = msgbuffers.BinaryReader(buffer)
    value = cls.unpack_from(reader)
    if reader.tell() != len(reader):
      raise msgbuffers.ReadError(
        ('ObjectBeingCarried.unpack received a buffer of length {length}, ' +
        'but only {position} bytes were read.').format(
        length=len(reader), position=reader.tell()))
    return value

  @classmethod
  def unpack_from(cls, reader):
    "Reads a new ObjectBeingCarried from the given BinaryReader."
    _objectID = reader.read('I')
    _isBeingCarried = bool(reader.read('b'))
    return cls(_objectID, _isBeingCarried)

  def pack(self):
    "Writes the current ObjectBeingCarried, returning bytes."
    writer = msgbuffers.BinaryWriter()
    self.pack_to(writer)
    return writer.dumps()

  def pack_to(self, writer):
    "Writes the current ObjectBeingCarried to the given BinaryWriter."
    writer.write(self._objectID, 'I')
    writer.write(int(self._isBeingCarried), 'b')

  def __eq__(self, other):
    if type(self) is type(other):
      return (self._objectID == other._objectID and
        self._isBeingCarried == other._isBeingCarried)
    else:
      return NotImplemented

  def __ne__(self, other):
    if type(self) is type(other):
      return not self.__eq__(other)
    else:
      return NotImplemented

  def __len__(self):
    return (msgbuffers.size(self._objectID, 'I') +
      msgbuffers.size(self._isBeingCarried, 'b'))

  def __str__(self):
    return '{type}(objectID={objectID}, isBeingCarried={isBeingCarried})'.format(
      type=type(self).__name__,
      objectID=self._objectID,
      isBeingCarried=self._isBeingCarried)

  def __repr__(self):
    return '{type}(objectID={objectID}, isBeingCarried={isBeingCarried})'.format(
      type=type(self).__name__,
      objectID=repr(self._objectID),
      isBeingCarried=repr(self._isBeingCarried))

Anki.Cozmo.ObjectBeingCarried = ObjectBeingCarried
del ObjectBeingCarried


class StreamObjectAccel(object):
  "Generated message-passing message."

  __slots__ = (
    '_objectID', # uint_32
    '_enable',   # bool
  )

  @property
  def objectID(self):
    "uint_32 objectID struct property."
    return self._objectID

  @objectID.setter
  def objectID(self, value):
    self._objectID = msgbuffers.validate_integer(
      'StreamObjectAccel.objectID', value, 0, 4294967295)

  @property
  def enable(self):
    "bool enable struct property."
    return self._enable

  @enable.setter
  def enable(self, value):
    self._enable = msgbuffers.validate_bool(
      'StreamObjectAccel.enable', value)

  def __init__(self, objectID=0, enable=False):
    self.objectID = objectID
    self.enable = enable

  @classmethod
  def unpack(cls, buffer):
    "Reads a new StreamObjectAccel from the given buffer."
    reader = msgbuffers.BinaryReader(buffer)
    value = cls.unpack_from(reader)
    if reader.tell() != len(reader):
      raise msgbuffers.ReadError(
        ('StreamObjectAccel.unpack received a buffer of length {length}, ' +
        'but only {position} bytes were read.').format(
        length=len(reader), position=reader.tell()))
    return value

  @classmethod
  def unpack_from(cls, reader):
    "Reads a new StreamObjectAccel from the given BinaryReader."
    _objectID = reader.read('I')
    _enable = bool(reader.read('b'))
    return cls(_objectID, _enable)

  def pack(self):
    "Writes the current StreamObjectAccel, returning bytes."
    writer = msgbuffers.BinaryWriter()
    self.pack_to(writer)
    return writer.dumps()

  def pack_to(self, writer):
    "Writes the current StreamObjectAccel to the given BinaryWriter."
    writer.write(self._objectID, 'I')
    writer.write(int(self._enable), 'b')

  def __eq__(self, other):
    if type(self) is type(other):
      return (self._objectID == other._objectID and
        self._enable == other._enable)
    else:
      return NotImplemented

  def __ne__(self, other):
    if type(self) is type(other):
      return not self.__eq__(other)
    else:
      return NotImplemented

  def __len__(self):
    return (msgbuffers.size(self._objectID, 'I') +
      msgbuffers.size(self._enable, 'b'))

  def __str__(self):
    return '{type}(objectID={objectID}, enable={enable})'.format(
      type=type(self).__name__,
      objectID=self._objectID,
      enable=self._enable)

  def __repr__(self):
    return '{type}(objectID={objectID}, enable={enable})'.format(
      type=type(self).__name__,
      objectID=repr(self._objectID),
      enable=repr(self._enable))

Anki.Cozmo.StreamObjectAccel = StreamObjectAccel
del StreamObjectAccel


class SetPropState(object):
  "Generated message-passing structure."

  __slots__ = (
    '_colors', # uint_16[4]
    '_slot',   # uint_8
  )

  @property
  def colors(self):
    "uint_16[4] colors struct property."
    return self._colors

  @colors.setter
  def colors(self, value):
    self._colors = msgbuffers.validate_farray(
      'SetPropState.colors', value, 4,
      lambda name, value_inner: msgbuffers.validate_integer(
        name, value_inner, 0, 65535))

  @property
  def slot(self):
    "uint_8 slot struct property."
    return self._slot

  @slot.setter
  def slot(self, value):
    self._slot = msgbuffers.validate_integer(
      'SetPropState.slot', value, 0, 255)

  def __init__(self, colors=(0,) * 4, slot=0):
    self.colors = colors
    self.slot = slot

  @classmethod
  def unpack(cls, buffer):
    "Reads a new SetPropState from the given buffer."
    reader = msgbuffers.BinaryReader(buffer)
    value = cls.unpack_from(reader)
    if reader.tell() != len(reader):
      raise msgbuffers.ReadError(
        ('SetPropState.unpack received a buffer of length {length}, ' +
        'but only {position} bytes were read.').format(
        length=len(reader), position=reader.tell()))
    return value

  @classmethod
  def unpack_from(cls, reader):
    "Reads a new SetPropState from the given BinaryReader."
    _colors = reader.read_farray('H', 4)
    _slot = reader.read('B')
    return cls(_colors, _slot)

  def pack(self):
    "Writes the current SetPropState, returning bytes."
    writer = msgbuffers.BinaryWriter()
    self.pack_to(writer)
    return writer.dumps()

  def pack_to(self, writer):
    "Writes the current SetPropState to the given BinaryWriter."
    writer.write_farray(self._colors, 'H', 4)
    writer.write(self._slot, 'B')

  def __eq__(self, other):
    if type(self) is type(other):
      return (self._colors == other._colors and
        self._slot == other._slot)
    else:
      return NotImplemented

  def __ne__(self, other):
    if type(self) is type(other):
      return not self.__eq__(other)
    else:
      return NotImplemented

  def __len__(self):
    return (msgbuffers.size_farray(self._colors, 'H', 4) +
      msgbuffers.size(self._slot, 'B'))

  def __str__(self):
    return '{type}(colors={colors}, slot={slot})'.format(
      type=type(self).__name__,
      colors=msgbuffers.shorten_sequence(self._colors),
      slot=self._slot)

  def __repr__(self):
    return '{type}(colors={colors}, slot={slot})'.format(
      type=type(self).__name__,
      colors=repr(self._colors),
      slot=repr(self._slot))

Anki.Cozmo.SetPropState = SetPropState
del SetPropState


class KillBodyCode(object):
  "Generated message-passing message."

  __slots__ = ()

  def __init__(self):
    pass

  @classmethod
  def unpack(cls, buffer):
    "Reads a new KillBodyCode from the given buffer."
    reader = msgbuffers.BinaryReader(buffer)
    value = cls.unpack_from(reader)
    if reader.tell() != len(reader):
      raise msgbuffers.ReadError(
        ('KillBodyCode.unpack received a buffer of length {length}, ' +
        'but only {position} bytes were read.').format(
        length=len(reader), position=reader.tell()))
    return value

  @classmethod
  def unpack_from(cls, reader):
    "Reads a new KillBodyCode from the given BinaryReader."
    return cls()

  def pack(self):
    "Writes the current KillBodyCode, returning bytes."
    writer = msgbuffers.BinaryWriter()
    self.pack_to(writer)
    return writer.dumps()

  def pack_to(self, writer):
    "Writes the current KillBodyCode to the given BinaryWriter."

  def __eq__(self, other):
    if type(self) is type(other):
      return True
    else:
      return NotImplemented

  def __ne__(self, other):
    if type(self) is type(other):
      return not self.__eq__(other)
    else:
      return NotImplemented

  def __len__(self):
    return 0

  def __str__(self):
    return '{type}()'.format(type=type(self).__name__)

  def __repr__(self):
    return '{type}()'.format(type=type(self).__name__)

Anki.Cozmo.KillBodyCode = KillBodyCode
del KillBodyCode

