# from django.conf import settings
# from django.db import models
# from model_utils.models import TimeStampedModel
#
#
# # Create your models here.
#
#
#
# class TrackedModel(TimeStampedModel):
#     """TrackedModel to make tables have created_on, created_by, updated_on and updated_by consistently"""
#
#     class Meta:
#         abstract = True
#
#     created_by = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         default=get_current_user(),
#         # Reverse relation from User not needed, hence +.
#         # https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.ForeignKey.related_name
#         related_name="+",
#         editable=False,
#         verbose_name="created_by",
#         on_delete=models.SET_NULL,
#         null=True,
#     )
#
#     modified_by = models.ForeignKey(
#         settings.AUTH_USER_MODEL,
#         default=get_current_user(),
#         # Reverse relation from User not needed, hence +.
#         # https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.ForeignKey.related_name
#         related_name="+",
#         editable=False,
#         verbose_name="modified_by",
#         on_delete=models.SET_NULL,
#         null=True,
#     )
#
#     def save(self, *args, **kwargs):
#         user = get_current_user() if get_current_request() and get_current_user() else get_user_model().get_system_user()
#         if not user:
#             raise PermissionDenied("You don't have permission to perform this operation.")
#         if self.created_by is None:
#             self.created_by = user
#         else:
#             self.modified_by = user
#         super(TrackedModel, self).save(*args, **kwargs)