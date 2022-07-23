from tinq import Tinq
from settings import PROJECTS_ENDPOINT, PROJECTS_CONTENT_ENDPOINT


class Projects(Tinq):
    def __init__(self):
        super().__init__()

    def list(self, page=1, order='DESC', column_sort='created_at'):
        """
        :param page: Pagination parameter. Helps you navigate through all projects that you have
        :param order: Sorting order.
        :param column_sort: Sorting column. default created_at, sort by date. options: project_name, sort by project name,
        """

        params = {'page': page, 'order': order, 'column_sort': column_sort}
        return self.tinq_request(endpoint=PROJECTS_ENDPOINT, params=params, method='GET')

    def get(self, project_id=None, page=1, order='DESC', column_sort='created_at'):
        """
        :param project_id: Project identifier
        :param page: Pagination parameter. Helps you navigate through all projects that you have
        :param order: Sorting order.
        :param column_sort: Sorting column. default created_at, sort by date. options: content, sort by project name,
        """

        params = {'page': page, 'order': order, 'column_sort': column_sort}
        return self.tinq_request(endpoint=f'{PROJECTS_ENDPOINT}/{project_id}', params=params, method='GET')

    def delete(self, project_id=None):
        """
        :param project_id: Project identifier
        """
        return self.tinq_request(endpoint=f'{PROJECTS_CONTENT_ENDPOINT}/{project_id}', method='DELETE')

