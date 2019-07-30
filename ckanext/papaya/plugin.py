import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import mimetypes
import logging
import zipfile
import os
import base64

log = logging.getLogger(__name__)

def get_filepath(resource_id):
    return "/var/lib/ckan/default/resources/" + resource_id[0:3] + \
            "/" + resource_id[3:6] + "/" + resource_id[6:]

def encode_files(resource):
    encoded_data = []
    src = get_filepath(resource["id"])
    dst = "/var/lib/ckan/default/zip/" + resource["package_id"]
    # temporarily unzip the file
    try:
        with zipfile.ZipFile(src, 'r') as zip_ref:
            zip_ref.extractall(dst)
    except:
        return ""
    dir_list = os.listdir(dst)
    for i in range(len(dir_list)):
        if dir_list[i][-4:] == ".dcm":
            try:
                f = open(dst + "/" + dir_list[i], 'r')
            except:
                continue
            contents = f.read()
            encoded_image = base64.encodestring(contents)
            encoded_data.append(encoded_image)
            f.close()
    # remove unzipped directory - we don't need it anymore
    # TODO: potential race condition here if someone else is also viewing
    # this resource?
    # could we keep each user's stuff completely separate to avoid that?
    os.system(" ".join(("rm -r", dst)))
    return encoded_data

class PapayaPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IResourceView)
    plugins.implements(plugins.IResourceController, inherit=True)
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
        return (resource.get('format').lower() in ['dicom', 'nifti', 'zip-dcm', 'zip'])

    def setup_template_variables(self, context, data_dict):
        return data_dict

    def view_template(self, context, data_dict):
        return "papaya_view.html"

    def form_template(self, context, data_dict):
        return "papaya_form.html"

    # IResourceController

    def after_create(self, context, resource):
        found_dcm = False
        if (resource["format"] == "ZIP"):
            src = get_filepath(resource["id"])
            with zipfile.ZipFile(src, 'r') as zip_ref:
                for item in zip_ref.namelist():
                    if item[-4:] == ".dcm":
                        found_dcm = True
                        break
        if found_dcm:
            toolkit.get_action('resource_view_create')(context, {
                                    'resource_id': resource['id'],
                                    'title': 'Papaya View',
                                    'view_type': 'papaya'
                                })
        return resource

    # ITemplateHelpers
    def get_helpers(self):
        return {'papaya_get_filepath': get_filepath,
                'papaya_encode_files': encode_files}
