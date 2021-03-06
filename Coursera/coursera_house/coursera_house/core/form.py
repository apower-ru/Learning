from django import forms


class ControllerForm(forms.Form):
    bedroom_target_temperature = forms.IntegerField(min_value=16, max_value=50)
    hot_water_target_temperature = forms.IntegerField(min_value=24, max_value=90)
    bedroom_light = forms.BooleanField(required=False)
    bathroom_light = forms.BooleanField(required=False)

#####################################################################################################################
# from django import forms
# from django.core.validators import MinValueValidator, MaxValueValidator
#
#
# class ControllerForm(forms.Form):
#     bedroom_target_temperature = forms.IntegerField(
#         required=False,
#         validators=[MinValueValidator(16), MaxValueValidator(50)]
#     )
#     hot_water_target_temperature = forms.IntegerField(
#         required=False,
#         validators=[MinValueValidator(24), MaxValueValidator(90)]
#     )
#     bedroom_light = forms.BooleanField(required=False)
#     bathroom_light = forms.BooleanField(required=False)