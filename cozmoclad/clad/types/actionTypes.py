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
Source: clad/types/actionTypes.clad
Full command line: ../tools/message-buffers/emitters/Python_emitter.py -C ./src/ -I ../robot/clad/src/ ../coretech/vision/clad/src/ ../coretech/common/clad/src/ ../lib/util/source/anki/clad -o ../generated/cladPython// clad/types/actionTypes.clad
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
Anki.AudioMetaData = msgbuffers.Namespace()
Anki.AudioMetaData.GameEvent = msgbuffers.Namespace()
Anki.Cozmo = msgbuffers.Namespace()

from clad.audio.audioEventTypes import Anki as _Anki
Anki.update(_Anki.deep_clone())

from clad.types.toolCodes import Anki as _Anki
Anki.update(_Anki.deep_clone())

from clad.types.unexpectedMovementTypes import Anki as _Anki
Anki.update(_Anki.deep_clone())

class ActionConstants(object):
  "Automatically-generated uint_32 enumeration."
  INVALID_TAG             = 0
  FIRST_GAME_TAG          = 1
  LAST_GAME_TAG           = 1000000
  FIRST_GAME_INTERNAL_TAG = 1000001
  LAST_GAME_INTERNAL_TAG  = 2000000
  FIRST_SDK_TAG           = 2000001
  LAST_SDK_TAG            = 3000000
  FIRST_ENGINE_TAG        = 3000001
  LAST_ENGINE_TAG         = 4294967295

Anki.Cozmo.ActionConstants = ActionConstants

class RobotActionType(object):
  "Automatically-generated int_32 enumeration."
  COMPOUND                              = -2
  UNKNOWN                               = -1
  ALIGN_WITH_OBJECT                     = 0
  ASCEND_OR_DESCEND_RAMP                = 1
  CALIBRATE_MOTORS                      = 2
  CROSS_BRIDGE                          = 3
  DEVICE_AUDIO                          = 4
  DISPLAY_FACE_IMAGE                    = 5
  DISPLAY_PROCEDURAL_FACE               = 6
  DRIVE_OFF_CHARGER_CONTACTS            = 7
  DRIVE_STRAIGHT                        = 8
  DRIVE_TO_FLIP_BLOCK_POSE              = 9
  DRIVE_TO_OBJECT                       = 10
  DRIVE_PATH                            = 11
  DRIVE_TO_POSE                         = 12
  DRIVE_TO_PLACE_CARRIED_OBJECT         = 13
  FACE_PLANT                            = 14
  FLIP_BLOCK                            = 15
  HANG                                  = 16
  MOUNT_CHARGER                         = 17
  MOVE_HEAD_TO_ANGLE                    = 18
  MOVE_LIFT_TO_HEIGHT                   = 19
  PAN_AND_TILT                          = 20
  PICK_AND_PLACE_INCOMPLETE             = 21
  PICKUP_OBJECT_LOW                     = 22
  PICKUP_OBJECT_HIGH                    = 23
  PLACE_OBJECT_LOW                      = 24
  PLACE_OBJECT_HIGH                     = 25
  PLAY_ANIMATION                        = 26
  PLAY_ANIMATION_DRONE_MODE_CLIFF_EVENT = 27
  PLAY_CUBE_ANIMATION                   = 28
  POP_A_WHEELIE                         = 29
  READ_TOOL_CODE                        = 30
  ROLL_OBJECT_LOW                       = 31
  SAY_TEXT                              = 32
  SEARCH_FOR_NEARBY_OBJECT              = 33
  TRACK_OBJECT                          = 34
  TRACK_FACE                            = 35
  TRACK_GROUND_POINT                    = 36
  TRACK_MOTION                          = 37
  TRACK_PET_FACE                        = 38
  TRAVERSE_OBJECT                       = 39
  TURN_IN_PLACE                         = 40
  TURN_TOWARDS_FACE                     = 41
  TURN_TOWARDS_IMAGE_POINT              = 42
  TURN_TOWARDS_LAST_FACE_POSE           = 43
  TURN_TOWARDS_OBJECT                   = 44
  TURN_TOWARDS_POSE                     = 45
  VISUALLY_VERIFY_OBJECT                = 46
  VISUALLY_VERIFY_FACE                  = 47
  VISUALLY_VERIFY_NO_OBJECT_AT_POSE     = 48
  WAIT                                  = 49
  WAIT_FOR_IMAGES                       = 50
  WAIT_FOR_LAMBDA                       = 51

Anki.Cozmo.RobotActionType = RobotActionType
del RobotActionType


class AlignmentType(object):
  "Automatically-generated uint_8 enumeration."
  LIFT_FINGER = 0
  LIFT_PLATE  = 1
  BODY        = 2
  CUSTOM      = 3

Anki.Cozmo.AlignmentType = AlignmentType
del AlignmentType


class ObjectInteractionCompleted(object):
  "Generated message-passing structure."

  __slots__ = (
    '_objectIDs',              # int_32[5]
    '_numObjects',             # uint_8
    '_seeingUnexpectedObject', # bool
  )

  @property
  def objectIDs(self):
    "int_32[5] objectIDs struct property."
    return self._objectIDs

  @objectIDs.setter
  def objectIDs(self, value):
    self._objectIDs = msgbuffers.validate_farray(
      'ObjectInteractionCompleted.objectIDs', value, 5,
      lambda name, value_inner: msgbuffers.validate_integer(
        name, value_inner, -2147483648, 2147483647))

  @property
  def numObjects(self):
    "uint_8 numObjects struct property."
    return self._numObjects

  @numObjects.setter
  def numObjects(self, value):
    self._numObjects = msgbuffers.validate_integer(
      'ObjectInteractionCompleted.numObjects', value, 0, 255)

  @property
  def seeingUnexpectedObject(self):
    "bool seeingUnexpectedObject struct property."
    return self._seeingUnexpectedObject

  @seeingUnexpectedObject.setter
  def seeingUnexpectedObject(self, value):
    self._seeingUnexpectedObject = msgbuffers.validate_bool(
      'ObjectInteractionCompleted.seeingUnexpectedObject', value)

  def __init__(self, objectIDs=(0,) * 5, numObjects=0, seeingUnexpectedObject=False):
    self.objectIDs = objectIDs
    self.numObjects = numObjects
    self.seeingUnexpectedObject = seeingUnexpectedObject

  @classmethod
  def unpack(cls, buffer):
    "Reads a new ObjectInteractionCompleted from the given buffer."
    reader = msgbuffers.BinaryReader(buffer)
    value = cls.unpack_from(reader)
    if reader.tell() != len(reader):
      raise msgbuffers.ReadError(
        ('ObjectInteractionCompleted.unpack received a buffer of length {length}, ' +
        'but only {position} bytes were read.').format(
        length=len(reader), position=reader.tell()))
    return value

  @classmethod
  def unpack_from(cls, reader):
    "Reads a new ObjectInteractionCompleted from the given BinaryReader."
    _objectIDs = reader.read_farray('i', 5)
    _numObjects = reader.read('B')
    _seeingUnexpectedObject = bool(reader.read('b'))
    return cls(_objectIDs, _numObjects, _seeingUnexpectedObject)

  def pack(self):
    "Writes the current ObjectInteractionCompleted, returning bytes."
    writer = msgbuffers.BinaryWriter()
    self.pack_to(writer)
    return writer.dumps()

  def pack_to(self, writer):
    "Writes the current ObjectInteractionCompleted to the given BinaryWriter."
    writer.write_farray(self._objectIDs, 'i', 5)
    writer.write(self._numObjects, 'B')
    writer.write(int(self._seeingUnexpectedObject), 'b')

  def __eq__(self, other):
    if type(self) is type(other):
      return (self._objectIDs == other._objectIDs and
        self._numObjects == other._numObjects and
        self._seeingUnexpectedObject == other._seeingUnexpectedObject)
    else:
      return NotImplemented

  def __ne__(self, other):
    if type(self) is type(other):
      return not self.__eq__(other)
    else:
      return NotImplemented

  def __len__(self):
    return (msgbuffers.size_farray(self._objectIDs, 'i', 5) +
      msgbuffers.size(self._numObjects, 'B') +
      msgbuffers.size(self._seeingUnexpectedObject, 'b'))

  def __str__(self):
    return '{type}(objectIDs={objectIDs}, numObjects={numObjects}, seeingUnexpectedObject={seeingUnexpectedObject})'.format(
      type=type(self).__name__,
      objectIDs=msgbuffers.shorten_sequence(self._objectIDs),
      numObjects=self._numObjects,
      seeingUnexpectedObject=self._seeingUnexpectedObject)

  def __repr__(self):
    return '{type}(objectIDs={objectIDs}, numObjects={numObjects}, seeingUnexpectedObject={seeingUnexpectedObject})'.format(
      type=type(self).__name__,
      objectIDs=repr(self._objectIDs),
      numObjects=repr(self._numObjects),
      seeingUnexpectedObject=repr(self._seeingUnexpectedObject))

Anki.Cozmo.ObjectInteractionCompleted = ObjectInteractionCompleted
del ObjectInteractionCompleted


class AnimationCompleted(object):
  "Generated message-passing structure."

  __slots__ = (
    '_animationName', # string[uint_8]
  )

  @property
  def animationName(self):
    "string[uint_8] animationName struct property."
    return self._animationName

  @animationName.setter
  def animationName(self, value):
    self._animationName = msgbuffers.validate_string(
      'AnimationCompleted.animationName', value, 255)

  def __init__(self, animationName=''):
    self.animationName = animationName

  @classmethod
  def unpack(cls, buffer):
    "Reads a new AnimationCompleted from the given buffer."
    reader = msgbuffers.BinaryReader(buffer)
    value = cls.unpack_from(reader)
    if reader.tell() != len(reader):
      raise msgbuffers.ReadError(
        ('AnimationCompleted.unpack received a buffer of length {length}, ' +
        'but only {position} bytes were read.').format(
        length=len(reader), position=reader.tell()))
    return value

  @classmethod
  def unpack_from(cls, reader):
    "Reads a new AnimationCompleted from the given BinaryReader."
    _animationName = reader.read_string('B')
    return cls(_animationName)

  def pack(self):
    "Writes the current AnimationCompleted, returning bytes."
    writer = msgbuffers.BinaryWriter()
    self.pack_to(writer)
    return writer.dumps()

  def pack_to(self, writer):
    "Writes the current AnimationCompleted to the given BinaryWriter."
    writer.write_string(self._animationName, 'B')

  def __eq__(self, other):
    if type(self) is type(other):
      return self._animationName == other._animationName
    else:
      return NotImplemented

  def __ne__(self, other):
    if type(self) is type(other):
      return not self.__eq__(other)
    else:
      return NotImplemented

  def __len__(self):
    return (msgbuffers.size_string(self._animationName, 'B'))

  def __str__(self):
    return '{type}(animationName={animationName})'.format(
      type=type(self).__name__,
      animationName=msgbuffers.shorten_string(self._animationName))

  def __repr__(self):
    return '{type}(animationName={animationName})'.format(
      type=type(self).__name__,
      animationName=repr(self._animationName))

Anki.Cozmo.AnimationCompleted = AnimationCompleted
del AnimationCompleted


class DeviceAudioCompleted(object):
  "Generated message-passing structure."

  __slots__ = (
    '_audioEvent', # Anki.AudioMetaData.GameEvent.GenericEvent
  )

  @property
  def audioEvent(self):
    "Anki.AudioMetaData.GameEvent.GenericEvent audioEvent struct property."
    return self._audioEvent

  @audioEvent.setter
  def audioEvent(self, value):
    self._audioEvent = msgbuffers.validate_integer(
      'DeviceAudioCompleted.audioEvent', value, 0, 4294967295)

  def __init__(self, audioEvent=Anki.AudioMetaData.GameEvent.GenericEvent.Invalid):
    self.audioEvent = audioEvent

  @classmethod
  def unpack(cls, buffer):
    "Reads a new DeviceAudioCompleted from the given buffer."
    reader = msgbuffers.BinaryReader(buffer)
    value = cls.unpack_from(reader)
    if reader.tell() != len(reader):
      raise msgbuffers.ReadError(
        ('DeviceAudioCompleted.unpack received a buffer of length {length}, ' +
        'but only {position} bytes were read.').format(
        length=len(reader), position=reader.tell()))
    return value

  @classmethod
  def unpack_from(cls, reader):
    "Reads a new DeviceAudioCompleted from the given BinaryReader."
    _audioEvent = reader.read('I')
    return cls(_audioEvent)

  def pack(self):
    "Writes the current DeviceAudioCompleted, returning bytes."
    writer = msgbuffers.BinaryWriter()
    self.pack_to(writer)
    return writer.dumps()

  def pack_to(self, writer):
    "Writes the current DeviceAudioCompleted to the given BinaryWriter."
    writer.write(self._audioEvent, 'I')

  def __eq__(self, other):
    if type(self) is type(other):
      return self._audioEvent == other._audioEvent
    else:
      return NotImplemented

  def __ne__(self, other):
    if type(self) is type(other):
      return not self.__eq__(other)
    else:
      return NotImplemented

  def __len__(self):
    return (msgbuffers.size(self._audioEvent, 'I'))

  def __str__(self):
    return '{type}(audioEvent={audioEvent})'.format(
      type=type(self).__name__,
      audioEvent=self._audioEvent)

  def __repr__(self):
    return '{type}(audioEvent={audioEvent})'.format(
      type=type(self).__name__,
      audioEvent=repr(self._audioEvent))

Anki.Cozmo.DeviceAudioCompleted = DeviceAudioCompleted
del DeviceAudioCompleted


class TrackFaceCompleted(object):
  "Generated message-passing structure."

  __slots__ = (
    '_faceID', # int_32
  )

  @property
  def faceID(self):
    "int_32 faceID struct property."
    return self._faceID

  @faceID.setter
  def faceID(self, value):
    self._faceID = msgbuffers.validate_integer(
      'TrackFaceCompleted.faceID', value, -2147483648, 2147483647)

  def __init__(self, faceID=0):
    self.faceID = faceID

  @classmethod
  def unpack(cls, buffer):
    "Reads a new TrackFaceCompleted from the given buffer."
    reader = msgbuffers.BinaryReader(buffer)
    value = cls.unpack_from(reader)
    if reader.tell() != len(reader):
      raise msgbuffers.ReadError(
        ('TrackFaceCompleted.unpack received a buffer of length {length}, ' +
        'but only {position} bytes were read.').format(
        length=len(reader), position=reader.tell()))
    return value

  @classmethod
  def unpack_from(cls, reader):
    "Reads a new TrackFaceCompleted from the given BinaryReader."
    _faceID = reader.read('i')
    return cls(_faceID)

  def pack(self):
    "Writes the current TrackFaceCompleted, returning bytes."
    writer = msgbuffers.BinaryWriter()
    self.pack_to(writer)
    return writer.dumps()

  def pack_to(self, writer):
    "Writes the current TrackFaceCompleted to the given BinaryWriter."
    writer.write(self._faceID, 'i')

  def __eq__(self, other):
    if type(self) is type(other):
      return self._faceID == other._faceID
    else:
      return NotImplemented

  def __ne__(self, other):
    if type(self) is type(other):
      return not self.__eq__(other)
    else:
      return NotImplemented

  def __len__(self):
    return (msgbuffers.size(self._faceID, 'i'))

  def __str__(self):
    return '{type}(faceID={faceID})'.format(
      type=type(self).__name__,
      faceID=self._faceID)

  def __repr__(self):
    return '{type}(faceID={faceID})'.format(
      type=type(self).__name__,
      faceID=repr(self._faceID))

Anki.Cozmo.TrackFaceCompleted = TrackFaceCompleted
del TrackFaceCompleted


class ReadToolCodeCompleted(object):
  "Generated message-passing structure."

  __slots__ = (
    '_info', # Anki.Cozmo.ToolCodeInfo
  )

  @property
  def info(self):
    "Anki.Cozmo.ToolCodeInfo info struct property."
    return self._info

  @info.setter
  def info(self, value):
    self._info = msgbuffers.validate_object(
      'ReadToolCodeCompleted.info', value, Anki.Cozmo.ToolCodeInfo)

  def __init__(self, info=Anki.Cozmo.ToolCodeInfo()):
    self.info = info

  @classmethod
  def unpack(cls, buffer):
    "Reads a new ReadToolCodeCompleted from the given buffer."
    reader = msgbuffers.BinaryReader(buffer)
    value = cls.unpack_from(reader)
    if reader.tell() != len(reader):
      raise msgbuffers.ReadError(
        ('ReadToolCodeCompleted.unpack received a buffer of length {length}, ' +
        'but only {position} bytes were read.').format(
        length=len(reader), position=reader.tell()))
    return value

  @classmethod
  def unpack_from(cls, reader):
    "Reads a new ReadToolCodeCompleted from the given BinaryReader."
    _info = reader.read_object(Anki.Cozmo.ToolCodeInfo.unpack_from)
    return cls(_info)

  def pack(self):
    "Writes the current ReadToolCodeCompleted, returning bytes."
    writer = msgbuffers.BinaryWriter()
    self.pack_to(writer)
    return writer.dumps()

  def pack_to(self, writer):
    "Writes the current ReadToolCodeCompleted to the given BinaryWriter."
    writer.write_object(self._info)

  def __eq__(self, other):
    if type(self) is type(other):
      return self._info == other._info
    else:
      return NotImplemented

  def __ne__(self, other):
    if type(self) is type(other):
      return not self.__eq__(other)
    else:
      return NotImplemented

  def __len__(self):
    return (msgbuffers.size_object(self._info))

  def __str__(self):
    return '{type}(info={info})'.format(
      type=type(self).__name__,
      info=self._info)

  def __repr__(self):
    return '{type}(info={info})'.format(
      type=type(self).__name__,
      info=repr(self._info))

Anki.Cozmo.ReadToolCodeCompleted = ReadToolCodeCompleted
del ReadToolCodeCompleted


class TurnInPlaceCompleted(object):
  "Generated message-passing structure."

  __slots__ = (
    '_relocalizedCnt', # uint_32
  )

  @property
  def relocalizedCnt(self):
    "uint_32 relocalizedCnt struct property."
    return self._relocalizedCnt

  @relocalizedCnt.setter
  def relocalizedCnt(self, value):
    self._relocalizedCnt = msgbuffers.validate_integer(
      'TurnInPlaceCompleted.relocalizedCnt', value, 0, 4294967295)

  def __init__(self, relocalizedCnt=0):
    self.relocalizedCnt = relocalizedCnt

  @classmethod
  def unpack(cls, buffer):
    "Reads a new TurnInPlaceCompleted from the given buffer."
    reader = msgbuffers.BinaryReader(buffer)
    value = cls.unpack_from(reader)
    if reader.tell() != len(reader):
      raise msgbuffers.ReadError(
        ('TurnInPlaceCompleted.unpack received a buffer of length {length}, ' +
        'but only {position} bytes were read.').format(
        length=len(reader), position=reader.tell()))
    return value

  @classmethod
  def unpack_from(cls, reader):
    "Reads a new TurnInPlaceCompleted from the given BinaryReader."
    _relocalizedCnt = reader.read('I')
    return cls(_relocalizedCnt)

  def pack(self):
    "Writes the current TurnInPlaceCompleted, returning bytes."
    writer = msgbuffers.BinaryWriter()
    self.pack_to(writer)
    return writer.dumps()

  def pack_to(self, writer):
    "Writes the current TurnInPlaceCompleted to the given BinaryWriter."
    writer.write(self._relocalizedCnt, 'I')

  def __eq__(self, other):
    if type(self) is type(other):
      return self._relocalizedCnt == other._relocalizedCnt
    else:
      return NotImplemented

  def __ne__(self, other):
    if type(self) is type(other):
      return not self.__eq__(other)
    else:
      return NotImplemented

  def __len__(self):
    return (msgbuffers.size(self._relocalizedCnt, 'I'))

  def __str__(self):
    return '{type}(relocalizedCnt={relocalizedCnt})'.format(
      type=type(self).__name__,
      relocalizedCnt=self._relocalizedCnt)

  def __repr__(self):
    return '{type}(relocalizedCnt={relocalizedCnt})'.format(
      type=type(self).__name__,
      relocalizedCnt=repr(self._relocalizedCnt))

Anki.Cozmo.TurnInPlaceCompleted = TurnInPlaceCompleted
del TurnInPlaceCompleted


class DefaultCompleted(object):
  "Generated message-passing structure."

  __slots__ = ()

  def __init__(self):
    pass

  @classmethod
  def unpack(cls, buffer):
    "Reads a new DefaultCompleted from the given buffer."
    reader = msgbuffers.BinaryReader(buffer)
    value = cls.unpack_from(reader)
    if reader.tell() != len(reader):
      raise msgbuffers.ReadError(
        ('DefaultCompleted.unpack received a buffer of length {length}, ' +
        'but only {position} bytes were read.').format(
        length=len(reader), position=reader.tell()))
    return value

  @classmethod
  def unpack_from(cls, reader):
    "Reads a new DefaultCompleted from the given BinaryReader."
    return cls()

  def pack(self):
    "Writes the current DefaultCompleted, returning bytes."
    writer = msgbuffers.BinaryWriter()
    self.pack_to(writer)
    return writer.dumps()

  def pack_to(self, writer):
    "Writes the current DefaultCompleted to the given BinaryWriter."

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

Anki.Cozmo.DefaultCompleted = DefaultCompleted
del DefaultCompleted


class ActionCompletedUnion(object):
  "Generated message-passing union."

  __slots__ = ('_tag', '_data')

  class Tag(object):
    "The type indicator for this union."
    objectInteractionCompleted = 0 # Anki.Cozmo.ObjectInteractionCompleted
    animationCompleted         = 1 # Anki.Cozmo.AnimationCompleted
    deviceAudioCompleted       = 2 # Anki.Cozmo.DeviceAudioCompleted
    trackFaceCompleted         = 3 # Anki.Cozmo.TrackFaceCompleted
    readToolCodeCompleted      = 4 # Anki.Cozmo.ReadToolCodeCompleted
    turnInPlaceCompleted       = 5 # Anki.Cozmo.TurnInPlaceCompleted
    defaultCompleted           = 6 # Anki.Cozmo.DefaultCompleted

  @property
  def tag(self):
    "The current tag for this union."
    return self._tag

  @property
  def tag_name(self):
    "The name of the current tag for this union."
    if self._tag in self._tags_by_value:
      return self._tags_by_value[self._tag]
    else:
      return None

  @property
  def data(self):
    "The data held by this union. None if no data is set."
    return self._data

  @property
  def objectInteractionCompleted(self):
    "Anki.Cozmo.ObjectInteractionCompleted objectInteractionCompleted union property."
    msgbuffers.safety_check_tag('objectInteractionCompleted', self._tag, self.Tag.objectInteractionCompleted, self._tags_by_value)
    return self._data

  @objectInteractionCompleted.setter
  def objectInteractionCompleted(self, value):
    self._data = msgbuffers.validate_object(
      'ActionCompletedUnion.objectInteractionCompleted', value, Anki.Cozmo.ObjectInteractionCompleted)
    self._tag = self.Tag.objectInteractionCompleted

  @property
  def animationCompleted(self):
    "Anki.Cozmo.AnimationCompleted animationCompleted union property."
    msgbuffers.safety_check_tag('animationCompleted', self._tag, self.Tag.animationCompleted, self._tags_by_value)
    return self._data

  @animationCompleted.setter
  def animationCompleted(self, value):
    self._data = msgbuffers.validate_object(
      'ActionCompletedUnion.animationCompleted', value, Anki.Cozmo.AnimationCompleted)
    self._tag = self.Tag.animationCompleted

  @property
  def deviceAudioCompleted(self):
    "Anki.Cozmo.DeviceAudioCompleted deviceAudioCompleted union property."
    msgbuffers.safety_check_tag('deviceAudioCompleted', self._tag, self.Tag.deviceAudioCompleted, self._tags_by_value)
    return self._data

  @deviceAudioCompleted.setter
  def deviceAudioCompleted(self, value):
    self._data = msgbuffers.validate_object(
      'ActionCompletedUnion.deviceAudioCompleted', value, Anki.Cozmo.DeviceAudioCompleted)
    self._tag = self.Tag.deviceAudioCompleted

  @property
  def trackFaceCompleted(self):
    "Anki.Cozmo.TrackFaceCompleted trackFaceCompleted union property."
    msgbuffers.safety_check_tag('trackFaceCompleted', self._tag, self.Tag.trackFaceCompleted, self._tags_by_value)
    return self._data

  @trackFaceCompleted.setter
  def trackFaceCompleted(self, value):
    self._data = msgbuffers.validate_object(
      'ActionCompletedUnion.trackFaceCompleted', value, Anki.Cozmo.TrackFaceCompleted)
    self._tag = self.Tag.trackFaceCompleted

  @property
  def readToolCodeCompleted(self):
    "Anki.Cozmo.ReadToolCodeCompleted readToolCodeCompleted union property."
    msgbuffers.safety_check_tag('readToolCodeCompleted', self._tag, self.Tag.readToolCodeCompleted, self._tags_by_value)
    return self._data

  @readToolCodeCompleted.setter
  def readToolCodeCompleted(self, value):
    self._data = msgbuffers.validate_object(
      'ActionCompletedUnion.readToolCodeCompleted', value, Anki.Cozmo.ReadToolCodeCompleted)
    self._tag = self.Tag.readToolCodeCompleted

  @property
  def turnInPlaceCompleted(self):
    "Anki.Cozmo.TurnInPlaceCompleted turnInPlaceCompleted union property."
    msgbuffers.safety_check_tag('turnInPlaceCompleted', self._tag, self.Tag.turnInPlaceCompleted, self._tags_by_value)
    return self._data

  @turnInPlaceCompleted.setter
  def turnInPlaceCompleted(self, value):
    self._data = msgbuffers.validate_object(
      'ActionCompletedUnion.turnInPlaceCompleted', value, Anki.Cozmo.TurnInPlaceCompleted)
    self._tag = self.Tag.turnInPlaceCompleted

  @property
  def defaultCompleted(self):
    "Anki.Cozmo.DefaultCompleted defaultCompleted union property."
    msgbuffers.safety_check_tag('defaultCompleted', self._tag, self.Tag.defaultCompleted, self._tags_by_value)
    return self._data

  @defaultCompleted.setter
  def defaultCompleted(self, value):
    self._data = msgbuffers.validate_object(
      'ActionCompletedUnion.defaultCompleted', value, Anki.Cozmo.DefaultCompleted)
    self._tag = self.Tag.defaultCompleted

  def __init__(self, **kwargs):
    if not kwargs:
      self._tag = None
      self._data = None

    elif len(kwargs) == 1:
      key, value = next(iter(kwargs.items()))
      if key not in self._tags_by_name:
        raise TypeError("'{argument}' is an invalid keyword argument for this method.".format(argument=key))
      # calls the correct property
      setattr(self, key, value)

    else:
      raise TypeError('This method only accepts up to one keyword argument.')

  @classmethod
  def unpack(cls, buffer):
    "Reads a new ActionCompletedUnion from the given buffer."
    reader = msgbuffers.BinaryReader(buffer)
    value = cls.unpack_from(reader)
    if reader.tell() != len(reader):
      raise msgbuffers.ReadError(
        ('ActionCompletedUnion.unpack received a buffer of length {length}, ' +
        'but only {position} bytes were read.').format(
        length=len(reader), position=reader.tell()))
    return value

  @classmethod
  def unpack_from(cls, reader):
    "Reads a new ActionCompletedUnion from the given BinaryReader."
    tag = reader.read('B')
    if tag in cls._tags_by_value:
      value = cls()
      setattr(value, cls._tags_by_value[tag], cls._tag_unpack_methods[tag](reader))
      return value
    else:
      raise ValueError('ActionCompletedUnion attempted to unpack unknown tag {tag}.'.format(tag=tag))

  def pack(self):
    "Writes the current ActionCompletedUnion, returning bytes."
    writer = msgbuffers.BinaryWriter()
    self.pack_to(writer)
    return writer.dumps()

  def pack_to(self, writer):
    "Writes the current SampleUnion to the given BinaryWriter."
    if self._tag in self._tags_by_value:
      writer.write(self._tag, 'B')
      self._tag_pack_methods[self._tag](writer, self._data)
    else:
      raise ValueError('Cannot pack an empty ActionCompletedUnion.')

  def clear(self):
    self._tag = None
    self._data = None

  @classmethod
  def typeByTag(cls, tag):
    return cls._type_by_tag_value[tag]()

  def __eq__(self, other):
    if type(self) is type(other):
      return self._tag == other._tag and self._data == other._data
    else:
      return NotImplemented

  def __ne__(self, other):
    if type(self) is type(other):
      return not self.__eq__(other)
    else:
      return NotImplemented

  def __len__(self):
    if 0 <= self._tag < 7:
      return self._tag_size_methods[self._tag](self._data)
    else:
      return 1

  def __str__(self):
    if 0 <= self._tag < 7:
      return '{type}({name}={value})'.format(
        type=type(self).__name__,
        name=self.tag_name,
        value=self._data)
    else:
      return '{type}()'.format(
        type=type(self).__name__)

  def __repr__(self):
    if 0 <= self._tag < 7:
      return '{type}({name}={value})'.format(
        type=type(self).__name__,
        name=self.tag_name,
        value=repr(self._data))
    else:
      return '{type}()'.format(
        type=type(self).__name__)

  _tags_by_name = dict(
    objectInteractionCompleted=0,
    animationCompleted=1,
    deviceAudioCompleted=2,
    trackFaceCompleted=3,
    readToolCodeCompleted=4,
    turnInPlaceCompleted=5,
    defaultCompleted=6,
  )

  _tags_by_value = dict()
  _tags_by_value[0] = 'objectInteractionCompleted'
  _tags_by_value[1] = 'animationCompleted'
  _tags_by_value[2] = 'deviceAudioCompleted'
  _tags_by_value[3] = 'trackFaceCompleted'
  _tags_by_value[4] = 'readToolCodeCompleted'
  _tags_by_value[5] = 'turnInPlaceCompleted'
  _tags_by_value[6] = 'defaultCompleted'
  

  _tag_unpack_methods = dict()
  _tag_unpack_methods[0] = lambda reader: reader.read_object(Anki.Cozmo.ObjectInteractionCompleted.unpack_from)
  _tag_unpack_methods[1] = lambda reader: reader.read_object(Anki.Cozmo.AnimationCompleted.unpack_from)
  _tag_unpack_methods[2] = lambda reader: reader.read_object(Anki.Cozmo.DeviceAudioCompleted.unpack_from)
  _tag_unpack_methods[3] = lambda reader: reader.read_object(Anki.Cozmo.TrackFaceCompleted.unpack_from)
  _tag_unpack_methods[4] = lambda reader: reader.read_object(Anki.Cozmo.ReadToolCodeCompleted.unpack_from)
  _tag_unpack_methods[5] = lambda reader: reader.read_object(Anki.Cozmo.TurnInPlaceCompleted.unpack_from)
  _tag_unpack_methods[6] = lambda reader: reader.read_object(Anki.Cozmo.DefaultCompleted.unpack_from)
  

  _tag_pack_methods = dict()
  _tag_pack_methods[0] = lambda writer, value: writer.write_object(value)
  _tag_pack_methods[1] = lambda writer, value: writer.write_object(value)
  _tag_pack_methods[2] = lambda writer, value: writer.write_object(value)
  _tag_pack_methods[3] = lambda writer, value: writer.write_object(value)
  _tag_pack_methods[4] = lambda writer, value: writer.write_object(value)
  _tag_pack_methods[5] = lambda writer, value: writer.write_object(value)
  _tag_pack_methods[6] = lambda writer, value: writer.write_object(value)
  

  _tag_size_methods = dict()
  _tag_size_methods[0] = lambda value: msgbuffers.size_object(value)
  _tag_size_methods[1] = lambda value: msgbuffers.size_object(value)
  _tag_size_methods[2] = lambda value: msgbuffers.size_object(value)
  _tag_size_methods[3] = lambda value: msgbuffers.size_object(value)
  _tag_size_methods[4] = lambda value: msgbuffers.size_object(value)
  _tag_size_methods[5] = lambda value: msgbuffers.size_object(value)
  _tag_size_methods[6] = lambda value: msgbuffers.size_object(value)
  

  _type_by_tag_value = dict()
  _type_by_tag_value[0] = lambda : Anki.Cozmo.ObjectInteractionCompleted
  _type_by_tag_value[1] = lambda : Anki.Cozmo.AnimationCompleted
  _type_by_tag_value[2] = lambda : Anki.Cozmo.DeviceAudioCompleted
  _type_by_tag_value[3] = lambda : Anki.Cozmo.TrackFaceCompleted
  _type_by_tag_value[4] = lambda : Anki.Cozmo.ReadToolCodeCompleted
  _type_by_tag_value[5] = lambda : Anki.Cozmo.TurnInPlaceCompleted
  _type_by_tag_value[6] = lambda : Anki.Cozmo.DefaultCompleted
  

Anki.Cozmo.ActionCompletedUnion = ActionCompletedUnion
del ActionCompletedUnion


class QueueActionPosition(object):
  "Automatically-generated uint_8 enumeration."
  NOW                     = 0
  NOW_AND_CLEAR_REMAINING = 1
  NOW_AND_RESUME          = 2
  NEXT                    = 3
  AT_END                  = 4
  IN_PARALLEL             = 5

Anki.Cozmo.QueueActionPosition = QueueActionPosition
del QueueActionPosition

