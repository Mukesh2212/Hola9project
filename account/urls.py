from django.urls import path
from .views import  *
from account.views import *
from django.conf import settings
from . import views  # Import the views module from your app
from django.conf.urls.static import static
urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),
    path('adsby/',userads.as_view(),name='adsby'),
    path('wishlist/',wishlist.as_view(),name='wishlist'),
    path('blogsby/',userblogs.as_view(),name='userblogs'),
    path('updateProfile/',updateProfile1.as_view(),name='update-Profile'),
    path('createFeatured/',createFeatured.as_view(),name='update-createFeatured'),
    path('ordersPyament/',ordersPyament.as_view(),name='update-ordersPyament'),
    path('verifyEmail/',verifyEmail.as_view(),name='update-verifyEmail'),
    path('verifyPhone/',verifyPhone.as_view(),name='update-verifyPhone'),
    path('verifyEmailLogin/',verifyEmailLogin.as_view(),name='update-verifyEmailLogin'),
    path('viewsupdate/', viewsupdate.as_view(),name='viewsupdate'),
    path('updateProfileApi/', updateProfileApi.as_view(),name='updateProfileApi'),
    path('userProfileDetailsApi/', userProfileDetailsApi.as_view(),name='userProfileDetailsApi'),
    path('lastLoginTime', lastLoginTime.as_view(),name='lastLoginTime'),
    path('lastLoginTimeGet', lastLoginTimeGet.as_view(),name='lastLoginTimeGet'),
    path('qrCodeAds', QrCodeAds.as_view(),name='qrCodeAds'),
    path('getQrCodeAds', getQrCodeAds.as_view(),name='getQrCodeAds'),
    # path('reviewSection', reviewSection.as_view(),name='reviewSection'),
    path('trackingTele',TrackingTele.as_view(),name="trackingTele"),
    path('paymentDetails',PaymentDetails.as_view(),name="paymentDetails"),
    path('jobDetails',jobDetails.as_view(),name="jobDetails"),
    path('jobsRequired',jobsRequired.as_view(),name="jobsRequired"),
    path('fullProfile',FullProfile.as_view(),name='FullProfile'),
    path('contactform', EnquiryListCreate.as_view(), name='contactform'),
    path('contacts', ContactListView.as_view(), name='contact-list'),
    # path('loginEmployee/', LoginAPIView.as_view(), name='loginEmployee'),
    # path('detailEmployee/', EmployeeDetailsView.as_view(), name='detailEmployee'),
    # path('employeeprofile/', EmployeeProfileView.as_view(), name='employeeprofile'),
    path('reviewSection/', views.review_section_list, name='reviewSection'),
    path('reviewSection/<int:pk>/', views.review_section_detail, name='reviewdetail'),
    # path('loginprofile/', LoginProfileList.as_view(), name='loginprofile'),

    path('contactenquiry', ContactEnquireAPIView.as_view(), name='contactenquiry'),




]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)