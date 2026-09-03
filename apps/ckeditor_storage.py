import cloudinary.uploader

from django.core.files.storage import Storage
from django.utils.deconstruct import deconstructible


@deconstructible
class CKEditorCloudinaryStorage(Storage):

    def _save(self, name, content):
        content.seek(0)

        result = cloudinary.uploader.upload(
            content,
            folder="ckeditor",
            resource_type="auto",
            use_filename=True,
            unique_filename=True,
        )

        return result["public_id"]

    def url(self, name):
        import cloudinary

        return cloudinary.CloudinaryImage(name).build_url(
            secure=True
        )

    def exists(self, name):
        return False