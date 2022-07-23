import logging
import dotenv
import os
import requests
import tinq.settings as s

logging.getLogger(__name__).addHandler(logging.NullHandler())

dotenv.load_dotenv()


class Tinq:
    def __init__(self, api_key=os.getenv('TINQ_API_KEY')):
        self.api_key = api_key

        self.header_parameters = {
            'Authorization': f'Bearer {self.api_key}'
        }

    def tinq_request(self, endpoint=None, params=None, method='POST'):
        """
        This method generates a request sent to Tinq.ai's API.
        API documentation: https://developers.tinq.ai/reference
        :param endpoint:
        :param params:
        :param method:
        :return:
        """
        if endpoint is None:
            endpoint = s.CHECK_ENDPOINT
        if params is None:
            params = {}

        parameters = {}
        for param in params:
            parameters.update({param: params[param]})

        payload = parameters

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f'Bearer {self.api_key}'
        }

        try:
            if method == 'POST':
                response = requests.post(url=endpoint, json=payload, headers=headers)
            elif method == 'GET':
                response = requests.get(url=endpoint, json=payload, headers=headers)
            elif method == 'DELETE':
                response = requests.delete(url=endpoint, json=payload, headers=headers)
            else:
                response = requests.post(url=endpoint, json=payload, headers=headers)
            return response.json()
        except Exception as e:
            return e

    def sentiments(self, text=None, project=None):
        params = {'text': text, 'project': project}
        return self.tinq_request(endpoint=s.SENTIMENT_ANALYSIS_ENDPOINT, params=params)

    def classify(self, text=None, classifier=None, project=None):
        params = {'text': text, 'project': project, 'classifier': classifier}
        return self.tinq_request(endpoint=s.CLASSIFIER_ENDPOINT, params=params)

    def classifiers(self):
        return self.tinq_request(endpoint=s.LIST_CLASSIFIERS_ENDPOINT, method='GET')

    def check_plagiarism(self, text=None):
        params = {'text': text}
        return self.tinq_request(endpoint=s.PLAGIARISM_CHECKER_ENDPOINT, params=params)

    def rewrite(self, text=None, mode='normal', unique=False, lang=None):
        params = {'text': text, 'mode': mode, 'unique': unique, 'lang': lang}
        return self.tinq_request(endpoint=s.REWRITER_ENDPOINT, params=params)

    def summarize(self, text=None, output_percent=30):
        params = {'text': text, 'output_percent': output_percent}
        return self.tinq_request(endpoint=s.SUMMARIZER_ENDPOINT, params=params)

    def extract_article(self, url=None):
        params = {'url': url}
        return self.tinq_request(endpoint=s.ARTICLE_EXTRACTOR_ENDPOINT, params=params)

    def ner(self, text=None):
        params = {'text': text}
        return self.tinq_request(endpoint=s.NER_ENDPOINT, params=params)