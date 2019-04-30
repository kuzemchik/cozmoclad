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
Source: clad/types/factoryTestTypes.clad
Full command line: ../tools/message-buffers/emitters/Python_emitter.py -C ./src/ -I ../robot/clad/src/ ../coretech/vision/clad/src/ ../coretech/common/clad/src/ ../lib/util/source/anki/clad -o ../generated/cladPython// clad/types/factoryTestTypes.clad
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

from clad.types.birthCertificate import Anki as _Anki
Anki.update(_Anki.deep_clone())

class FactoryTestState(object):
  "Automatically-generated uint_8 enumeration."
  GetPrevTestResults         = 0
  InitRobot                  = 1
  WaitingForMotorCalibration = 2
  ChargerAndIMUCheck         = 3
  DriveToSlot                = 4
  GotoCalibrationPose        = 5
  TakeCalibrationImages      = 6
  ComputeCameraCalibration   = 7
  WaitForCameraCalibration   = 8
  ReadLiftToolCode           = 9
  GotoPickupPose             = 10
  StartPickup                = 11
  PickingUpBlock             = 12
  PlacingBlock               = 13
  BackAndForth               = 14
  WaitingForWritesToRobot    = 15

Anki.Cozmo.FactoryTestState = FactoryTestState
del FactoryTestState


class FactoryTestResultCode(object):
  "Automatically-generated uint_8 enumeration."
  UNKNOWN                                   = 0
  SUCCESS                                   = 1
  MISMATCHED_CLAD                           = 2
  INIT_LIFT_OR_HEAD_FAILED                  = 3
  CHARGER_UNDETECTED                        = 4
  CHARGER_UNAVAILABLE                       = 5
  CHARGER_UNCONNECTED                       = 6
  IMU_DRIFTING                              = 7
  STILL_ON_CHARGER                          = 8
  GOTO_CALIB_POSE_ACTION_FAILED             = 9
  CLIFF_UNDETECTED                          = 10
  CLIFF_UNEXPECTED                          = 11
  NOT_IN_CALIBRATION_POSE                   = 12
  CALIBRATION_TIMED_OUT                     = 13
  CALIBRATION_VALUES_OOR                    = 14
  CAMERA_CALIB_WRITE_FAILED                 = 15
  CALIB_IMAGES_WRITE_FAILED                 = 16
  CALIB_POSE_WRITE_FAILED                   = 17
  TOO_MANY_CALIB_IMAGES                     = 18
  CALIB_POSE_GET_FAILED                     = 19
  READ_TOOL_CODE_FAILED                     = 20
  TOOL_CODE_POSITIONS_OOR                   = 21
  TOOL_CODE_WRITE_FAILED                    = 22
  GOTO_PRE_PICKUP_POSE_ACTION_FAILED        = 23
  NOT_IN_PRE_PICKUP_POSE                    = 24
  CUBE_NOT_FOUND                            = 25
  CUBE_NOT_WHERE_EXPECTED                   = 26
  PICKUP_FAILED                             = 27
  PLACEMENT_FAILED                          = 28
  UNEXPECTED_OBSERVED_OBJECT                = 29
  GOTO_PRE_MOUNT_CHARGER_POSE_ACTION_FAILED = 30
  CHARGER_NOT_FOUND                         = 31
  CHARGER_DOCK_FAILED                       = 32
  QUEUE_ACTION_FAILED                       = 33
  MOTOR_CALIB_UNEXPECTED                    = 34
  TEST_RESULT_WRITE_FAILED                  = 35
  TEST_TIMED_OUT                            = 36
  TEST_CANCELLED                            = 37
  ROBOT_PICKUP                              = 38
  TOOL_CODE_IMAGES_WRITE_FAILED             = 39
  FIRST_CALIB_IMAGE_NOT_TAKEN               = 40
  CUBE_POSE_WRITE_FAILED                    = 41
  LIFT_MOTOR_CALIB_UNEXPECTED               = 42
  HEAD_MOTOR_CALIB_UNEXPECTED               = 43
  WIPED_ALL                                 = 44
  ROBOT_FAILED_PREPLAYPEN_TESTS             = 45
  ROBOT_NOT_TESTED                          = 46
  MOTORS_UNCALIBRATED                       = 47
  BIRTH_CERTIFICATE_WRITE_FAILED            = 48
  NVSTORAGE_WRITE_FAILED                    = 49
  NVSTORAGE_SEND_FAILED                     = 50
  TOO_MANY_TOOL_CODE_IMAGES                 = 51
  CALIB_META_INFO_WRITE_FAILED              = 52
  IMU_INFO_WRITE_FAILED                     = 53
  NO_ACTIVE_OBJECTS_DISCOVERED              = 54
  NO_PREPLAYPEN_CENTROIDS                   = 55
  COMPUTE_CAM_POSE_FAILED                   = 56
  CAM_POSE_OOR                              = 57
  PLAY_SOUND_FAILED                         = 58
  PREV_TEST_RESULTS_READ_FAILED             = 59
  WRONG_FIRMWARE_VERSION                    = 60
  CLIFF_VALUE_TOO_HIGH                      = 61
  CLIFF_VALUE_TOO_LOW                       = 62
  BACKUP_NOT_STRAIGHT                       = 63
  BATTERY_TOO_LOW                           = 64
  NO_IMU_DATA                               = 65
  BACK_AND_FORTH_NOT_STRAIGHT               = 66
  WRONG_BODY_HW_VERSION                     = 67
  NO_BODY_VERSION_MESSAGE                   = 68
  NVSTORAGE_ERASE_FAILED                    = 69
  PARSE_HEADER_FAILED                       = 70
  ONE_POINT_ZERO_FIRMWARE                   = 71

Anki.Cozmo.FactoryTestResultCode = FactoryTestResultCode
del FactoryTestResultCode


class FactoryTestResultEntry(object):
  "Generated message-passing message."

  __slots__ = (
    '_utcTime',    # uint_64
    '_engineSHA1', # uint_32
    '_timestamps', # uint_32[18]
    '_stationID',  # int_32
    '_result',     # Anki.Cozmo.FactoryTestResultCode
  )

  @property
  def utcTime(self):
    "uint_64 utcTime struct property."
    return self._utcTime

  @utcTime.setter
  def utcTime(self, value):
    self._utcTime = msgbuffers.validate_integer(
      'FactoryTestResultEntry.utcTime', value, 0, 18446744073709551615)

  @property
  def engineSHA1(self):
    "uint_32 engineSHA1 struct property."
    return self._engineSHA1

  @engineSHA1.setter
  def engineSHA1(self, value):
    self._engineSHA1 = msgbuffers.validate_integer(
      'FactoryTestResultEntry.engineSHA1', value, 0, 4294967295)

  @property
  def timestamps(self):
    "uint_32[18] timestamps struct property."
    return self._timestamps

  @timestamps.setter
  def timestamps(self, value):
    self._timestamps = msgbuffers.validate_farray(
      'FactoryTestResultEntry.timestamps', value, 18,
      lambda name, value_inner: msgbuffers.validate_integer(
        name, value_inner, 0, 4294967295))

  @property
  def stationID(self):
    "int_32 stationID struct property."
    return self._stationID

  @stationID.setter
  def stationID(self, value):
    self._stationID = msgbuffers.validate_integer(
      'FactoryTestResultEntry.stationID', value, -2147483648, 2147483647)

  @property
  def result(self):
    "Anki.Cozmo.FactoryTestResultCode result struct property."
    return self._result

  @result.setter
  def result(self, value):
    self._result = msgbuffers.validate_integer(
      'FactoryTestResultEntry.result', value, 0, 255)

  def __init__(self, utcTime=0, engineSHA1=0, timestamps=(0,) * 18, stationID=0, result=Anki.Cozmo.FactoryTestResultCode.UNKNOWN):
    self.utcTime = utcTime
    self.engineSHA1 = engineSHA1
    self.timestamps = timestamps
    self.stationID = stationID
    self.result = result

  @classmethod
  def unpack(cls, buffer):
    "Reads a new FactoryTestResultEntry from the given buffer."
    reader = msgbuffers.BinaryReader(buffer)
    value = cls.unpack_from(reader)
    if reader.tell() != len(reader):
      raise msgbuffers.ReadError(
        ('FactoryTestResultEntry.unpack received a buffer of length {length}, ' +
        'but only {position} bytes were read.').format(
        length=len(reader), position=reader.tell()))
    return value

  @classmethod
  def unpack_from(cls, reader):
    "Reads a new FactoryTestResultEntry from the given BinaryReader."
    _utcTime = reader.read('Q')
    _engineSHA1 = reader.read('I')
    _timestamps = reader.read_farray('I', 18)
    _stationID = reader.read('i')
    _result = reader.read('B')
    return cls(_utcTime, _engineSHA1, _timestamps, _stationID, _result)

  def pack(self):
    "Writes the current FactoryTestResultEntry, returning bytes."
    writer = msgbuffers.BinaryWriter()
    self.pack_to(writer)
    return writer.dumps()

  def pack_to(self, writer):
    "Writes the current FactoryTestResultEntry to the given BinaryWriter."
    writer.write(self._utcTime, 'Q')
    writer.write(self._engineSHA1, 'I')
    writer.write_farray(self._timestamps, 'I', 18)
    writer.write(self._stationID, 'i')
    writer.write(self._result, 'B')

  def __eq__(self, other):
    if type(self) is type(other):
      return (self._utcTime == other._utcTime and
        self._engineSHA1 == other._engineSHA1 and
        self._timestamps == other._timestamps and
        self._stationID == other._stationID and
        self._result == other._result)
    else:
      return NotImplemented

  def __ne__(self, other):
    if type(self) is type(other):
      return not self.__eq__(other)
    else:
      return NotImplemented

  def __len__(self):
    return (msgbuffers.size(self._utcTime, 'Q') +
      msgbuffers.size(self._engineSHA1, 'I') +
      msgbuffers.size_farray(self._timestamps, 'I', 18) +
      msgbuffers.size(self._stationID, 'i') +
      msgbuffers.size(self._result, 'B'))

  def __str__(self):
    return '{type}(utcTime={utcTime}, engineSHA1={engineSHA1}, timestamps={timestamps}, stationID={stationID}, result={result})'.format(
      type=type(self).__name__,
      utcTime=self._utcTime,
      engineSHA1=self._engineSHA1,
      timestamps=msgbuffers.shorten_sequence(self._timestamps),
      stationID=self._stationID,
      result=self._result)

  def __repr__(self):
    return '{type}(utcTime={utcTime}, engineSHA1={engineSHA1}, timestamps={timestamps}, stationID={stationID}, result={result})'.format(
      type=type(self).__name__,
      utcTime=repr(self._utcTime),
      engineSHA1=repr(self._engineSHA1),
      timestamps=repr(self._timestamps),
      stationID=repr(self._stationID),
      result=repr(self._result))

Anki.Cozmo.FactoryTestResultEntry = FactoryTestResultEntry
del FactoryTestResultEntry


class CalibMetaInfo(object):
  "Generated message-passing structure."

  __slots__ = (
    '_dotsFoundMask', # uint_8
  )

  @property
  def dotsFoundMask(self):
    "uint_8 dotsFoundMask struct property."
    return self._dotsFoundMask

  @dotsFoundMask.setter
  def dotsFoundMask(self, value):
    self._dotsFoundMask = msgbuffers.validate_integer(
      'CalibMetaInfo.dotsFoundMask', value, 0, 255)

  def __init__(self, dotsFoundMask=0):
    self.dotsFoundMask = dotsFoundMask

  @classmethod
  def unpack(cls, buffer):
    "Reads a new CalibMetaInfo from the given buffer."
    reader = msgbuffers.BinaryReader(buffer)
    value = cls.unpack_from(reader)
    if reader.tell() != len(reader):
      raise msgbuffers.ReadError(
        ('CalibMetaInfo.unpack received a buffer of length {length}, ' +
        'but only {position} bytes were read.').format(
        length=len(reader), position=reader.tell()))
    return value

  @classmethod
  def unpack_from(cls, reader):
    "Reads a new CalibMetaInfo from the given BinaryReader."
    _dotsFoundMask = reader.read('B')
    return cls(_dotsFoundMask)

  def pack(self):
    "Writes the current CalibMetaInfo, returning bytes."
    writer = msgbuffers.BinaryWriter()
    self.pack_to(writer)
    return writer.dumps()

  def pack_to(self, writer):
    "Writes the current CalibMetaInfo to the given BinaryWriter."
    writer.write(self._dotsFoundMask, 'B')

  def __eq__(self, other):
    if type(self) is type(other):
      return self._dotsFoundMask == other._dotsFoundMask
    else:
      return NotImplemented

  def __ne__(self, other):
    if type(self) is type(other):
      return not self.__eq__(other)
    else:
      return NotImplemented

  def __len__(self):
    return (msgbuffers.size(self._dotsFoundMask, 'B'))

  def __str__(self):
    return '{type}(dotsFoundMask={dotsFoundMask})'.format(
      type=type(self).__name__,
      dotsFoundMask=self._dotsFoundMask)

  def __repr__(self):
    return '{type}(dotsFoundMask={dotsFoundMask})'.format(
      type=type(self).__name__,
      dotsFoundMask=repr(self._dotsFoundMask))

Anki.Cozmo.CalibMetaInfo = CalibMetaInfo
del CalibMetaInfo


class IMUInfo(object):
  "Generated message-passing structure."

  __slots__ = (
    '_driftRate_degPerSec', # float_32
  )

  @property
  def driftRate_degPerSec(self):
    "float_32 driftRate_degPerSec struct property."
    return self._driftRate_degPerSec

  @driftRate_degPerSec.setter
  def driftRate_degPerSec(self, value):
    self._driftRate_degPerSec = msgbuffers.validate_float(
      'IMUInfo.driftRate_degPerSec', value, 'f')

  def __init__(self, driftRate_degPerSec=0.0):
    self.driftRate_degPerSec = driftRate_degPerSec

  @classmethod
  def unpack(cls, buffer):
    "Reads a new IMUInfo from the given buffer."
    reader = msgbuffers.BinaryReader(buffer)
    value = cls.unpack_from(reader)
    if reader.tell() != len(reader):
      raise msgbuffers.ReadError(
        ('IMUInfo.unpack received a buffer of length {length}, ' +
        'but only {position} bytes were read.').format(
        length=len(reader), position=reader.tell()))
    return value

  @classmethod
  def unpack_from(cls, reader):
    "Reads a new IMUInfo from the given BinaryReader."
    _driftRate_degPerSec = reader.read('f')
    return cls(_driftRate_degPerSec)

  def pack(self):
    "Writes the current IMUInfo, returning bytes."
    writer = msgbuffers.BinaryWriter()
    self.pack_to(writer)
    return writer.dumps()

  def pack_to(self, writer):
    "Writes the current IMUInfo to the given BinaryWriter."
    writer.write(self._driftRate_degPerSec, 'f')

  def __eq__(self, other):
    if type(self) is type(other):
      return self._driftRate_degPerSec == other._driftRate_degPerSec
    else:
      return NotImplemented

  def __ne__(self, other):
    if type(self) is type(other):
      return not self.__eq__(other)
    else:
      return NotImplemented

  def __len__(self):
    return (msgbuffers.size(self._driftRate_degPerSec, 'f'))

  def __str__(self):
    return '{type}(driftRate_degPerSec={driftRate_degPerSec})'.format(
      type=type(self).__name__,
      driftRate_degPerSec=self._driftRate_degPerSec)

  def __repr__(self):
    return '{type}(driftRate_degPerSec={driftRate_degPerSec})'.format(
      type=type(self).__name__,
      driftRate_degPerSec=repr(self._driftRate_degPerSec))

Anki.Cozmo.IMUInfo = IMUInfo
del IMUInfo


class CliffSensorValue(object):
  "Generated message-passing structure."

  __slots__ = (
    '_val', # uint_16
  )

  @property
  def val(self):
    "uint_16 val struct property."
    return self._val

  @val.setter
  def val(self, value):
    self._val = msgbuffers.validate_integer(
      'CliffSensorValue.val', value, 0, 65535)

  def __init__(self, val=0):
    self.val = val

  @classmethod
  def unpack(cls, buffer):
    "Reads a new CliffSensorValue from the given buffer."
    reader = msgbuffers.BinaryReader(buffer)
    value = cls.unpack_from(reader)
    if reader.tell() != len(reader):
      raise msgbuffers.ReadError(
        ('CliffSensorValue.unpack received a buffer of length {length}, ' +
        'but only {position} bytes were read.').format(
        length=len(reader), position=reader.tell()))
    return value

  @classmethod
  def unpack_from(cls, reader):
    "Reads a new CliffSensorValue from the given BinaryReader."
    _val = reader.read('H')
    return cls(_val)

  def pack(self):
    "Writes the current CliffSensorValue, returning bytes."
    writer = msgbuffers.BinaryWriter()
    self.pack_to(writer)
    return writer.dumps()

  def pack_to(self, writer):
    "Writes the current CliffSensorValue to the given BinaryWriter."
    writer.write(self._val, 'H')

  def __eq__(self, other):
    if type(self) is type(other):
      return self._val == other._val
    else:
      return NotImplemented

  def __ne__(self, other):
    if type(self) is type(other):
      return not self.__eq__(other)
    else:
      return NotImplemented

  def __len__(self):
    return (msgbuffers.size(self._val, 'H'))

  def __str__(self):
    return '{type}(val={val})'.format(
      type=type(self).__name__,
      val=self._val)

  def __repr__(self):
    return '{type}(val={val})'.format(
      type=type(self).__name__,
      val=repr(self._val))

Anki.Cozmo.CliffSensorValue = CliffSensorValue
del CliffSensorValue


class PoseData(object):
  "Generated message-passing structure."

  __slots__ = (
    '_angleX_rad', # float_32
    '_angleY_rad', # float_32
    '_angleZ_rad', # float_32
    '_transX_mm',  # float_32
    '_transY_mm',  # float_32
    '_transZ_mm',  # float_32
  )

  @property
  def angleX_rad(self):
    "float_32 angleX_rad struct property."
    return self._angleX_rad

  @angleX_rad.setter
  def angleX_rad(self, value):
    self._angleX_rad = msgbuffers.validate_float(
      'PoseData.angleX_rad', value, 'f')

  @property
  def angleY_rad(self):
    "float_32 angleY_rad struct property."
    return self._angleY_rad

  @angleY_rad.setter
  def angleY_rad(self, value):
    self._angleY_rad = msgbuffers.validate_float(
      'PoseData.angleY_rad', value, 'f')

  @property
  def angleZ_rad(self):
    "float_32 angleZ_rad struct property."
    return self._angleZ_rad

  @angleZ_rad.setter
  def angleZ_rad(self, value):
    self._angleZ_rad = msgbuffers.validate_float(
      'PoseData.angleZ_rad', value, 'f')

  @property
  def transX_mm(self):
    "float_32 transX_mm struct property."
    return self._transX_mm

  @transX_mm.setter
  def transX_mm(self, value):
    self._transX_mm = msgbuffers.validate_float(
      'PoseData.transX_mm', value, 'f')

  @property
  def transY_mm(self):
    "float_32 transY_mm struct property."
    return self._transY_mm

  @transY_mm.setter
  def transY_mm(self, value):
    self._transY_mm = msgbuffers.validate_float(
      'PoseData.transY_mm', value, 'f')

  @property
  def transZ_mm(self):
    "float_32 transZ_mm struct property."
    return self._transZ_mm

  @transZ_mm.setter
  def transZ_mm(self, value):
    self._transZ_mm = msgbuffers.validate_float(
      'PoseData.transZ_mm', value, 'f')

  def __init__(self, angleX_rad=0.0, angleY_rad=0.0, angleZ_rad=0.0, transX_mm=0.0, transY_mm=0.0, transZ_mm=0.0):
    self.angleX_rad = angleX_rad
    self.angleY_rad = angleY_rad
    self.angleZ_rad = angleZ_rad
    self.transX_mm = transX_mm
    self.transY_mm = transY_mm
    self.transZ_mm = transZ_mm

  @classmethod
  def unpack(cls, buffer):
    "Reads a new PoseData from the given buffer."
    reader = msgbuffers.BinaryReader(buffer)
    value = cls.unpack_from(reader)
    if reader.tell() != len(reader):
      raise msgbuffers.ReadError(
        ('PoseData.unpack received a buffer of length {length}, ' +
        'but only {position} bytes were read.').format(
        length=len(reader), position=reader.tell()))
    return value

  @classmethod
  def unpack_from(cls, reader):
    "Reads a new PoseData from the given BinaryReader."
    _angleX_rad = reader.read('f')
    _angleY_rad = reader.read('f')
    _angleZ_rad = reader.read('f')
    _transX_mm = reader.read('f')
    _transY_mm = reader.read('f')
    _transZ_mm = reader.read('f')
    return cls(_angleX_rad, _angleY_rad, _angleZ_rad, _transX_mm, _transY_mm, _transZ_mm)

  def pack(self):
    "Writes the current PoseData, returning bytes."
    writer = msgbuffers.BinaryWriter()
    self.pack_to(writer)
    return writer.dumps()

  def pack_to(self, writer):
    "Writes the current PoseData to the given BinaryWriter."
    writer.write(self._angleX_rad, 'f')
    writer.write(self._angleY_rad, 'f')
    writer.write(self._angleZ_rad, 'f')
    writer.write(self._transX_mm, 'f')
    writer.write(self._transY_mm, 'f')
    writer.write(self._transZ_mm, 'f')

  def __eq__(self, other):
    if type(self) is type(other):
      return (self._angleX_rad == other._angleX_rad and
        self._angleY_rad == other._angleY_rad and
        self._angleZ_rad == other._angleZ_rad and
        self._transX_mm == other._transX_mm and
        self._transY_mm == other._transY_mm and
        self._transZ_mm == other._transZ_mm)
    else:
      return NotImplemented

  def __ne__(self, other):
    if type(self) is type(other):
      return not self.__eq__(other)
    else:
      return NotImplemented

  def __len__(self):
    return (msgbuffers.size(self._angleX_rad, 'f') +
      msgbuffers.size(self._angleY_rad, 'f') +
      msgbuffers.size(self._angleZ_rad, 'f') +
      msgbuffers.size(self._transX_mm, 'f') +
      msgbuffers.size(self._transY_mm, 'f') +
      msgbuffers.size(self._transZ_mm, 'f'))

  def __str__(self):
    return '{type}(angleX_rad={angleX_rad}, angleY_rad={angleY_rad}, angleZ_rad={angleZ_rad}, transX_mm={transX_mm}, transY_mm={transY_mm}, transZ_mm={transZ_mm})'.format(
      type=type(self).__name__,
      angleX_rad=self._angleX_rad,
      angleY_rad=self._angleY_rad,
      angleZ_rad=self._angleZ_rad,
      transX_mm=self._transX_mm,
      transY_mm=self._transY_mm,
      transZ_mm=self._transZ_mm)

  def __repr__(self):
    return '{type}(angleX_rad={angleX_rad}, angleY_rad={angleY_rad}, angleZ_rad={angleZ_rad}, transX_mm={transX_mm}, transY_mm={transY_mm}, transZ_mm={transZ_mm})'.format(
      type=type(self).__name__,
      angleX_rad=repr(self._angleX_rad),
      angleY_rad=repr(self._angleY_rad),
      angleZ_rad=repr(self._angleZ_rad),
      transX_mm=repr(self._transX_mm),
      transY_mm=repr(self._transY_mm),
      transZ_mm=repr(self._transZ_mm))

Anki.Cozmo.PoseData = PoseData
del PoseData

