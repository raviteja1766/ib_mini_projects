from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import ValidatorAbstractClass


class ValidatorClass(ValidatorAbstractClass):
    def __init__(self, *args, **kwargs):
        self.request_data = kwargs['request_data']
        self.user = kwargs['user']
        self.user_dto = kwargs['user_dto']
        self.access_token = kwargs['access_token']

    def sample_validation(self):
        """
        sample validations to be carried out here
        return True or False
        """
        return self.request_data

    def validate(self):
        """
        A wrapper function that calls all the validations and sends back
        necessary data.
        :return: A dictionary with values that are to be carry-forwarded to
        api_wrapper.
        """
        dict_ = dict()
        dict_['some_key'] = self.sample_validation()
        return dict_
