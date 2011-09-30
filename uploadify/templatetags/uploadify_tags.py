from django import template
from django.conf import settings
from uploadify import settings as u_settings

register = template.Library()

# -----------------------------------------------------------------------------
#   multi_file_upload
# -----------------------------------------------------------------------------
@register.inclusion_tag('uploadify/multi_file_upload.html', takes_context=True)
def multi_file_upload(context, upload_complete_url):
    """
    Displays a Flash-based interface for uploading multiple files.
    When all files have been uploaded, the given URL is POSTed to.  The returned
    page replaces (AJAX) the upload interface.

    * filesUploaded - The total number of files uploaded
    * errors - The total number of errors while uploading
    * allBytesLoaded - The total number of bytes uploaded
    * speed - The average speed of all uploaded files
    """
    return { 
        'upload_complete_url' : upload_complete_url,
        'uploadify_path' : u_settings.UPLOADIFY_PATH,
        'upload_path' : u_settings.UPLOADIFY_UPLOAD_PATH,
        'cookie_name' :  settings.SESSION_COOKIE_NAME,
        'cookie_value' : context['request'][settings.SESSION_COOKIE_NAME],
    }
