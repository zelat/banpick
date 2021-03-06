from django import forms
from .models import Draft

class RoomCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(RoomCreateForm, self).__init__(*args, **kwargs)
    
    match_name = forms.CharField(
        label="比赛名称",
        widget=forms.TextInput(attrs={
            'class': 'bg_black bold draft_input',
            'autofocus': 'true',
            'onkeyup': 'submitable()'
        })
    )

    blue_team_name = forms.CharField(
        label="蓝队名字",
        help_text="<span class='f_right player_check'><input id='blue_player_check' class='blue' type='checkbox' onchange='playerCheck(event);'><label for='blue_player_check'>成员名字</label></span>",
        widget=forms.TextInput(attrs={
            'class': 'bg_blue bold draft_input',
            'onkeyup': 'submitable()'
        })
    )

    red_team_name = forms.CharField(
        label="红队名字",
        help_text="<span class='f_right player_check'><input id='red_player_check' class='red' type='checkbox' onchange='playerCheck(event);'><label for='red_player_check'>成员名字</label></span>",
        widget=forms.TextInput(attrs={
            'class': 'bg_red bold draft_input',
            'onkeyup': 'submitable()'
        })
    )

    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput(attrs={
            'class': 'bg_black bold draft_input',
            'onkeyup': 'submitable()'
        })
    )

    class Meta:
        model = Draft
        fields = ('match_name', 'blue_team_name', 'red_team_name', 'password')
