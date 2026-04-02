
    (function() {
    var bs = window.photosBootstrap;

    bs.Weblabs = {"ForesterDeprecation":"T2","CDSNawsMigration":"T1","ShowDPSLearnMoreLink":"T1","ThumbnailService":"T1","YMSPaymentUpdate":"C","SlpHeader":"C","InAppPurchaseLaunchControl":"C","VideoEditorExperience":"C","FtcAutoRenewConsentCheckboxRequired":"T1","Languages":"C","PhotosPrinting":"T1","snapFishHeifHeicSupport":"T1","MFABlockPlanSubs":"C","AIAskPhotosLaunch":"C","ThumbnailServiceForCdsShares":"C","FolderDeletionMitigationDialog":"C","TwoClickCancellation":"C","StorageTermsUpdate":"C","SharedAlbums":"C","Bootstrap":"C","SharedDigitalGreetingCardAppUpsell":"C","IAMBanner":"C","NonMediaView":"C","InAppPurchaseManageStorageSection":"T1","PlayWithPhotos":"C","TrashViewCounts":"C","PSSStorageMigrationLaunch":"T1","FamilyStorageSharing":"T1","InAppPurchaseUpsellTreatment":"C","DevicePersonalizationRefresh":"C","Printing":"T1","GroupsEnabled":"T1","DisableStoryFamilyVaultSharing":"C","InAppPurchase":"C","VoltronThirdPartyPlanData":"C","BanyanStoragePage":"C","OneClickCancelButton":"T1","ImageEditorImprovement":"T1","AppConfigLaunch":"C","StartTokenListChildren":"C","NawsProxy":"C","ReportAbuseCategoryUpdate":"T1","DisableOnboardingSMS":"C","InAppPurchaseDailyPlans":"C","IAMPrintsSidebar":"C","CloudDriveUploadService":"T1","PrintsSideBarShutterflyIntegration":"T1"};

    bs.Features = {
        ...bs.Weblabs,

        featureWeblabMap: {
            // Despite the name, in-app-purchase is specifically for iOS IAP.  This is not a general gate on all IAP.
            'in-app-purchase': '',
            'in-app-purchase-upgrade-treatment': 'AMAZON_PHOTOS_IAP_UPGRADE_TREATMENT_294445',
            'SlpHeader': 'AMAZON_PHOTOS_WEB_SLP_HEADER_1243448',
        },
        
        'autocomplete': true,
        'rename-face': true,
        'no-people-limit': false,
        'people-detail' : true,
        'filterByDay': false,
        'share': false,
        'email-share': true,
        'folder-album': false,
        'merge-people-check-delay': false,
        'merge-people-check-poll': false,
        'changePeopleAvatar': true,
        'changePeopleAvatarPreview': false,
        'trash-auto-purge': true,
        'photos-edit-location': false,
        'naws': true,
        
        'groups': true,
        'printing': true,
        'snapfish-heif-heic-support': true,
        'disable-onboarding-sms': false,
        'cloud-drive-upload-service': true,
        'show-dps-learn-more-link': true,
        
        
        'in-app-purchase': false,
        
        'internal-tools': Boolean(false) || Boolean(false),
        'in-app-purchase-daily-plans': false,
        'in-app-purchase-upgrade-treatment': "C",
        'mfa-block-plans': false,
        'yms-payment-update': false,
        'disable-story-family-vault-sharing': false,
        'voltron-iframe-plan-info': false,
        'manage-storage-section-for-in-app-purchase': true,
        'two-click-cancellation': false,
        'device-personalization-refresh': false,
        'storage-terms-update': false,
        'shared-digital-greeting-card-app-upsell': false,
        'bulk-download-migration': false,
        'banyan-storage-page': false,
        PrintsSideBarShutterflyIntegration: true,
        PrintsSideBarShutterflyOnly: false,
        PrintsSideBarSnapfishOnly: false,
        ShutterflyEarlyMothersDayPromotion: false,
        ShutterflyLateMothersDayPromotion: false
    };

    bs.AccountFeatureResponse = [];

    

    

    

    
    bs.Config = {
            appName: 'horizonte',
            browser: bs.Browser,
            client: bs.Client,
            device: bs.Device,

            locales: ["cs_CZ","de_DE","en_AU","en_CA","en_GB","en_US","es_ES","es_US","fr_CA","fr_FR","it_IT","ja_JP","nl_NL","pl_PL","pt_BR","tr_TR","zh_CN"],
            applicationId: 'YW16bjEuYXBwbGljYXRpb24uMjllMmU2YjgxZDE3NDhjYWIxZjM4MDQwZGZmMjJkYmY',

            urls: {
                baseAppUrl        : "/photos",
                baseWebViewUrl    : "/photos/webview",
                clouddrive        : "/clouddrive",
                manageStorage     : "/photos/storage",
                orderHandler      : "/photos/storage/order",
                billingHistory    : "/gp/your-account/order-history/ref_=photos_yo_new_digital?ie=UTF8&digitalOrders=1&unifiedOrders=0",
                sharedHistory     : "/clouddrive/shared",
                voltron           : "/dppui/pay-select/?preferenceType=AmazonDrive&clientId=clouddrive",
                yms               : "/yourmembershipsandsubscriptions",

                
                apps              : "/photos/apps",
                voice             : "/photos/voice",
                welcome           : "/photos/welcome",
                imageRecognition  : "/photos/imageRecognition",

                help              : "/help/primephotos",
                recognitionHelp   : "/help/primephotos/findpeopleandthings",
                thirdPartyAppsHelp: "/gp/help/customer/display.html?nodeId=201194060",
                manageThirdParty  : "/ap/adam",
                authPortal        : "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=172800&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fphotos%2Fshared%2Fc0DUWYbiQp-l29Y1XNeONw.Y0iSRUBZHsJhWSOUngm5OB&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=amzn_photos_web_us&openid.mode=checkid_setup&language=en_US&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0",
                switchAccounts    : "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fphotos%2Fshared%2Fc0DUWYbiQp-l29Y1XNeONw.Y0iSRUBZHsJhWSOUngm5OB&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=amzn_photos_web_us&openid.mode=checkid_setup&language=en_US&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&switch_account=picker&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0",

                
                dashboard         : "/dashboard",
                all               : "/all",
                askPhotos         : "/ask",
                search            : "/search",
                videos            : "/videos",
                familyArchive     : "/family",
                folderView        : "/folders",
                nonMediaView      : "/non-media",
                groups            : '/groups',
                groupShare        : '/groups/share',
                people            : "/people",
                stories           : "/stories",
                editFaces         : "/tags",         
                places            : "/places",
                settings          : "/settings",
                share             : "/share",
                sharedAlbum       : "/shared/album",
                
                shareV2           : "/shared",
                shareList         : "/shares",
                shareListPrevious : "/shares?previousLinks=1",
                blockedContacts   : "/blocked",
                album             : "/album",
                albums            : "/albums",
                invite            : "/invite",
                thisday           : "/thisday",
                trash             : "/trash",
                onboard           : "/onboard",
                hidden            : "/hidden",
                report            : "/report",
                storage           : "/storage",
                familyStorage     : "/family-plan",
                androidSimpleStorage    : "/photos/webview/storage/android/simple",
                androidStorage    : "/photos/webview/storage/android",
                iosStorage        : "/photos/webview/storage?isIOS=true",
                imageRecognitionSettings: "/photos/webview/image-recognition-settings",
                storagePlans      : "/storage/plans",
                cancelPlan        : "/storage/cancel",
                IOSUpgradeInstructions: "/webview/change-ios-plan",
                gallery           : "/gallery",      
                404               : "/404",
                playWithPhotosDiscover    : "/explore",
                playWithPhotosSeedDetail    : "/tag",
                playWithPhotosArtifact   : "/artifact",

                
                cancellationFeedback: "/webview/storage/cancellation-feedback",
                cancellationSurveyLink: "https://amazonexteu.qualtrics.com/jfe/form/SV_eQJiUNZ5rIwWmN0",
                cancellationFeedbackPrivacyLink: "/gp/help/customer/display.html?nodeId=201909010",
                cancellationFeedbackCustomerHelpLink: "/gp/help/customer/display.html?nodeId=201909060",

                
                serviceWorker     : "/photos/sw.js",

                
                
                prints            : "/clouddrive/prints?mgh=1&site=photos",
                printsSignout     : "https://www.amazonprinting.com/photo-gift/logout",
                printingDefaultURL: "https://www.amazonprinting.com/photo-gift/shop",

                printsMarketing   : "/prints",

                chromeLink        : "https://www.google.com/chrome/browser/",
                primeSignupLink   : "/photos/getprime",  
                signout           : "/photos/signout?",
                resignin          : "/photos/signout?",

                
                
                universalAppLink  : "/photos/download",
                desktopLink       : "/photos/download",
                windowsAppLink    : "/photos/download",
                macAppLink        : "/photos/download",
                appDownloadiOS    : "/photos/download",
                appDownloadAndroid: "/photos/download",

                
                appStoreiOS    :  "/photos/appstore/ios",
                appStoreAndroid:  "/photos/appstore/android",

                reportFormLink    : "https://dcupkcmoyuvm5.cloudfront.net/copyright-forms/US+Copyright+Complaint.pdf",
                photosInfoPage    : "/photos/home",
                
                desktopHelpPages  : "https://www.amazon.com/gp/help/customer/display.html?nodeId=202006490",

                feedbackForm: "https://digprjsurvey.amazon.com/csad/contactus/feedback/AmazonPhotos/AmazonPhotosSendFeedbackForm",

                privacyPolicy: "/gp/help/customer/display.html?nodeId=468496",
                termsOfUse: "/gp/help/customer/display.html?nodeId=201376540",
                dataRetentionPolicy: "/gp/help/customer/display.html?nodeId=202146630",
                cookieNotice: "/gp/help/customer/display.html?nodeId=201890250",

                
                cloneServiceEndpoint: 'https://upload-photos.amazon.com/',
                devicePersonalizationServiceEndpoint: '/cdrs/drive/v2/device-personalization',
                driveServiceEndpoint: '/drive/v1/',
                groupsOnboardingEndpoint: '/cdrs/drive/v2/onboarding-context',
                promptoServiceEndpoint: '/cdrs/drive/v2/photosGroups',
                proxyServiceEndpoint: 'https://content-na.drive.amazonaws.com/cdproxy/drive/v1/',
                suliServiceEndpoint: '/cdrs',
                thumbnailServiceEndpoint: 'https://thumbnails-photos.amazon.com/',
                uploadServiceEndpoint: 'https://upload-photos.amazon.com/',
                pssServiceEndpoint: '/cdrs/drive/v2/photos-subscriptions/',
                downloadServiceEndpoint: 'https://download-photos.amazon.com/',
                accountServiceEndpoint: '/cdrs/drive/v2/account',
                inAppMessagesServiceEndpoint: '/cdrs/drive/v2/engagement/inappmessages',
                recordCustomerActionServiceEndpoint: '/cdrs/drive/v2/engagement/actions',
                sharingControlPlaneEndpoint: '/cdrs/drive/v2/photosSharing',
            },

            primeUpsellReftag: '',

            isBeta: Boolean(false),
            isGamma: Boolean(false),
            isProd: Boolean(true),

            isWebView: false,

            isPhoneMaskSupported: Boolean(),
            seenYourDevices: Boolean(),
            hasConnectedMobileDevice: Boolean(),
            hasSeenPersonalizeDevices: Boolean(),
            hasDismissedPrintsAwarenessBanner: Boolean(),

            photoEditorLicense: 'O57PfA4EEvU5BiVsiTA4FZ7o4i0vJ_GoSluCNALSmlH_13lkRSGbHNfS27f899zo',

            uploaderBaseFolder : '/Pictures/Web/',
            accountNearQuotaLimit: Number(524288000),

            routeConfig: {"/photos/webview/storage/android":{"pageType":"AmazonPhotosWebView","subPageType":"AndroidStorageView","viewName":"AndroidStorageView","pageContext":"AndroidStorageView"},"/photos/thisday/:month(\\d+)-:day(\\d+)-:year(\\d+)/gallery/:nodeId":{"pageType":"AmazonPhotos","subPageType":"ThisDayDetailViewSPV","viewName":"ThisDayDetailViewSPV","pageContext":"ThisDayDetailViewSPV"},"/photos/groups/share/:shareToken/add":{"pageType":"AmazonPhotos","subPageType":"GroupShareView","viewName":"GroupShareView","pageContext":"GroupShareView"},"/photos/hidden":{"pageType":"AmazonPhotos","subPageType":"Hidden","viewName":"Hidden","pageContext":"Hidden"},"/photos/albums":{"pageType":"AmazonPhotos","subPageType":"Albums","viewName":"Albums","pageContext":"Albums"},"/photos/settings":{"pageType":"AmazonPhotos","subPageType":"Settings","viewName":"Settings","pageContext":"Settings"},"/photos/groups/:groupId/collections":{"pageType":"AmazonPhotos","subPageType":"GroupDetailView","viewName":"GroupDetailView","pageContext":"GroupDetailView"},"/photos/storage":{"pageType":"AmazonPhotos","subPageType":"Storage","viewName":"Storage","pageContext":"Storage"},"/photos/hidden/:nodeId":{"pageType":"AmazonPhotos","subPageType":"Hidden","viewName":"Hidden","pageContext":"Hidden"},"/photos/shares":{"pageType":"AmazonPhotos","subPageType":"SharesList","viewName":"SharesList","pageContext":"SharesList"},"/photos/folders/:folderId":{"pageType":"AmazonPhotos","subPageType":"FolderView","viewName":"FolderView","pageContext":"FolderView"},"/photos/explore/:tagId/artifact/:seedId":{"pageType":"AmazonPhotos","subPageType":"PlayWithPhotosSeedDetailArtifactView","viewName":"PlayWithPhotosSeedDetailArtifactView","pageContext":"PlayWithPhotosSeedDetailArtifactView"},"/photos/thisday/:month(\\d+)-:day(\\d+)-:year(\\d+)":{"pageType":"AmazonPhotos","subPageType":"ThisDayDetailView","viewName":"ThisDayDetailView","pageContext":"ThisDayDetailView"},"/photos/blocked":{"pageType":"AmazonPhotos","subPageType":"BlockedContacts","viewName":"BlockedContacts","pageContext":"BlockedContacts"},"/photos/groups/:groupId":{"pageType":"AmazonPhotos","subPageType":"GroupDetailView","viewName":"GroupDetailView","pageContext":"GroupDetailView"},"/photos/tools":{"pageType":"AmazonPhotos","subPageType":"InternalTools","viewName":"InternalTools","pageContext":"InternalTools"},"/photos/webview/storage/android/simple":{"pageType":"AmazonPhotosWebView","subPageType":"AndroidSimpleStorageView","viewName":"AndroidSimpleStorageView","pageContext":"AndroidSimpleStorageView"},"/photos":{"pageType":"AmazonPhotos","subPageType":"YourPhotos","viewName":"YourPhotos","pageContext":"YourPhotos"},"/photos/thisday/:year(\\d+)":{"pageType":"AmazonPhotos","subPageType":"ThisDayDetailView","viewName":"ThisDayDetailView","pageContext":"ThisDayDetailView"},"/photos/groups/:groupId/album/:albumId/gallery/:nodeId":{"pageType":"AmazonPhotos","subPageType":"GroupAlbumViewSPV","viewName":"GroupAlbumViewSPV","pageContext":"GroupAlbumViewSPV"},"/photos/share/:shareId":{"pageType":"AmazonPhotos","subPageType":"ShareLanding","viewName":"ShareLanding","pageContext":"ShareLanding"},"/photos/device-personalization":{"pageType":"AmazonPhotos","subPageType":"DeviceList","viewName":"DeviceList","pageContext":"DeviceList"},"/photos/404":{"pageType":"AmazonPhotos","subPageType":"404","viewName":"404","pageContext":"404"},"/photos/all/gallery/:nodeId":{"pageType":"AmazonPhotos","subPageType":"YourPhotosSPV","viewName":"YourPhotosSPV","pageContext":"YourPhotosSPV"},"/photos/groups":{"pageType":"AmazonPhotos","subPageType":"ListGroups","viewName":"ListGroups","pageContext":"ListGroups"},"/photos/people":{"pageType":"AmazonPhotos","subPageType":"People","viewName":"People","pageContext":"People"},"/photos/groups/:groupId/album/:albumId":{"pageType":"AmazonPhotos","subPageType":"GroupAlbumView","viewName":"GroupAlbumView","pageContext":"GroupAlbumView"},"/photos/search/:category/:name/gallery/:nodeId":{"pageType":"AmazonPhotos","subPageType":"SERPSPV","viewName":"SERPSPV","pageContext":"SERPSPV"},"/photos/explore/artifact/:seedId":{"pageType":"AmazonPhotos","subPageType":"PlayWithPhotosDiscoverArtifactView","viewName":"PlayWithPhotosDiscoverArtifactView","pageContext":"PlayWithPhotosDiscoverArtifactView"},"/photos/shares/:groupId":{"pageType":"AmazonPhotos","subPageType":"SharesDetailView","viewName":"SharesDetailView","pageContext":"SharesDetailView"},"/photos/groups/:groupId/collections/:collectionId":{"pageType":"AmazonPhotos","subPageType":"GroupCollectionDetailView","viewName":"GroupCollectionDetailView","pageContext":"GroupCollectionDetailView"},"/photos/groups/:groupId/collections/:collectionId/:nodeId":{"pageType":"AmazonPhotos","subPageType":"GroupCollectionDetailView","viewName":"GroupCollectionDetailView","pageContext":"GroupCollectionDetailView"},"/photos/folders/:folderId/gallery/:nodeId":{"pageType":"AmazonPhotos","subPageType":"FolderViewSPV","viewName":"FolderViewSPV","pageContext":"FolderViewSPV"},"/photos/all":{"pageType":"AmazonPhotos","subPageType":"YourPhotos","viewName":"YourPhotos","pageContext":"YourPhotos"},"/photos/family":{"pageType":"AmazonPhotos","subPageType":"FamilyPhotos","viewName":"FamilyPhotos","pageContext":"FamilyPhotos"},"/photos/webview/change-ios-plan":{"pageType":"AmazonPhotosWebView","subPageType":"IOSIAPStorageUpdate","viewName":"IOSIAPStorageUpdate","pageContext":"IOSIAPStorageUpdate"},"/photos/artifact/:seedId":{"pageType":"AmazonPhotos","subPageType":"YourPhotosPlayWithPhotosArtifactView","viewName":"YourPhotosPlayWithPhotosArtifactView","pageContext":"YourPhotosPlayWithPhotosArtifactView"},"/photos/places/:locationId/gallery/:nodeId":{"pageType":"AmazonPhotos","subPageType":"PlaceDetailViewSPV","viewName":"PlaceDetailViewSPV","pageContext":"PlaceDetailViewSPV"},"/photos/folders/gallery/:nodeId":{"pageType":"AmazonPhotos","subPageType":"FolderViewSPV","viewName":"FolderViewSPV","pageContext":"FolderViewSPV"},"/photos/places":{"pageType":"AmazonPhotos","subPageType":"Places","viewName":"Places","pageContext":"Places"},"/photos/report":{"pageType":"AmazonPhotos","subPageType":"ReportAbuseView","viewName":"ReportAbuseView","pageContext":"ReportAbuseView"},"/photos/groups/share/:shareToken/gallery/:nodeId":{"pageType":"AmazonPhotos","subPageType":"GroupShareViewSPV","viewName":"GroupShareViewSPV","pageContext":"GroupShareViewSPV"},"/photos/people/:clusterId/gallery/:nodeId":{"pageType":"AmazonPhotos","subPageType":"PeopleDetailViewSPV","viewName":"PeopleDetailViewSPV","pageContext":"PeopleDetailViewSPV"},"/photos/trash":{"pageType":"AmazonPhotos","subPageType":"Trash","viewName":"Trash","pageContext":"Trash"},"/photos/explore/tag/:tagId":{"pageType":"AmazonPhotos","subPageType":"PlayWithPhotosSeedDetail","viewName":"PlayWithPhotosSeedDetail","pageContext":"PlayWithPhotosSeedDetail"},"/photos/folders":{"pageType":"AmazonPhotos","subPageType":"FolderView","viewName":"FolderView","pageContext":"FolderView"},"/photos/groups/share/:shareToken/join":{"pageType":"AmazonPhotos","subPageType":"GroupShareView","viewName":"GroupShareView","pageContext":"GroupShareView"},"/photos/search/:category/:name":{"pageType":"AmazonPhotos","subPageType":"SERP","viewName":"SERP","pageContext":"SERP"},"/photos/ref\u003d:refTag":{"pageType":"AmazonPhotos","subPageType":"YourPhotos","viewName":"YourPhotos","pageContext":"YourPhotos"},"/photos/printing/select":{"pageType":"AmazonPhotosPrinting","subPageType":"PrintingSelect","viewName":"PrintingSelect","pageContext":"PrintingSelect"},"/photos/tools/template-editor":{"pageType":"AmazonPhotos","subPageType":"TemplateEditor","viewName":"TemplateEditor","pageContext":"TemplateEditor"},"/photos/webview/storage/plans":{"pageType":"AmazonPhotosWebView","subPageType":"StoragePlansView","viewName":"StoragePlansView","pageContext":"StoragePlansView"},"/photos/webview/upgrade":{"pageType":"AmazonPhotosWebView","subPageType":"UpgradeStorageWebView","viewName":"UpgradeStorageWebView","pageContext":"UpgradeStorageWebView"},"/photos/webview/ios-storage":{"pageType":"AmazonPhotosWebView","subPageType":"IosStorageSettingsView","viewName":"IosStorageSettingsView","pageContext":"IosStorageSettingsView"},"/photos/webview/storage/cancel":{"pageType":"AmazonPhotosWebView","subPageType":"StorageCancelView","viewName":"StorageCancelView","pageContext":"StorageCancelView"},"/photos/device-personalization/:deviceAccount":{"pageType":"AmazonPhotos","subPageType":"DeviceDetail","viewName":"DeviceDetail","pageContext":"DeviceDetail"},"/photos/thisday/:month(\\d+)-:day(\\d+)":{"pageType":"AmazonPhotos","subPageType":"ThisDayDetailView","viewName":"ThisDayDetailView","pageContext":"ThisDayDetailView"},"/photos/groups/share/:shareToken":{"pageType":"AmazonPhotos","subPageType":"GroupShareView","viewName":"GroupShareView","pageContext":"GroupShareView"},"/photos/album/:albumId/gallery/:nodeId":{"pageType":"AmazonPhotos","subPageType":"AlbumDetailViewSPV","viewName":"AlbumDetailViewSPV","pageContext":"AlbumDetailViewSPV"},"/photos/non-media":{"pageType":"AmazonPhotos","subPageType":"NonMediaView","viewName":"NonMediaView","pageContext":"NonMediaView"},"/photos/webview/storage":{"pageType":"AmazonPhotosWebView","subPageType":"MobileStorageView","viewName":"MobileStorageView","pageContext":"MobileStorageView"},"/photos/webview/image-recognition-settings":{"pageType":"AmazonPhotosWebView","subPageType":"ImageRecognitionSettingsView","viewName":"ImageRecognitionSettingsView","pageContext":"ImageRecognitionSettingsView"},"/photos/welcome":{"pageType":"AmazonPhotos","subPageType":"Welcome","viewName":"Welcome","pageContext":"Welcome"},"/photos/people/:clusterId":{"pageType":"AmazonPhotos","subPageType":"PeopleDetailView","viewName":"PeopleDetailView","pageContext":"PeopleDetailView"},"/photos/shared/album/:sharedAlbumToken/gallery/:nodeId":{"pageType":"AmazonPhotos","subPageType":"SharedAlbumLandingSPV","viewName":"SharedAlbumLandingSPV","pageContext":"SharedAlbumLandingSPV"},"/photos/stories":{"pageType":"AmazonPhotos","subPageType":"Stories","viewName":"Stories","pageContext":"Stories"},"/photos/shared/album/:sharedAlbumToken":{"pageType":"AmazonPhotos","subPageType":"SharedAlbumLanding","viewName":"SharedAlbumLanding","pageContext":"SharedAlbumLanding"},"/photos/stories/:nodeId":{"pageType":"AmazonPhotos","subPageType":"StoriesSPV","viewName":"StoriesSPV","pageContext":"StoriesSPV"},"/photos/family/gallery/:nodeId":{"pageType":"AmazonPhotos","subPageType":"FamilyPhotosSPV","viewName":"FamilyPhotosSPV","pageContext":"FamilyPhotosSPV"},"/photos/webview/getapps":{"pageType":"AmazonPhotosWebView","subPageType":"GetAppsView","viewName":"GetAppsView","pageContext":"GetAppsView"},"/photos/ask":{"pageType":"AmazonPhotos","subPageType":"AskPhotos","viewName":"AskPhotos","pageContext":"AskPhotos"},"/photos/explore":{"pageType":"AmazonPhotos","subPageType":"PlayWithPhotosDiscover","viewName":"PlayWithPhotosDiscover","pageContext":"PlayWithPhotosDiscover"},"/photos/shared/:shareToken/gallery/:nodeId":{"pageType":"AmazonPhotos","subPageType":"SharedLandingSPV","viewName":"SharedLandingSPV","pageContext":"SharedLandingSPV"},"/photos/shared/:shareToken":{"pageType":"AmazonPhotos","subPageType":"SharedLanding","viewName":"SharedLanding","pageContext":"SharedLanding"},"/photos/album/:albumId":{"pageType":"AmazonPhotos","subPageType":"AlbumDetailView","viewName":"AlbumDetailView","pageContext":"AlbumDetailView"},"/photos/thisday/:year(\\d+)/gallery/:nodeId":{"pageType":"AmazonPhotos","subPageType":"ThisDayDetailViewSPV","viewName":"ThisDayDetailViewSPV","pageContext":"ThisDayDetailViewSPV"},"/photos/family-plan":{"pageType":"AmazonPhotos","subPageType":"FamilyStorage","viewName":"FamilyStorage","pageContext":"FamilyStorage"},"/photos/storage/plans":{"pageType":"AmazonPhotos","subPageType":"StoragePlans","viewName":"StoragePlans","pageContext":"StoragePlans"},"/photos/share/:shareId/gallery/:nodeId":{"pageType":"AmazonPhotos","subPageType":"ShareLandingSPV","viewName":"ShareLandingSPV","pageContext":"ShareLandingSPV"},"/photos/storage/cancel":{"pageType":"AmazonPhotos","subPageType":"StorageCancel","viewName":"StorageCancel","pageContext":"StorageCancel"},"/photos/thisday":{"pageType":"AmazonPhotos","subPageType":"ThisDay","viewName":"ThisDay","pageContext":"ThisDay"},"/photos/places/:locationId":{"pageType":"AmazonPhotos","subPageType":"PlaceDetailView","viewName":"PlaceDetailView","pageContext":"PlaceDetailView"},"/photos/tools/icon-previews":{"pageType":"AmazonPhotos","subPageType":"IconPreviews","viewName":"IconPreviews","pageContext":"IconPreviews"},"/photos/groups/:groupId/gallery/:nodeId":{"pageType":"AmazonPhotos","subPageType":"GroupDetailViewSPV","viewName":"GroupDetailViewSPV","pageContext":"GroupDetailViewSPV"},"/photos/webview/storage/cancellation-feedback":{"pageType":"AmazonPhotosWebView","subPageType":"CancellationFeedbackView","viewName":"CancellationFeedbackView","pageContext":"CancellationFeedbackView"}},
            
            emailRegex: /\w+([-+.']\w+)*[-+']*@\w+([-.]\w+)*\.\w+([-.]\w+)*/,
            metrics: {
                pageType: 'AmazonPhotos',
                
                forester: {
                    API_VERSION     : '1',
                    CHANNEL_ID      : 'clouddrive-photos',
                    CHANNEL_VERSION : '1',
                    EMPTY_ACTION    : 'OE',
                    IMAGE_ACTION    : 'OP',
                    TEXT_ACTION     : 'TOP',
                    DOMAIN          : 'fls-na.amazon.com'
                },
                sushi: {
                    endpoint:'https://unagi-na.amazon.com/1/events/com.amazon.photos.bi.metrics.web.prod'
                }
            }
        };
    })();
