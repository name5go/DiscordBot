 # -*- coding: Shift-JIS -*-

#������`�F�b�N
import re

name5go_id=377632130718498826

class Checker():
 """�`�F�b�N�n�̊֐��܂Ƃ�"""
 def is_admin_id(self,id):
  return id==name5go_id

 def is_url_string(self,url):
  """������url�̏������ǂ������ׂ�"""
  pattern = "https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"
  return re.match (pattern, url)

 #�����񂪃T�[�o�[�����ɓo�^����Ă��邩
 def is_pic_list_word(self,server_pic_list,server_id,word):
  return word in server_pic_list[server_id]



 def is_joined_user(self,ctx):
  """�R�}���h���s�҂��{�C�X�`�����l���ɓ����Ă��Ȃ����true��Ԃ�"""
  return ctx.author.voice is None

 def is_joined_bot(self,ctx):
  """BOT���{�C�X�`�����l���ɉ������Ă��邩���ׂ�"""
  return ctx.guild.voice_client is None


 #�ǂ���url�����ׂ�
 def where_url(self,url):
    youtube="youtube"
    no="not applied"
    if re.match(youtube, url):
        return youtube
    return no


