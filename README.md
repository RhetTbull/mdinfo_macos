# mdinfo-macos

Plugin for [mdinfo](https://github.com/RhetTbull/mdinfo) that provides access to macOS specific metadata.

## Synopsis

```bash
mdinfo -p "{mac:kMDItemKeywords}" -p "{finder:comment}" *.*
```

## Installation

Requires [mdinfo](https://github.com/RhetTbull/mdinfo) to be installed.

```bash
pip install mdinfo
pip install mdinfo-macos
```

## Template Help

<!-- [[[cog
import cog
from mdinfo_macos import get_markdown_help 
cog.out(
    "\n{}\n".format(get_markdown_help())
)
]]] -->

**MacOS Specific Metadata**
| Field | Description              |
| ----- | ------------------------ |
| {mac} | Format: '{mac:SUBFIELD}' |


The `{mac}` template provides access to a wide range of macOS specific metadata fields
including all Spotlight metadata fields. 

The following attributes are supported:

kMDItemDueDate, kMDItemDurationSeconds, kMDItemResolutionWidthDPI, NSURLFileAllocatedSizeKey, NSURLIsExecutableKey, kMDItemGPSMapDatum, kMDItemEXIFVersion, kMDItemInformation, NSURLVolumeSupportsHardLinksKey, NSURLLabelColorKey, kMDItemEncodingApplications, NSURLIsAliasFileKey, NSURLVolumeSupportsExtendedSecurityKey, kMDItemColorSpace, NSURLIsUbiquitousItemKey, kMDItemHeadline, kMDItemAcquisitionMake, NSURLVolumeSupportsImmutableFilesKey, NSURLUbiquitousItemDownloadRequestedKey, NSURLUbiquitousItemUploadingErrorKey, kMDItemTextContent, kMDItemCountry, kMDItemVideoBitRate, NSURLFileSecurityKey, kMDItemGenre, kMDItemFSNodeCount, kMDItemRecipientEmailAddresses, NSURLUbiquitousItemIsUploadingKey, kMDItemGPSDateStamp, kMDItemGPSStatus, NSURLIsSystemImmutableKey, com.apple.FinderInfo, NSURLCanonicalPathKey, kMDItemDeliveryType, kMDItemLyricist, NSURLDocumentIdentifierKey, NSURLContentTypeKey, kMDLabelIconData, kMDItemLanguages, kMDLabelKindIsMutuallyExclusiveSetKey, kMDItemSpeed, NSURLVolumeIsJournalingKey, NSURLVolumeNameKey, kMDItemLensModel, kMDItemCodecs, kMDItemMusicalInstrumentCategory, kMDItemRecipientAddresses, NSURLVolumeIsAutomountedKey, NSURLIsExcludedFromBackupKey, kMDItemAppleLoopsRootKey, kMDItemIsGeneralMIDISequence, kMDItemAttributeChangeDate, NSURLFileResourceIdentifierKey, NSURLIsDirectoryKey, NSURLVolumeSupportsSwapRenamingKey, kMDItemGPSDestLatitude, NSURLEffectiveIconKey, kMDItemVersion, kMDItemAppleLoopsLoopMode, NSURLVolumeSupportsExclusiveRenamingKey, kMDItemMeteringMode, NSURLIsSymbolicLinkKey, kMDItemCreator, NSURLVolumeResourceCountKey, kMDItemMusicalGenre, NSURLUbiquitousSharedItemCurrentUserRoleKey, kMDItemAppleLoopsKeyFilterType, NSURLMayShareFileContentKey, NSURLPreferredIOBlockSizeKey, NSURLUbiquitousSharedItemMostRecentEditorNameComponentsKey, kMDLabelUserDomain, NSURLFileContentIdentifierKey, NSURLVolumeSupportsJournalingKey, kMDItemTitle, kMDItemNamedLocation, NSURLVolumeURLForRemountingKey, NSURLUbiquitousItemDownloadingErrorKey, NSURLUbiquitousItemIsExcludedFromSyncKey, kMDItemCity, kMDItemFSSize, kMDItemMediaTypes, NSURLVolumeAvailableCapacityForImportantUsageKey, NSURLVolumeMaximumFileSizeKey, kMDItemGPSTrack, kMDItemTheme, kMDItemIsLikelyJunk, kMDItemEmailAddresses, kMDItemPerformers, kMDItemAudioTrackNumber, kMDItemSecurityMethod, kMDItemOriginalSource, kMDItemProfileName, kMDItemAltitude, kMDItemAudioEncodingApplication, kMDItemPageHeight, stationerypad, NSURLVolumeAvailableCapacityForOpportunisticUsageKey, NSURLFileResourceTypeKey, NSURLVolumeIsReadOnlyKey, kMDItemFSOwnerGroupID, NSURLVolumeAvailableCapacityKey, kMDItemURL, kMDItemPhoneNumbers, NSURLMayHaveExtendedAttributesKey, NSURLAddedToDirectoryDateKey, NSURLLinkCountKey, NSURLVolumeIsRemovableKey, kMDItemGPSAreaInformation, kMDItemPixelWidth, kMDItemStreamable, kMDItemExecutableArchitectures, NSURLIsReadableKey, NSURLVolumeIsEncryptedKey, NSURLFileSizeKey, kMDItemFNumber, kMDPublicVisibility, kMDItemHasAlphaChannel, NSURLUbiquitousItemIsDownloadingKey, kMDLabelBundleURL, kMDItemTimestamp, kMDItemComment, NSURLVolumeIsBrowsableKey, kMDItemCFBundleIdentifier, kMDLabelSetsFinderColor, kMDLabelIsMutuallyExclusiveSetMember, kMDItemExposureTimeSeconds, kMDItemImageDirection, kMDItemLayerNames, NSURLVolumeSupportsPersistentIDsKey, kMDItemPixelCount, kMDItemPageWidth, NSURLIsSparseKey, kMDItemLastUsedDate, NSURLAttributeModificationDateKey, kMDItemBitsPerSample, kMDItemAudioChannelCount, NSURLLocalizedNameKey, kMDItemOrientation, NSURLCustomIconKey, kMDItemExposureProgram, kMDItemAcquisitionModel, kMDItemLatitude, NSURLVolumeSupportsAccessPermissionsKey, NSURLContentModificationDateKey, kMDItemGPSDestDistance, kMDItemGPSDestLongitude, kMDItemExposureTimeString, kMDItemEditors, kMDLabelKind, NSURLIsWritableKey, kMDItemIdentifier, NSURLVolumeSupportsCompressionKey, kMDPrivateVisibility, NSURLVolumeCreationDateKey, NSURLVolumeSupportsSymbolicLinksKey, NSURLVolumeSupportsFileProtectionKey, NSURLGenerationIdentifierKey, kMDItemCameraOwner, kMDItemContentModificationDate, kMDItemPixelHeight, kMDItemLongitude, NSURLIsPackageKey, kMDItemGPSProcessingMethod, kMDItemContributors, kMDItemFSLabel, kMDItemGPSDifferental, kMDItemAudioBitRate, kMDItemAlbum, kMDItemFSCreationDate, kMDItemISOSpeed, kMDItemRedEyeOnOff, NSURLVolumeSupportsCasePreservedNamesKey, NSURLVolumeSupportsFileCloningKey, kMDItemTempo, kMDLabelDisplayName, NSURLVolumeSupportsVolumeSizesKey, NSURLVolumeIsLocalKey, NSURLTotalFileSizeKey, kMDItemPublishers, kMDItemRights, kMDItemAudioSampleRate, kMDItemFSInvisible, kMDItemNumberOfPages, kMDItemExposureMode, NSURLVolumeSupportsCaseSensitiveNamesKey, NSURLVolumeLocalizedFormatDescriptionKey, kMDItemContentTypeTree, kMDItemGPSMeasureMode, NSURLVolumeLocalizedNameKey, kMDItemOrganizations, NSURLIsRegularFileKey, NSURLVolumeIsInternalKey, kMDItemDisplayName, NSURLVolumeSupportsZeroRunsKey, kMDItemDirector, kMDItemAuthors, kMDItemApplicationCategories, NSURLVolumeUUIDStringKey, kMDItemComposer, kMDItemKind, kMDItemMaxAperture, kMDItemEXIFGPSVersion, kMDLabelChangedNotification, NSURLHasHiddenExtensionKey, NSURLPathKey, kMDItemParticipants, NSURLParentDirectoryURLKey, NSURLUbiquitousItemDownloadingStatusKey, NSURLIsHiddenKey, kMDItemFSContentChangeDate, kMDItemFocalLength, NSURLApplicationIsScriptableKey, kMDItemDateAdded, NSURLUbiquitousSharedItemCurrentUserPermissionsKey, NSURLIsMountTriggerKey, kMDItemGPSDestBearing, kMDItemContentType, NSURLContentAccessDateKey, kMDLabelUUID, kMDItemFocalLength35mm, NSURLVolumeSupportsSparseFilesKey, kMDItemHTMLContent, kMDItemStarRating, NSURLTotalFileAllocatedSizeKey, NSURLIsUserImmutableKey, NSURLUbiquitousItemIsSharedKey, NSURLVolumeSupportsAdvisoryFileLockingKey, kMDItemResolutionHeightDPI, NSURLUbiquitousItemContainerDisplayNameKey, kMDItemGPSDOP, findercolor, NSURLVolumeIsRootFileSystemKey, kMDItemContentCreationDate, kMDItemFSOwnerUserID, kMDLabelRemovedNotification, kMDItemFSHasCustomIcon, kMDItemKeywords, kMDLabelContentChangeDate, kMDItemTimeSignature, kMDItemTotalBitRate, kMDItemAuthorAddresses, kMDItemFSIsStationery, NSURLNameKey, kMDItemExecutablePlatform, kMDItemWhereFroms, kMDItemAuthorEmailAddresses, kMDItemRecordingDate, kMDItemSubject, NSURLVolumeSupportsRootDirectoryDatesKey, NSURLLabelNumberKey, kMDLabelAddedNotification, kMDItemOriginalFormat, kMDItemMusicalInstrumentName, NSURLVolumeSupportsRenamingKey, kMDItemFonts, kMDItemRecipients, kMDItemContactKeywords, NSURLIsVolumeKey, NSURLVolumeIdentifierKey, kMDItemRecordingYear, NSURLFileProtectionKey, NSURLLocalizedLabelKey, kMDItemCoverage, kMDItemInstantMessageAddresses, kMDItemAudiences, NSURLVolumeIsEjectableKey, NSURLIsApplicationKey, NSURLKeysOfUnsetValuesKey, kMDItemFSName, kMDItemInstructions, kMDItemProducer, kMDItemCopyright, kMDItemFSIsExtensionHidden, kMDItemDownloadedDate, NSURLQuarantinePropertiesKey, NSURLTagNamesKey, kMDItemFinderComment, kMDItemFlashOnOff, NSURLIsPurgeableKey, kMDLabelIconUUID, NSURLVolumeTotalCapacityKey, _kMDItemUserTags, kMDItemProjects, kMDItemWhiteBalance, kMDLabelKindVisibilityKey, kMDItemAppleLoopDescriptors, kMDItemStateOrProvince, NSURLVolumeURLKey, NSURLUbiquitousItemIsUploadedKey, NSURLUbiquitousItemHasUnresolvedConflictsKey, kMDItemAperture, NSURLUbiquitousSharedItemOwnerNameComponentsKey, NSURLCreationDateKey, kMDItemIsApplicationManaged, kMDLabelVisibility, kMDItemDescription, kMDLabelLocalDomain, kMDItemKeySignature, kMDItemPath

**Finder Metadata**
| Field | Description                                                          |
| ---- | -------------------------------------------------------------------- |
| {finder} | Get metadata managed by macOS Finder such as tags and comments; use in form '{finder:SUBFIELD}', e.g. '{finder:tags}' |


`{finder}` provides access to Finder metadata; available only on macOS. It must be used in the form `{finder:SUBFIELD}` 
where SUBFIELD is one of the following:

| Subfield | Description            |
| -------- | ---------------------- |
| tags     | Finder tags (keywords) |
| comment  | Finder comment         |


<!-- [[[end]]] -->

## Additional Notes

More information on the supported metadata fields can be found at Apple's developer site:

* [Common Metadata Attributes](https://developer.apple.com/documentation/coreservices/file_metadata/mditem/common_metadata_attribute_keys?language=objc)
* [Image Metadata Attributes](https://developer.apple.com/documentation/coreservices/file_metadata/mditem/image_metadata_attribute_keys?language=objc)
* [Video Metadata Attributes](https://developer.apple.com/documentation/coreservices/file_metadata/mditem/video_metadata_attribute_keys?language=objc)
* [Audio Metadata Attributes](https://developer.apple.com/documentation/coreservices/file_metadata/mditem/audio_metadata_attribute_keys?language=objc)
* [File System Metadata Attributes](https://developer.apple.com/documentation/coreservices/file_metadata/mditem/file_system_metadata_attribute_keys?language=objc)
* [NSURL Resource Keys](https://developer.apple.com/documentation/foundation/nsurlresourcekey?language=objc)

## Testing

Tested on Ubuntu Linux and macOS Ventura using Python 3.9, 3.10, and 3.11.

## Contributing

Contributions of all kinds welcome. Please see [README_DEV.md](README_DEV.md) for more notes on the development environment and tooling.
