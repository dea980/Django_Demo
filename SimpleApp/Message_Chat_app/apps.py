from django.apps import AppConfig


class MessageChatAppConfig(AppConfig):
    """
    MessageChatAppConfig class for the Message_Chat_app application.
    Defines the name of the application.
    """
    # 근데 모델 여러가지 쓸수 있나? LLM
    ## 혹옥시 모르자너~ 물론 메시지가 나중에 30분 후에 없어지는식으로 할꺼지만 
    ## 일단 GPT를 답장하는 LLM으로 쓸꺼고~ 아직을 30분 후 보단 기입되는 configuration에 집중~
    ##default_auto_field는 모델에서 기본적으로 사용하는 자동 필드(primary key) 타입을 설정
    ##데이터베이스에서 저장할 데이터의 크기가 작다면, AutoField(32비트 정수형)를 사용할 수도 있지만, BigAutoField는 더 많은 데이터를 처리할 수 있으므로 기본으 설정
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Message_Chat_app'

## chatting app 에 필요한 설정들이 필요할경우 여기에 기입.
