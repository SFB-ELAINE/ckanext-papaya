import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import mimetypes
import logging

log = logging.getLogger(__name__)

def get_filepath(resource_id):
    return "/var/lib/ckan/default/resources/" + resource_id[0:3] + \
            "/" + resource_id[3:6] + "/" + resource_id[6:]

class PapayaPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IResourceView)
    plugins.implements(plugins.ITemplateHelpers)

    # IConfigurer

    def update_config(self, config_):
        mimetypes.add_type("DICOM", ".dcm")
        mimetypes.add_type("NIFTI", ".nii")

        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'papaya')

    # IResourceView

    def info(self):
        return { 'name': 'papaya',
            'title': toolkit._('Papaya Viewer'),
            'icon': 'cube',
            'default_title' :toolkit._('Papaya Viewer'),
            'iframed': False
        }

    def can_view(self, data_dict):
        resource = data_dict['resource']
        return (resource.get('format').lower() in ['dicom', 'nifti'])

    def setup_template_variables(self, context, data_dict):
        return data_dict

    def view_template(self, context, data_dict):
        return "papaya_view.html"

    def form_template(self, context, data_dict):
        return "papaya_form.html"

    # ITemplateHelpers
    def get_helpers(self):
        return {'papaya_get_filepath': get_filepath}
