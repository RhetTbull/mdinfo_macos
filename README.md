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

NSURLAddedToDirectoryDateKey, NSURLApplicationIsScriptableKey, NSURLAttributeModificationDateKey, NSURLCanonicalPathKey, NSURLContentAccessDateKey, NSURLContentModificationDateKey, NSURLContentTypeKey, NSURLCreationDateKey, NSURLCustomIconKey, NSURLDocumentIdentifierKey, NSURLEffectiveIconKey, NSURLFileAllocatedSizeKey, NSURLFileContentIdentifierKey, NSURLFileProtectionKey, NSURLFileResourceIdentifierKey, NSURLFileResourceTypeKey, NSURLFileSecurityKey, NSURLFileSizeKey, NSURLGenerationIdentifierKey, NSURLHasHiddenExtensionKey, NSURLIsAliasFileKey, NSURLIsApplicationKey, NSURLIsDirectoryKey, NSURLIsExcludedFromBackupKey, NSURLIsExecutableKey, NSURLIsHiddenKey, NSURLIsMountTriggerKey, NSURLIsPackageKey, NSURLIsPurgeableKey, NSURLIsReadableKey, NSURLIsRegularFileKey, NSURLIsSparseKey, NSURLIsSymbolicLinkKey, NSURLIsSystemImmutableKey, NSURLIsUbiquitousItemKey, NSURLIsUserImmutableKey, NSURLIsVolumeKey, NSURLIsWritableKey, NSURLKeysOfUnsetValuesKey, NSURLLabelColorKey, NSURLLabelNumberKey, NSURLLinkCountKey, NSURLLocalizedLabelKey, NSURLLocalizedNameKey, NSURLMayHaveExtendedAttributesKey, NSURLMayShareFileContentKey, NSURLNameKey, NSURLParentDirectoryURLKey, NSURLPathKey, NSURLPreferredIOBlockSizeKey, NSURLQuarantinePropertiesKey, NSURLTagNamesKey, NSURLTotalFileAllocatedSizeKey, NSURLTotalFileSizeKey, NSURLUbiquitousItemContainerDisplayNameKey, NSURLUbiquitousItemDownloadRequestedKey, NSURLUbiquitousItemDownloadingErrorKey, NSURLUbiquitousItemDownloadingStatusKey, NSURLUbiquitousItemHasUnresolvedConflictsKey, NSURLUbiquitousItemIsDownloadingKey, NSURLUbiquitousItemIsExcludedFromSyncKey, NSURLUbiquitousItemIsSharedKey, NSURLUbiquitousItemIsUploadedKey, NSURLUbiquitousItemIsUploadingKey, NSURLUbiquitousItemUploadingErrorKey, NSURLUbiquitousSharedItemCurrentUserPermissionsKey, NSURLUbiquitousSharedItemCurrentUserRoleKey, NSURLUbiquitousSharedItemMostRecentEditorNameComponentsKey, NSURLUbiquitousSharedItemOwnerNameComponentsKey, NSURLVolumeAvailableCapacityForImportantUsageKey, NSURLVolumeAvailableCapacityForOpportunisticUsageKey, NSURLVolumeAvailableCapacityKey, NSURLVolumeCreationDateKey, NSURLVolumeIdentifierKey, NSURLVolumeIsAutomountedKey, NSURLVolumeIsBrowsableKey, NSURLVolumeIsEjectableKey, NSURLVolumeIsEncryptedKey, NSURLVolumeIsInternalKey, NSURLVolumeIsJournalingKey, NSURLVolumeIsLocalKey, NSURLVolumeIsReadOnlyKey, NSURLVolumeIsRemovableKey, NSURLVolumeIsRootFileSystemKey, NSURLVolumeLocalizedFormatDescriptionKey, NSURLVolumeLocalizedNameKey, NSURLVolumeMaximumFileSizeKey, NSURLVolumeNameKey, NSURLVolumeResourceCountKey, NSURLVolumeSupportsAccessPermissionsKey, NSURLVolumeSupportsAdvisoryFileLockingKey, NSURLVolumeSupportsCasePreservedNamesKey, NSURLVolumeSupportsCaseSensitiveNamesKey, NSURLVolumeSupportsCompressionKey, NSURLVolumeSupportsExclusiveRenamingKey, NSURLVolumeSupportsExtendedSecurityKey, NSURLVolumeSupportsFileCloningKey, NSURLVolumeSupportsFileProtectionKey, NSURLVolumeSupportsHardLinksKey, NSURLVolumeSupportsImmutableFilesKey, NSURLVolumeSupportsJournalingKey, NSURLVolumeSupportsPersistentIDsKey, NSURLVolumeSupportsRenamingKey, NSURLVolumeSupportsRootDirectoryDatesKey, NSURLVolumeSupportsSparseFilesKey, NSURLVolumeSupportsSwapRenamingKey, NSURLVolumeSupportsSymbolicLinksKey, NSURLVolumeSupportsVolumeSizesKey, NSURLVolumeSupportsZeroRunsKey, NSURLVolumeTotalCapacityKey, NSURLVolumeURLForRemountingKey, NSURLVolumeURLKey, NSURLVolumeUUIDStringKey, _kMDItemUserTags, com.apple.FinderInfo, findercolor, kMDItemAcquisitionMake, kMDItemAcquisitionModel, kMDItemAlbum, kMDItemAltitude, kMDItemAperture, kMDItemAppleLoopDescriptors, kMDItemAppleLoopsKeyFilterType, kMDItemAppleLoopsLoopMode, kMDItemAppleLoopsRootKey, kMDItemApplicationCategories, kMDItemAttributeChangeDate, kMDItemAudiences, kMDItemAudioBitRate, kMDItemAudioChannelCount, kMDItemAudioEncodingApplication, kMDItemAudioSampleRate, kMDItemAudioTrackNumber, kMDItemAuthorAddresses, kMDItemAuthorEmailAddresses, kMDItemAuthors, kMDItemBitsPerSample, kMDItemCFBundleIdentifier, kMDItemCameraOwner, kMDItemCity, kMDItemCodecs, kMDItemColorSpace, kMDItemComment, kMDItemComposer, kMDItemContactKeywords, kMDItemContentCreationDate, kMDItemContentModificationDate, kMDItemContentType, kMDItemContentTypeTree, kMDItemContributors, kMDItemCopyright, kMDItemCountry, kMDItemCoverage, kMDItemCreator, kMDItemDateAdded, kMDItemDeliveryType, kMDItemDescription, kMDItemDirector, kMDItemDisplayName, kMDItemDownloadedDate, kMDItemDueDate, kMDItemDurationSeconds, kMDItemEXIFGPSVersion, kMDItemEXIFVersion, kMDItemEditors, kMDItemEmailAddresses, kMDItemEncodingApplications, kMDItemExecutableArchitectures, kMDItemExecutablePlatform, kMDItemExposureMode, kMDItemExposureProgram, kMDItemExposureTimeSeconds, kMDItemExposureTimeString, kMDItemFNumber, kMDItemFSContentChangeDate, kMDItemFSCreationDate, kMDItemFSHasCustomIcon, kMDItemFSInvisible, kMDItemFSIsExtensionHidden, kMDItemFSIsStationery, kMDItemFSLabel, kMDItemFSName, kMDItemFSNodeCount, kMDItemFSOwnerGroupID, kMDItemFSOwnerUserID, kMDItemFSSize, kMDItemFinderComment, kMDItemFlashOnOff, kMDItemFocalLength, kMDItemFocalLength35mm, kMDItemFonts, kMDItemGPSAreaInformation, kMDItemGPSDOP, kMDItemGPSDateStamp, kMDItemGPSDestBearing, kMDItemGPSDestDistance, kMDItemGPSDestLatitude, kMDItemGPSDestLongitude, kMDItemGPSDifferental, kMDItemGPSMapDatum, kMDItemGPSMeasureMode, kMDItemGPSProcessingMethod, kMDItemGPSStatus, kMDItemGPSTrack, kMDItemGenre, kMDItemHTMLContent, kMDItemHasAlphaChannel, kMDItemHeadline, kMDItemISOSpeed, kMDItemIdentifier, kMDItemImageDirection, kMDItemInformation, kMDItemInstantMessageAddresses, kMDItemInstructions, kMDItemIsApplicationManaged, kMDItemIsGeneralMIDISequence, kMDItemIsLikelyJunk, kMDItemKeySignature, kMDItemKeywords, kMDItemKind, kMDItemLanguages, kMDItemLastUsedDate, kMDItemLatitude, kMDItemLayerNames, kMDItemLensModel, kMDItemLongitude, kMDItemLyricist, kMDItemMaxAperture, kMDItemMediaTypes, kMDItemMeteringMode, kMDItemMusicalGenre, kMDItemMusicalInstrumentCategory, kMDItemMusicalInstrumentName, kMDItemNamedLocation, kMDItemNumberOfPages, kMDItemOrganizations, kMDItemOrientation, kMDItemOriginalFormat, kMDItemOriginalSource, kMDItemPageHeight, kMDItemPageWidth, kMDItemParticipants, kMDItemPath, kMDItemPerformers, kMDItemPhoneNumbers, kMDItemPixelCount, kMDItemPixelHeight, kMDItemPixelWidth, kMDItemProducer, kMDItemProfileName, kMDItemProjects, kMDItemPublishers, kMDItemRecipientAddresses, kMDItemRecipientEmailAddresses, kMDItemRecipients, kMDItemRecordingDate, kMDItemRecordingYear, kMDItemRedEyeOnOff, kMDItemResolutionHeightDPI, kMDItemResolutionWidthDPI, kMDItemRights, kMDItemSecurityMethod, kMDItemSpeed, kMDItemStarRating, kMDItemStateOrProvince, kMDItemStreamable, kMDItemSubject, kMDItemTempo, kMDItemTextContent, kMDItemTheme, kMDItemTimeSignature, kMDItemTimestamp, kMDItemTitle, kMDItemTotalBitRate, kMDItemURL, kMDItemVersion, kMDItemVideoBitRate, kMDItemWhereFroms, kMDItemWhiteBalance, kMDLabelAddedNotification, kMDLabelBundleURL, kMDLabelChangedNotification, kMDLabelContentChangeDate, kMDLabelDisplayName, kMDLabelIconData, kMDLabelIconUUID, kMDLabelIsMutuallyExclusiveSetMember, kMDLabelKind, kMDLabelKindIsMutuallyExclusiveSetKey, kMDLabelKindVisibilityKey, kMDLabelLocalDomain, kMDLabelRemovedNotification, kMDLabelSetsFinderColor, kMDLabelUUID, kMDLabelUserDomain, kMDLabelVisibility, kMDPrivateVisibility, kMDPublicVisibility, stationerypad

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

Tested macOS Ventura using Python 3.9, 3.10, and 3.11.

This package requires macOS 10.15 or later. It will not work on other operating systems.

## Contributing

Contributions of all kinds welcome. Please see [README_DEV.md](README_DEV.md) for more notes on the development environment and tooling.
