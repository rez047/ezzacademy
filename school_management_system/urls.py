from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.views.static import serve 

from school_management_app import views, HodViews, StaffViews, StudentViews, ParentViews, AccountViews
from school_management_app.EditResultVIewClass import EditResultViewClass, UpdateSelectedResultView
from school_management_system import settings
from school_management_app.HodViews import  InvoiceListView, createInvoice, generate_PDF, view_PDF
from school_management_app.views import bulk_upload, success_page
# handler404 = 'school_management_app.views.error_404'

urlpatterns = [
    path('signup_admin',views.signup_admin,name="signup_admin"),
    path('signup_student',views.signup_student,name="signup_student"),
    path('signup_staff',views.signup_staff,name="signup_staff"),
    path('do_admin_signup',views.do_admin_signup,name="do_admin_signup"),
    path('do_staff_signup',views.do_staff_signup,name="do_staff_signup"),
    path('do_signup_student',views.do_signup_student,name="do_signup_student"),
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('',views.ShowLoginPage,name="show_login"),
    path('get_user_details', views.GetUserDetails),
    path('logout_user', views.logout_user,name="logout"),
    path('doLogin',views.doLogin,name="do_login"),
    path('admin_home',HodViews.admin_home,name="admin_home"),
    path('add_staff',HodViews.add_staff,name="add_staff"),
    path('add_staff_save',HodViews.add_staff_save,name="add_staff_save"),
    path('add_account',HodViews.add_account,name="add_account"),
    path('add_account_save',HodViews.add_account_save,name="add_account_save"),
    path('add_parent',HodViews.add_parent,name="add_parent"),
    path('add_parent_save',HodViews.add_parent_save,name="add_parent_save"),
    path('edit_parent/<str:parent_id>', HodViews.edit_parent,name="edit_parent"),
    path('edit_parent_save', HodViews.edit_parent_save,name="edit_parent_Save"),
    path('delete_parent/<str:parent_id>', HodViews.delete_parent,name="delete_parent"),
    path('add_course/', HodViews.add_course,name="add_course"),
    path('add_course_save', HodViews.add_course_save,name="add_course_save"),
    path('add_student', HodViews.add_student,name="add_student"),
    path('add_student_save', HodViews.add_student_save,name="add_student_save"),
    path('add_subject', HodViews.add_subject,name="add_subject"),
    path('add_subject_save', HodViews.add_subject_save,name="add_subject_save"),
    path('manage_staff', HodViews.manage_staff,name="manage_staff"),
    path('manage_account', HodViews.manage_account,name="manage_account"),
    path('manage_parent', HodViews.manage_parent,name="manage_parent"),
    path('manage_student', HodViews.manage_student,name="manage_student"),
    path('manage_course', HodViews.manage_course,name="manage_course"),
    path('manage_subject', HodViews.manage_subject,name="manage_subject"),
    path('edit_staff/<str:staff_id>', HodViews.edit_staff,name="edit_staff"),
    path('edit_staff_save', HodViews.edit_staff_save,name="edit_staff_save"),
    path('delete_staff/<str:staff_id>', HodViews.delete_staff,name="delete_staff"),
    path('edit_account/<str:account_id>', HodViews.edit_account,name="account"),
    path('edit_account_save', HodViews.edit_account_save,name="edit_account_save"),
    path('delete_account/<str:account_id>', HodViews.delete_account,name="delete_account"),
    path('edit_student/<str:student_id>', HodViews.edit_student,name="edit_student"),
    path('edit_student_save', HodViews.edit_student_save,name="edit_student_save"),
    path('delete_student/<str:student_id>', HodViews.delete_student,name="delete_student"),
    path('edit_subject/<str:subject_id>', HodViews.edit_subject,name="edit_subject"),
    path('edit_subject_save', HodViews.edit_subject_save,name="edit_subject_save"),
    path('delete_subject/<str:subject_id>', HodViews.delete_subject,name="delete_subject"),
    path('edit_course/<str:course_id>', HodViews.edit_course,name="edit_course"),
    path('edit_course_save', HodViews.edit_course_save,name="edit_course_save"),
    path('delete_course/<str:course_id>', HodViews.delete_course,name="delete_course"),
    path('manage_session', HodViews.manage_session,name="manage_session"),
    path('add_session', HodViews.add_session,name="add_session"),
    path('add_session_save', HodViews.add_session_save,name="add_session_save"),
    path('edit_session_save/<str:session_id>', HodViews.edit_session_save,name="edit_session_save"),
    path('edit_session/<str:session_id>', HodViews.edit_session,name="edit_session"),
    path('delete_session/<str:session_id>', HodViews.delete_session,name="delete_session"),
    path('check_email_exist', HodViews.check_email_exist,name="check_email_exist"),
    path('check_username_exist', HodViews.check_username_exist,name="check_username_exist"),
    path('student_feedback_message', HodViews.student_feedback_message,name="student_feedback_message"),
    path('account_feedback_message', HodViews.account_feedback_message,name="account_feedback_message"),
    path('parent_feedback_message', HodViews.parent_feedback_message,name="parent_feedback_message"),
    path('student_feedback_message_replied', HodViews.student_feedback_message_replied,name="student_feedback_message_replied"),
    path('account_feedback_message_replied', HodViews.account_feedback_message_replied,name="account_feedback_message_replied"),
    path('parent_feedback_message_replied', HodViews.parent_feedback_message_replied,name="parent_feedback_message_replied"),
    path('staff_feedback_message', HodViews.staff_feedback_message,name="staff_feedback_message"),
    path('staff_feedback_message_replied', HodViews.staff_feedback_message_replied,name="staff_feedback_message_replied"),
    path('student_leave_view', HodViews.student_leave_view,name="student_leave_view"),
    path('staff_leave_view', HodViews.staff_leave_view,name="staff_leave_view"),
    path('account_leave_view', HodViews.account_leave_view,name="account_leave_view"),
    path('student_approve_leave/<str:leave_id>', HodViews.student_approve_leave,name="student_approve_leave"),
    path('student_disapprove_leave/<str:leave_id>', HodViews.student_disapprove_leave,name="student_disapprove_leave"),
    path('staff_disapprove_leave/<str:leave_id>', HodViews.staff_disapprove_leave,name="staff_disapprove_leave"),
    path('staff_approve_leave/<str:leave_id>', HodViews.staff_approve_leave,name="staff_approve_leave"),
    path('account_disapprove_leave/<str:leave_id>', HodViews.account_disapprove_leave,name="account_disapprove_leave"),
    path('account_approve_leave/<str:leave_id>', HodViews.account_approve_leave,name="account_approve_leave"),
    path('admin_view_attendance', HodViews.admin_view_attendance,name="admin_view_attendance"),
    path('admin_get_attendance_dates', HodViews.admin_get_attendance_dates,name="admin_get_attendance_dates"),
    path('admin_get_attendance_student', HodViews.admin_get_attendance_student,name="admin_get_attendance_student"),
    path('admin_profile', HodViews.admin_profile,name="admin_profile"),
    path('admin_profile_save', HodViews.admin_profile_save,name="admin_profile_save"),
    path('admin_send_notification_staff', HodViews.admin_send_notification_staff,name="admin_send_notification_staff"),
    path('admin_send_notification_account', HodViews.admin_send_notification_account,name="admin_send_notification_account"),
    path('delete_account_notifications/<str:id>', HodViews.delete_account_notifications,name="delete_account_notifications"),
    path('delete_staff_notifications/<str:id>', HodViews.delete_staff_notifications,name="delete_staff_notifications"),
    path('admin_send_notification_student', HodViews.admin_send_notification_student,name="admin_send_notification_student"),
    path('delete_student_notifications/<str:id>', HodViews.delete_student_notifications,name="delete_student_notifications"),
    path('admin_send_notification_parent', HodViews.admin_send_notification_parent,name="admin_send_notification_parent"),
    path('delete_parent_notifications/<str:id>', HodViews.delete_parent_notifications,name="delete_parent_notifications"),
    path('send_student_notification', HodViews.send_student_notification,name="send_student_notification"),
    path('send_staff_notification', HodViews.send_staff_notification,name="send_staff_notification"),
    path('send_account_notification', HodViews.send_account_notification,name="send_account_notification"),
    path('send_parent_notification', HodViews.send_parent_notification,name="send_parent_notification"),
    path('manage_student_news', HodViews.manage_news,name="manage_news"),
    path('manage_account_news', HodViews.manage_anews,name="manage_anews"),
    path('manage_parent_news', HodViews.manage_pnews,name="manage_pnews"),
    path('add_student_news',HodViews.add_news,name="add_news"),
    path('add_parent_news',HodViews.add_pnews,name="add_pnews"),
    path('add_account_news',HodViews.add_anews,name="add_anews"),
    path('add_student_news_save',HodViews.add_news_save,name="add_news_save"),
    path('add_parent_news_save',HodViews.add_pnews_save,name="add_pnews_save"),
    path('add_account_news_save',HodViews.add_anews_save,name="add_anews_save"),
    path('edit_student_news/<str:news_id>', HodViews.edit_news,name="edit_news"),
    path('edit_student_news_save', HodViews.edit_news_save,name="edit_news_save"),
    path('delete_student_news/<str:news_id>', HodViews.delete_news,name="delete_news"),
    path('view_student_news/<str:news_id>', HodViews.view_news,name="view_news"),
    path('view_parent_news/<str:news_id>', HodViews.view_pnews,name="view_pnews"),
    path('edit_parent_news/<str:news_id>', HodViews.edit_pnews,name="edit_pnews"),
    path('edit_parent_news_save', HodViews.edit_pnews_save,name="edit_pnews_save"),
    path('delete_parent_news/<str:news_id>', HodViews.delete_pnews,name="delete_pnews"),
    path('view_account_news/<str:news_id>', HodViews.view_anews,name="view_anews"),
    path('edit_account_news/<str:news_id>', HodViews.edit_anews,name="edit_anews"),
    path('edit_account_news_save', HodViews.edit_anews_save,name="edit_anews_save"),
    path('delete_account_news/<str:news_id>', HodViews.delete_anews,name="delete_anews"),
    path('covid19', HodViews.covid19,name="covid19"),
    path('manage_teacher_news', HodViews.manage_tnews,name="manage_tnews"),
    path('add_teacher_news',HodViews.add_tnews,name="add_tnews"),
    path('add_teacher_news_save',HodViews.add_tnews_save,name="add_tnews_save"),
    path('edit_teacher_news/<str:news_id>', HodViews.edit_tnews,name="edit_tnews"),
    path('edit_teacher_news_save', HodViews.edit_tnews_save,name="edit_tnews_save"),
    path('delete_teacher_news/<str:news_id>', HodViews.delete_tnews,name="delete_tnews"),
    path('view_teacher_news/<str:news_id>', HodViews.view_tnews,name="view_tnews"),
    path('view_teacher_news_comment_save', HodViews.view_staff_news_comment_save, name="view_staff_news_comment_save"),
    path('view_teacher_news_comment_edit_save', HodViews.view_staff_news_comment_edit_save, name="view_staff_news_comment_edit_save"),
    path('delete_teacher_comment/<str:news_id>/<str:comment_id>', HodViews.delete_tcomment, name="delete_tcomment"),
    path('view_student_news_comment_save', HodViews.view_student_news_comment_save, name="view_student_news_comment_save"),
    path('view_student_news_comment_edit_save', HodViews.view_student_news_comment_edit_save, name="view_student_news_comment_edit_save"),
    path('delete_student_comment/<str:news_id>/<str:comment_id>', HodViews.delete_scomment, name="delete_scomment"),
    path('view_account_news_comment_save', HodViews.view_account_news_comment_save, name="view_account_news_comment_save"),
    path('view_account_news_comment_edit_save', HodViews.view_account_news_comment_edit_save, name="view_account_news_comment_edit_save"),
    path('delete_account_comment/<str:news_id>/<str:comment_id>', HodViews.delete_acomment, name="delete_acomment"),
    path('view_parent_news_comment_save', HodViews.view_parent_news_comment_save, name="view_parent_news_comment_save"),
    path('view_parent_news_comment_edit_save', HodViews.view_parent_news_comment_edit_save, name="view_parent_news_comment_edit_save"),
    path('delete_parent_comment/<str:news_id>/<str:comment_id>', HodViews.delete_pcomment, name="delete_pcomment"),
    path('manage_invoice', InvoiceListView.as_view(), name="manage_invoice"),
    path('create/', createInvoice, name="invoice_create"),
    path('invoice-detail/<id>', view_PDF, name='invoice_detail'),
    path('invoice-download/<id>', generate_PDF, name='invoice_download'),
    path('bulk_upload', views.bulk_upload, name='bulk_upload'),
    path('success-page/', views.success_page, name='success_page'),
    path('add_financial_record', HodViews.add_financial_record, name='add_financial_record'),
    path('financial_record_list/', HodViews.financial_record_list, name='financial_record_list'),
    path('generate-receipt/<int:student_id>/', HodViews.generate_receipt_pdf, name='generate_receipt_pdf'),
    path('generate-receipts/<int:student_id>/', HodViews.generate_receipt_pdfs, name='generate_receipt_pdfs'),
    path('account_generate-receipt/<int:student_id>/', AccountViews.account_generate_receipt_pdf, name='account_generate_receipt_pdf'),
    path('account_generate-receipts/<int:student_id>/', AccountViews.account_generate_receipt_pdfs, name='account_generate_receipt_pdfs'),    

    #Staff URL Path
    path('staff_home', StaffViews.staff_home, name="staff_home"),
    path('staff_take_attendance', StaffViews.staff_take_attendance, name="staff_take_attendance"),
    path('staff_update_attendance', StaffViews.staff_update_attendance, name="staff_update_attendance"),
    path('get_students', StaffViews.get_students, name="get_students"),
    path('get_attendance_dates', StaffViews.get_attendance_dates, name="get_attendance_dates"),
    path('get_attendance_student', StaffViews.get_attendance_student, name="get_attendance_student"),
    path('save_attendance_data', StaffViews.save_attendance_data, name="save_attendance_data"),
    path('save_updateattendance_data', StaffViews.save_updateattendance_data, name="save_updateattendance_data"),
    path('staff_apply_leave', StaffViews.staff_apply_leave, name="staff_apply_leave"),
    path('staff_apply_leave_save', StaffViews.staff_apply_leave_save, name="staff_apply_leave_save"),
    path('staff_feedback', StaffViews.staff_feedback, name="staff_feedback"),
    path('staff_feedback_save', StaffViews.staff_feedback_save, name="staff_feedback_save"),
    path('staff_profile', StaffViews.staff_profile, name="staff_profile"),
    path('staff_profile_save', StaffViews.staff_profile_save, name="staff_profile_save"),
    path('staff_fcmtoken_save', StaffViews.staff_fcmtoken_save, name="staff_fcmtoken_save"),
    path('staff_all_notification', StaffViews.staff_all_notification, name="staff_all_notification"),
    path('staff_add_result', StaffViews.staff_add_result, name="staff_add_result"),
    path('save_student_result', StaffViews.save_student_result, name="save_student_result"),
    path('edit_student_result',EditResultViewClass.as_view(), name="edit_student_result"),
    path('fetch_result_student',StaffViews.fetch_result_student, name="fetch_result_student"),
    path('staff_news', StaffViews.staff_news, name="staff_news"),
    path('view_staff_news/<str:news_id>', StaffViews.view_staff_news, name="view_staff_news"),
    path('view_staff_news_comment_save', StaffViews.view_staff_news_comment_save, name="view_staff_news_comment_save"),
    path('view_staff_news_comment_edit_save', StaffViews.view_staff_news_comment_edit_save, name="view_staff_news_comment_edit_save"),
    path('delete_tcomment/<str:news_id>/<str:comment_id>', StaffViews.delete_tcomment, name="delete_tcomment"),
    path('teacher/covid19', StaffViews.tcovid19,name="tcovid19"),
    path('update_selected_result/', UpdateSelectedResultView.as_view(), name='update_selected_result'),


    #Student URL Path
    path('student_home', StudentViews.student_home, name="student_home"),
    path('student_view_attendance', StudentViews.student_view_attendance, name="student_view_attendance"),
    path('student_view_attendance_post', StudentViews.student_view_attendance_post, name="student_view_attendance_post"),
    path('student_apply_leave', StudentViews.student_apply_leave, name="student_apply_leave"),
    path('student_apply_leave_save', StudentViews.student_apply_leave_save, name="student_apply_leave_save"),
    path('student_feedback', StudentViews.student_feedback, name="student_feedback"),
    path('student_feedback_save', StudentViews.student_feedback_save, name="student_feedback_save"),
    path('student_profile', StudentViews.student_profile, name="student_profile"),
    path('student_profile_save', StudentViews.student_profile_save, name="student_profile_save"),
    path('student_fcmtoken_save', StudentViews.student_fcmtoken_save, name="student_fcmtoken_save"),
    path('student_all_notification',StudentViews.student_all_notification,name="student_all_notification"),
    path('student_view_result',StudentViews.student_view_result,name="student_view_result"),
    path('testurl/',views.Testurl),
    path('student_news', StudentViews.student_news, name="student_news"),
    path('student/view_student_news/<str:news_id>', StudentViews.view_student_news, name="view_student_news"),
    path('view_s_news_comment_save', StudentViews.view_student_news_comment_save, name="view_student_news_comment_save"),
    path('view_s_news_comment_edit_save', StudentViews.view_student_news_comment_edit_save, name="view_student_news_comment_edit_save"),
    path('delete_scomment/<str:news_id>/<str:comment_id>', StudentViews.delete_scomment, name="delete_scomment"),
    path('student/covid19', StudentViews.scovid19,name="scovid19"),
    path('student_view_financial_record_list',StudentViews.student_view_financial_record_list,name="student_view_financial_record_list"),
    
    #Accountant URL Path
    path('account_home', AccountViews.account_home, name="account_home"),
    path('account_apply_leave', AccountViews.account_apply_leave, name="account_apply_leave"),
    path('account_apply_leave_save', AccountViews.account_apply_leave_save, name="account_apply_leave_save"),
    path('account_feedback', AccountViews.account_feedback, name="account_feedback"),
    path('account_feedback_save', AccountViews.account_feedback_save, name="account_feedback_save"),
    path('account_profile', AccountViews.account_profile, name="account_profile"),
    path('account_profile_save', AccountViews.account_profile_save, name="account_profile_save"),
    path('account_fcmtoken_save', AccountViews.account_fcmtoken_save, name="account_fcmtoken_save"),
    path('account_all_notification', AccountViews.account_all_notification, name="account_all_notification"),
    path('account_news', AccountViews.account_news, name="account_news"),
    path('account/view_account_news/<str:news_id>', AccountViews.view_account_news, name="view_account_news"),
    path('view_a_news_comment_save', AccountViews.view_account_news_comment_save, name="view_account_news_comment_save"),
    path('view_a_news_comment_edit_save', AccountViews.view_account_news_comment_edit_save, name="view_account_news_comment_edit_save"),
    path('delete_acomment/<str:news_id>/<str:comment_id>', AccountViews.delete_acomment, name="delete_acomment"),
    path('account_add_financial_record', AccountViews.account_add_financial_record, name='account_add_financial_record'),
    path('account_financial_record_list/', AccountViews.account_financial_record_list, name='account_financial_record_list'),
    
    
    # Parents URL Path
    path('parent_home', ParentViews.parent_home, name="parent_home"),
    path('parent_view_attendance', ParentViews.parent_view_attendance, name="parent_view_attendance"),
    path('parent_view_attendance_post', ParentViews.parent_view_attendance_post, name="parent_view_attendance_post"),
    path('parent_feedback', ParentViews.parent_feedback, name="parent_feedback"),
    path('parent_feedback_save', ParentViews.parent_feedback_save, name="parent_feedback_save"),
    path('parent_profile', ParentViews.parent_profile, name="parent_profile"),
    path('parent_profile_save', ParentViews.parent_profile_save, name="parent_profile_save"),
    path('parent_fcmtoken_save', ParentViews.parent_fcmtoken_save, name="parent_fcmtoken_save"),
    path('parent_all_notification',ParentViews.parent_all_notification,name="parent_all_notification"),
    path('parent_student_view_result',ParentViews.parent_student_view_result,name="parent_student_view_result"),
    path('parent_news', ParentViews.parent_news, name="parent_news"),
    path('parent/view_parent_news/<str:news_id>', ParentViews.view_parent_news, name="view_parent_news"),
    path('view_p_news_comment_save', ParentViews.view_parent_news_comment_save, name="view_parent_news_comment_save"),
    path('view_p_news_comment_edit_save', ParentViews.view_parent_news_comment_edit_save, name="view_parent_news_comment_edit_save"),
    path('delete_pcomment/<str:news_id>/<str:comment_id>', ParentViews.delete_pcomment, name="delete_pcomment"),
    path('parent_view_financial_record_list',ParentViews.parent_view_financial_record_list,name="parent_view_financial_record_list"),
    path('parent/covid19', ParentViews.pcovid19,name="pcovid19"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
