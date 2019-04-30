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
Source: clad/types/animationTrigger.clad
Full command line: ../tools/message-buffers/emitters/Python_emitter.py -C ./src/ -I ../robot/clad/src/ ../coretech/vision/clad/src/ ../coretech/common/clad/src/ ../lib/util/source/anki/clad -o ../generated/cladPython// clad/types/animationTrigger.clad
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

class AnimationTrigger(object):
  "Automatically-generated int_32 enumeration."
  AcknowledgeFaceInitPause                = 0
  AcknowledgeFaceNamed                    = 1
  AcknowledgeFaceUnnamed                  = 2
  AcknowledgeObject                       = 3
  AskToBeRightedLeft                      = 4
  AskToBeRightedRight                     = 5
  AudioTestAnim                           = 6
  BlockReact                              = 7
  BouncerGetIn                            = 8
  BouncerGetOut                           = 9
  BouncerIdeaToPlay                       = 10
  BouncerIntoScore1                       = 11
  BouncerIntoScore2                       = 12
  BouncerIntoScore3                       = 13
  BouncerRequestToPlay                    = 14
  BouncerTimeout                          = 15
  BouncerWait                             = 16
  BuildPyramidFirstBlockOnSide            = 17
  BuildPyramidFirstBlockUpright           = 18
  BuildPyramidLookForFace                 = 19
  BuildPyramidReactToBase                 = 20
  BuildPyramidSecondBlockOnSide           = 21
  BuildPyramidSecondBlockUpright          = 22
  BuildPyramidSuccess                     = 23
  BuildPyramidThankUser                   = 24
  BuildPyramidThirdBlockOnSide            = 25
  BuildPyramidThirdBlockUpright           = 26
  CantHandleTallStack                     = 27
  PatternGuessNewIdea                     = 28
  PatternGuessThinking                    = 29
  CodeLab123Go                            = 30
  CodeLabAmazed                           = 31
  CodeLabBlink                            = 32
  CodeLabBored                            = 33
  CodeLabCat                              = 34
  CodeLabCelebrate                        = 35
  CodeLabChatty                           = 36
  CodeLabChicken                          = 37
  CodeLabConducting                       = 38
  CodeLabCow                              = 39
  CodeLabCurious                          = 40
  CodeLabDancingMambo                     = 41
  CodeLabDejected                         = 42
  CodeLabDizzy                            = 43
  CodeLabDizzyEnd                         = 44
  CodeLabDog                              = 45
  CodeLabDuck                             = 46
  CodeLabElephant                         = 47
  CodeLabEnergyEat                        = 48
  CodeLabEnter                            = 49
  CodeLabExcited                          = 50
  CodeLabExit                             = 51
  CodeLabFireTruck                        = 52
  CodeLabFrog                             = 53
  CodeLabFrustrated                       = 54
  CodeLabGetInPos                         = 55
  CodeLabGhoul                            = 56
  CodeLabHappy                            = 57
  CodeLabHeadsUp                          = 58
  CodeLabHelium                           = 59
  CodeLabHiccup                           = 60
  CodeLabIDK                              = 61
  CodeLabIdle                             = 62
  CodeLabLose                             = 63
  CodeLabNo                               = 64
  CodeLabPartyTime                        = 65
  CodeLabRattleSnake                      = 66
  CodeLabReactHappy                       = 67
  CodeLabRooster                          = 68
  CodeLabScaredCozmo                      = 69
  CodeLabScaryCozmo                       = 70
  CodeLabSheep                            = 71
  CodeLabSleep                            = 72
  CodeLabSneeze                           = 73
  CodeLabSquint1                          = 74
  CodeLabSquint2                          = 75
  CodeLabStaring                          = 76
  CodeLabSurprise                         = 77
  CodeLabTakaTaka                         = 78
  CodeLabTapCube                          = 79
  CodeLabThinking                         = 80
  CodeLabTiger                            = 81
  CodeLabTwitch                           = 82
  CodeLabUnhappy                          = 83
  CodeLabVampire                          = 84
  CodeLabVictory                          = 85
  CodeLabWhee1                            = 86
  CodeLabWhee2                            = 87
  CodeLabWhee3                            = 88
  CodeLabWhee4                            = 89
  CodeLabWhew                             = 90
  CodeLabWhoa                             = 91
  CodeLabWin                              = 92
  CodeLabWondering                        = 93
  CodeLabYes                              = 94
  CodeLabYuck                             = 95
  CodeLabZombie                           = 96
  ConnectWakeUp                           = 97
  ConnectWakeUp_SevereEnergy              = 98
  ConnectWakeUp_SevereRepair              = 99
  ComeHere_AlreadyHere                    = 100
  ComeHere_SearchForFace                  = 101
  ComeHere_SearchForFace_FoundFace        = 102
  CozmoSaysGetIn                          = 103
  CozmoSaysGetOut                         = 104
  CozmoSaysSpeakGetInShort                = 105
  CozmoSaysSpeakGetInMedium               = 106
  CozmoSaysSpeakGetInLong                 = 107
  CozmoSaysSpeakGetOutShort               = 108
  CozmoSaysSpeakGetOutMedium              = 109
  CozmoSaysSpeakGetOutLong                = 110
  CozmoSaysSpeakLoop                      = 111
  CozmoSaysBadWord                        = 112
  CozmoSaysIdle                           = 113
  CubeMovedSense                          = 114
  CubeMovedUpset                          = 115
  CubePounceFake                          = 116
  CubePounceGetIn                         = 117
  CubePounceGetOut                        = 118
  CubePounceGetReady                      = 119
  CubePounceGetUnready                    = 120
  CubePounceIdleLiftDown                  = 121
  CubePounceIdleLiftUp                    = 122
  CubePounceLoseHand                      = 123
  CubePounceLoseRound                     = 124
  CubePounceLoseSession                   = 125
  CubePouncePounceClose                   = 126
  CubePouncePounceNormal                  = 127
  CubePounceWinHand                       = 128
  CubePounceWinRound                      = 129
  CubePounceWinSession                    = 130
  DanceMambo                              = 131
  DemoSpeedTapCozmoWin                    = 132
  DemoSpeedTapCozmoLose                   = 133
  DizzyReactionHard                       = 134
  DizzyReactionMedium                     = 135
  DizzyReactionSoft                       = 136
  DizzyShakeLoop                          = 137
  DizzyShakeStop                          = 138
  DizzyStillPickedUp                      = 139
  DriveEndAngry                           = 140
  DriveEndDefault                         = 141
  DriveEndHappy                           = 142
  DriveEndLaunch                          = 143
  DriveLoopAngry                          = 144
  DriveLoopDefault                        = 145
  DriveLoopHappy                          = 146
  DriveLoopLaunch                         = 147
  DriveStartAngry                         = 148
  DriveStartDefault                       = 149
  DriveStartHappy                         = 150
  DriveStartLaunch                        = 151
  DroneModeBackwardDrivingEnd             = 152
  DroneModeBackwardDrivingLoop            = 153
  DroneModeBackwardDrivingStart           = 154
  DroneModeCliffEvent                     = 155
  DroneModeForwardDrivingEnd              = 156
  DroneModeForwardDrivingLoop             = 157
  DroneModeForwardDrivingStart            = 158
  DroneModeGetIn                          = 159
  DroneModeGetOut                         = 160
  DroneModeIdle                           = 161
  DroneModeKeepAlive                      = 162
  DroneModeTurboDrivingStart              = 163
  EarnedSparks                            = 164
  FacePlantRoll                           = 165
  FacePlantRollArmUp                      = 166
  FailedToRightFromFace                   = 167
  FeedingAteFullEnough_Normal             = 168
  FeedingAteFullEnough_Severe             = 169
  FeedingAteNotFullEnough_Normal          = 170
  FeedingAteNotFullEnough_Severe          = 171
  FeedingDrivingGetIn_Severe              = 172
  FeedingDrivingGetOut_Severe             = 173
  FeedingDrivingLoop_Severe               = 174
  FeedingPlaceLiftOnCube_Normal           = 175
  FeedingPlaceLiftOnCube_Severe           = 176
  FeedingIdleSearch_Normal                = 177
  FeedingIdleSearch_Severe                = 178
  FeedingIdleSearchForFaces_Normal        = 179
  FeedingIdleSearchForFaces_Severe        = 180
  FeedingIdleWaitForFullCube_Normal       = 181
  FeedingIdleWaitForFullCube_Severe       = 182
  FeedingIdleWaitForShakeNoHead_Severe    = 183
  FeedingIdleWaitForShake_Normal          = 184
  FeedingIdleWaitForShake_Severe          = 185
  FeedingInterrupted                      = 186
  FeedingInterrupted_Severe               = 187
  FeedingSearchRequest                    = 188
  FeedingSearchRequest_Severe             = 189
  FeedingSearchFailure                    = 190
  FeedingSearchFailure_Severe             = 191
  FeedingReactToFullCube_Normal           = 192
  FeedingReactToFullCube_Severe           = 193
  FeedingReactToSeeCube_Normal            = 194
  FeedingReactToSeeCube_Severe            = 195
  FeedingReactToShake_Normal              = 196
  FeedingReactToShake_Severe              = 197
  FistBumpIdle                            = 198
  FistBumpRequestOnce                     = 199
  FistBumpRequestRetry                    = 200
  FistBumpSuccess                         = 201
  FistBumpLeftHanging                     = 202
  FlipDownFromBack                        = 203
  FrustratedByFailure                     = 204
  FrustratedByFailureMajor                = 205
  GameSetupGetIn                          = 206
  GameSetupGetOut                         = 207
  GameSetupIdle                           = 208
  GameSetupReaction                       = 209
  GoToSleepGetIn                          = 210
  GoToSleepGetOut                         = 211
  GoToSleepOff                            = 212
  GoToSleepSleeping                       = 213
  GuardDogBusted                          = 214
  GuardDogCubeDisconnect                  = 215
  GuardDogFakeout                         = 216
  GuardDogInterruption                    = 217
  GuardDogPlayerSuccess                   = 218
  GuardDogPulse                           = 219
  GuardDogSettle                          = 220
  GuardDogSleepLoop                       = 221
  GuardDogTimeout                         = 222
  GuardDogTimeoutCubesTouched             = 223
  GuardDogTimeoutCubesUntouched           = 224
  Hiccup                                  = 225
  HiccupGetIn                             = 226
  HiccupPlayerCure                        = 227
  HiccupRobotOnBack                       = 228
  HiccupRobotOnFace                       = 229
  HiccupRobotPickedUp                     = 230
  HiccupSelfCure                          = 231
  HikingDrivingEnd                        = 232
  HikingDrivingLoop                       = 233
  HikingDrivingStart                      = 234
  HikingInterestingEdgeThought            = 235
  HikingIntro                             = 236
  HikingLookAround                        = 237
  HikingObserve                           = 238
  HikingReactToEdge                       = 239
  HikingReactToNewArea                    = 240
  HikingReactToPossibleMarker             = 241
  HikingSquintEnd                         = 242
  HikingSquintLoop                        = 243
  HikingSquintStart                       = 244
  HikingWakeUpOffCharger                  = 245
  IdleOnCharger                           = 246
  InteractWithFaceTrackingIdle            = 247
  InteractWithFacesInitialNamed           = 248
  InteractWithFacesInitialUnnamed         = 249
  KnockOverEyes                           = 250
  KnockOverFailure                        = 251
  KnockOverGrabAttempt                    = 252
  KnockOverPreActionNamedFace             = 253
  KnockOverPreActionUnnamedFace           = 254
  KnockOverSuccess                        = 255
  LaserAcknowledge                        = 256
  LaserDriveEnd                           = 257
  LaserDriveLoop                          = 258
  LaserDriveStart                         = 259
  LaserFace                               = 260
  LaserGetOut                             = 261
  LaserPounce                             = 262
  LookInPlaceForFacesBodyPause            = 263
  LookInPlaceForFacesHeadMovePause        = 264
  MajorFail                               = 265
  MajorWin                                = 266
  MeetCozmoGetIn                          = 267
  MeetCozmoLookFaceGetIn                  = 268
  MeetCozmoLookFaceGetOut                 = 269
  MeetCozmoScanningIdle                   = 270
  MeetCozmoFirstEnrollmentSayName         = 271
  MeetCozmoFirstEnrollmentRepeatName      = 272
  MeetCozmoFirstEnrollmentCelebration     = 273
  MeetCozmoReEnrollmentSayName            = 274
  MeetCozmoRenameFaceSayName              = 275
  MeetCozmoLookFaceInterrupt              = 276
  MemoryMatchPlayerWinHand                = 277
  MemoryMatchPlayerWinHandLong            = 278
  MemoryMatchPlayerWinHandSolo            = 279
  MemoryMatchPlayerLoseHand               = 280
  MemoryMatchPlayerLoseHandSolo           = 281
  MemoryMatchCozmoWinHand                 = 282
  MemoryMatchCozmoLoseHand                = 283
  MemoryMatchCozmoWinGame                 = 284
  MemoryMatchPlayerWinGame                = 285
  MemoryMatchSoloGameOver                 = 286
  MemoryMatchReactToPattern               = 287
  MemoryMatchReactToPatternSolo           = 288
  MemoryMatchPointCenter                  = 289
  MemoryMatchPointLeftBig                 = 290
  MemoryMatchPointLeftSmall               = 291
  MemoryMatchPointRightBig                = 292
  MemoryMatchPointRightSmall              = 293
  MemoryMatchPointCenterFast              = 294
  MemoryMatchPointLeftBigFast             = 295
  MemoryMatchPointLeftSmallFast           = 296
  MemoryMatchPointRightBigFast            = 297
  MemoryMatchPointRightSmallFast          = 298
  MemoryMatchCozmoGetOut                  = 299
  MemoryMatchCozmoFollowTapsSoundOnly     = 300
  NamedFaceInitialGreeting                = 301
  NeedsMildLowEnergyRequest               = 302
  NeedsMildLowPlayRequest                 = 303
  NeedsMildLowRepairRequest               = 304
  NeedsSevereLowEnergyCliffReact          = 305
  NeedsSevereLowEnergyDrivingEnd          = 306
  NeedsSevereLowEnergyDrivingLoop         = 307
  NeedsSevereLowEnergyDrivingStart        = 308
  NeedsSevereLowEnergyForceGetOut         = 309
  NeedsSevereLowEnergyGetIn               = 310
  NeedsSevereLowEnergyIdle                = 311
  NeedsSevereLowEnergyRequest             = 312
  NeedsSevereLowEnergySlopeReact          = 313
  NeedsSevereLowPlayForceGetOut           = 314
  NeedsSevereLowPlayGetIn                 = 315
  NeedsSevereLowPlayRequest               = 316
  NeedsSevereLowRepairCliffReact          = 317
  NeedsSevereLowRepairDrivingEnd          = 318
  NeedsSevereLowRepairDrivingLoop         = 319
  NeedsSevereLowRepairDrivingStart        = 320
  NeedsSevereLowRepairForceGetOut         = 321
  NeedsSevereLowRepairGetIn               = 322
  NeedsSevereLowRepairIdle                = 323
  NeedsSevereLowRepairRequest             = 324
  NeedsSevereLowRepairSlopeReact          = 325
  NeutralFace                             = 326
  NothingToDoBoredEvent                   = 327
  NothingToDoBoredIdle                    = 328
  NothingToDoBoredIntro                   = 329
  NothingToDoBoredOutro                   = 330
  OnLearnedPlayerName                     = 331
  OnSawNewNamedFace                       = 332
  OnSawNewUnnamedFace                     = 333
  OnSawOldNamedFace                       = 334
  OnSawOldUnnamedFace                     = 335
  OnSpeedtapCozmoConfirm                  = 336
  OnSpeedtapFakeout                       = 337
  OnSpeedtapGameCozmoWinHighIntensity     = 338
  OnSpeedtapGameCozmoWinLowIntensity      = 339
  OnSpeedtapGamePlayerWinHighIntensity    = 340
  OnSpeedtapGamePlayerWinLowIntensity     = 341
  OnSpeedtapGetOut                        = 342
  OnSpeedtapHandCozmoWin                  = 343
  OnSpeedtapHandPlayerWin                 = 344
  OnSpeedtapIdle                          = 345
  OnSpeedtapRoundCozmoWinHighIntensity    = 346
  OnSpeedtapRoundCozmoWinLowIntensity     = 347
  OnSpeedtapRoundPlayerWinHighIntensity   = 348
  OnSpeedtapRoundPlayerWinLowIntensity    = 349
  OnSpeedtapTap                           = 350
  OnWaitForCubesMinigameSetup             = 351
  OnWiggle                                = 352
  OnboardingBirth                         = 353
  OnboardingCubeDockFail                  = 354
  OnboardingDiscoverCube                  = 355
  OnboardingDriveEnd                      = 356
  OnboardingDriveLoop                     = 357
  OnboardingDriveStart                    = 358
  OnboardingEyesOn                        = 359
  OnboardingHelloPlayer                   = 360
  OnboardingHelloWorld                    = 361
  OnboardingIdle                          = 362
  OnboardingIdleEnergy                    = 363
  OnboardingIdlePlay                      = 364
  OnboardingIdleRepair                    = 365
  OnboardingInteractWithCube              = 366
  OnboardingPreBirth                      = 367
  OnboardingReactToCube                   = 368
  OnboardingReactToCubePutDown            = 369
  OnboardingReactToFace                   = 370
  OnboardingSoundOnlyLiftEffortPickup     = 371
  OnboardingSoundOnlyLiftEffortPlaceLow   = 372
  OnboardingGetOut                        = 373
  OnboardingWakeUpDriveOffCharger         = 374
  PeekABooGetIn                           = 375
  PeekABooGetOutHappy                     = 376
  PeekABooGetOutSad                       = 377
  PeekABooHighIntensity                   = 378
  PeekABooIdle                            = 379
  PeekABooLowIntensity                    = 380
  PeekABooMedIntensity                    = 381
  PeekABooNoUserInteraction               = 382
  PeekABooShort                           = 383
  PeekABooSurprised                       = 384
  PetDetectionCat                         = 385
  PetDetectionDog                         = 386
  PetDetectionShort                       = 387
  PetDetectionShort_Cat                   = 388
  PetDetectionShort_Dog                   = 389
  PetDetectionSneeze                      = 390
  PickupHelperPreActionNamedFace          = 391
  PickupHelperPreActionUnnamedFace        = 392
  PlacedOnCharger                         = 393
  PopAWheelieInitial                      = 394
  PopAWheeliePreActionNamedFace           = 395
  PopAWheeliePreActionUnnamedFace         = 396
  PopAWheelieRealign                      = 397
  PopAWheelieRetry                        = 398
  PounceDriveEnd                          = 399
  PounceDriveLoop                         = 400
  PounceDriveStart                        = 401
  PounceFace                              = 402
  PounceFail                              = 403
  PounceGetOut                            = 404
  PounceInitial                           = 405
  PouncePounce                            = 406
  PounceSuccess                           = 407
  ProceduralLive                          = 408
  PutDownBlockKeepAlive                   = 409
  PutDownBlockPutDown                     = 410
  ReactToBlockPickupSuccess               = 411
  ReactToBlockRetryPickup                 = 412
  ReactToCliff                            = 413
  ReactToCliffDetectorStop                = 414
  ReactToFalling                          = 415
  ReactToImpact                           = 416
  ReactToObstacle                         = 417
  ReactToMotorCalibration                 = 418
  ReactToNewBlockAsk                      = 419
  ReactToNewBlockBig                      = 420
  ReactToNewBlockSmall                    = 421
  ReactToOnLeftSide                       = 422
  ReactToOnRightSide                      = 423
  ReactToPerchedOnBlock                   = 424
  ReactToPickup                           = 425
  ReactToPokeReaction                     = 426
  ReactToPokeStartled                     = 427
  ReactToUnexpectedMovement               = 428
  ReactToUnexpectedMovement_Severe_Energy = 429
  ReactToUnexpectedMovement_Severe_Repair = 430
  RepairFailMild                          = 431
  RepairFailSevere                        = 432
  RepairFixMildGetIn                      = 433
  RepairFixMildGetOut                     = 434
  RepairFixMildGetReady                   = 435
  RepairFixMildHeadDown                   = 436
  RepairFixMildHeadUp                     = 437
  RepairFixMildIdle                       = 438
  RepairFixMildLiftDown                   = 439
  RepairFixMildLiftUp                     = 440
  RepairFixMildLowerLift                  = 441
  RepairFixMildRaiseLift                  = 442
  RepairFixMildRoundReact                 = 443
  RepairFixMildWheelsBack                 = 444
  RepairFixMildWheelsForward              = 445
  RepairFixSevereGetIn                    = 446
  RepairFixSevereGetOut                   = 447
  RepairFixSevereGetReady                 = 448
  RepairFixSevereHeadDown                 = 449
  RepairFixSevereHeadUp                   = 450
  RepairFixSevereIdle                     = 451
  RepairFixSevereLiftDown                 = 452
  RepairFixSevereLiftUp                   = 453
  RepairFixSevereLowerLift                = 454
  RepairFixSevereRaiseLift                = 455
  RepairFixSevereRoundReact               = 456
  RepairFixSevereWheelsBack               = 457
  RepairFixSevereWheelsForward            = 458
  RepairIdleFullyRepaired                 = 459
  RepairPartRepaired_Head_Mild            = 460
  RepairPartRepaired_Lift_Mild            = 461
  RepairPartRepaired_Tread_Mild           = 462
  RequestGameInterrupt                    = 463
  RequestGameKeepAwayAccept0              = 464
  RequestGameKeepAwayAccept1              = 465
  RequestGameKeepAwayDeny0                = 466
  RequestGameKeepAwayDeny1                = 467
  RequestGameKeepAwayIdle0                = 468
  RequestGameKeepAwayIdle1                = 469
  RequestGameKeepAwayInitial0             = 470
  RequestGameKeepAwayInitial1             = 471
  RequestGameKeepAwayPreDrive0            = 472
  RequestGameKeepAwayPreDrive1            = 473
  RequestGameKeepAwayRequest0             = 474
  RequestGameKeepAwayRequest1             = 475
  RequestGameMemoryMatchAccept0           = 476
  RequestGameMemoryMatchAccept1           = 477
  RequestGameMemoryMatchDeny0             = 478
  RequestGameMemoryMatchDeny1             = 479
  RequestGameMemoryMatchIdle0             = 480
  RequestGameMemoryMatchIdle1             = 481
  RequestGameMemoryMatchInitial0          = 482
  RequestGameMemoryMatchInitial1          = 483
  RequestGameMemoryMatchPreDrive0         = 484
  RequestGameMemoryMatchPreDrive1         = 485
  RequestGameMemoryMatchRequest0          = 486
  RequestGameMemoryMatchRequest1          = 487
  RequestGamePickupFail                   = 488
  RequestGameSpeedTapAccept0              = 489
  RequestGameSpeedTapAccept1              = 490
  RequestGameSpeedTapDeny0                = 491
  RequestGameSpeedTapDeny1                = 492
  RequestGameSpeedTapIdle0                = 493
  RequestGameSpeedTapIdle1                = 494
  RequestGameSpeedTapInitial0             = 495
  RequestGameSpeedTapInitial1             = 496
  RequestGameSpeedTapPreDrive0            = 497
  RequestGameSpeedTapPreDrive1            = 498
  RequestGameSpeedTapRequest0             = 499
  RequestGameSpeedTapRequest1             = 500
  RollBlockInitial                        = 501
  RollBlockPreActionNamedFace             = 502
  RollBlockPreActionUnnamedFace           = 503
  RollBlockPutDown                        = 504
  RollBlockRealign                        = 505
  RollBlockRetry                          = 506
  RollBlockSuccess                        = 507
  SdkTextToSpeech                         = 508
  Shiver                                  = 509
  Shocked                                 = 510
  Singing_80bpm                           = 511
  Singing_100bpm                          = 512
  Singing_120bpm                          = 513
  Singing_GetIn                           = 514
  Singing_GetOut                          = 515
  Sleeping                                = 516
  SoftSparkUpgradeLift                    = 517
  SoftSparkUpgradeTracks                  = 518
  SoundOnlyLiftEffortPickup               = 519
  SoundOnlyLiftEffortPlaceHigh            = 520
  SoundOnlyLiftEffortPlaceLow             = 521
  SoundOnlyLiftEffortPlaceRoll            = 522
  SoundOnlyRamIntoBlock                   = 523
  SoundOnlyTurnSmall                      = 524
  SparkDrivingLoop                        = 525
  SparkDrivingStart                       = 526
  SparkDrivingStop                        = 527
  SparkFailure                            = 528
  SparkGetIn                              = 529
  SparkGetOut                             = 530
  SparkIdle                               = 531
  SparkPickupFinalCubeReaction            = 532
  SparkPickupInitialCubeReaction          = 533
  SparkSuccess                            = 534
  SpeedTapDrivingEnd                      = 535
  SpeedTapDrivingLoop                     = 536
  SpeedTapDrivingStart                    = 537
  StackBlocksSuccess                      = 538
  StartSleeping                           = 539
  SuccessfulWheelie                       = 540
  Surprise                                = 541
  TurtleRoll                              = 542
  UnitTestAnim                            = 543
  VC_Alrighty                             = 544
  VC_HowAreYouDoing_AllGood               = 545
  VC_Listening                            = 546
  VC_LookDownForLaser                     = 547
  VC_LookDownNoLaser                      = 548
  VC_NoFollowupCommand_NoFace             = 549
  VC_NoFollowupCommand_WithFace           = 550
  VC_Refuse_energy                        = 551
  VC_Refuse_repair                        = 552
  VC_Refuse_sparks                        = 553
  VC_StartledWakeup                       = 554
  WaitOnSideLoop                          = 555
  WorkoutPostLift_highEnergy              = 556
  WorkoutPostLift_lowEnergy               = 557
  WorkoutPostLift_mediumEnergy            = 558
  WorkoutPreLift_highEnergy               = 559
  WorkoutPreLift_lowEnergy                = 560
  WorkoutPreLift_mediumEnergy             = 561
  WorkoutPutDown_highEnergy               = 562
  WorkoutPutDown_lowEnergy                = 563
  WorkoutPutDown_lowEnergy_simple         = 564
  WorkoutPutDown_mediumEnergy             = 565
  WorkoutStrongLift_highEnergy            = 566
  WorkoutStrongLift_lowEnergy             = 567
  WorkoutStrongLift_mediumEnergy          = 568
  WorkoutTransition_highEnergy            = 569
  WorkoutTransition_lowEnergy             = 570
  WorkoutTransition_mediumEnergy          = 571
  WorkoutWeakLift_highEnergy              = 572
  WorkoutWeakLift_lowEnergy               = 573
  WorkoutWeakLift_mediumEnergy            = 574
  Count                                   = 575

Anki.Cozmo.AnimationTrigger = AnimationTrigger
del AnimationTrigger


class CubeAnimationTrigger(object):
  "Automatically-generated int_32 enumeration."
  Carrying                    = 0
  Connected                   = 1
  CubePouncePlayerLose        = 2
  CubePouncePlayerWin         = 3
  Dance_01                    = 4
  Dance_02                    = 5
  Dance_03                    = 6
  Dance_04                    = 7
  Dance_05                    = 8
  Dance_06                    = 9
  DanceFadeOff                = 10
  DrivingTo                   = 11
  FeedingBlank                = 12
  FeedingCyanCycle            = 13
  FeedingCyanSolid            = 14
  Flash                       = 15
  GatherCubesAllCubesInBeacon = 16
  GatherCubesCubeInBeacon     = 17
  GuardDogBeingMoved          = 18
  GuardDogBusted              = 19
  GuardDogOff                 = 20
  GuardDogSetup               = 21
  GuardDogSleeping            = 22
  GuardDogSuccessfullyFlipped = 23
  Interacting                 = 24
  InteractingBehaviorLock     = 25
  Onboarding                  = 26
  PyramidBaseBottom           = 27
  PyramidFlourish             = 28
  PyramidOnSideLocated        = 29
  PyramidOnSideNotLocated     = 30
  PyramidPickup               = 31
  PyramidSingle               = 32
  Sleep                       = 33
  SleepNoFade                 = 34
  SpeedTapWin                 = 35
  SpeedTapLose                = 36
  Visible                     = 37
  WakeUp                      = 38
  Workout                     = 39
  Count                       = 40

Anki.Cozmo.CubeAnimationTrigger = CubeAnimationTrigger
del CubeAnimationTrigger

