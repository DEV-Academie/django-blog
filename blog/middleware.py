class CountPostMiddleWare:

    def __init__(self, get_response):
        self.get_response = get_response
        self.count_posts = dict()

    def _get_pk(self, request):
        path_elements = request.path.split("/")

        # Exclude Home
        if not path_elements[1]:
            return None

        # Exclude Categories and Comments
        elif "comment" in path_elements or "categorie" in path_elements:
            return None

        # Update count and print result
        else:
            return path_elements[1]

    def __call__(self, request, *args, **kwargs):

        response = self.get_response(request)  # View called

        pk = self._get_pk(request)
        if pk:
            self.count_posts[pk] = self.count_posts.get(pk, 0) + 1

            for key, value in self.count_posts.items():
                print(f"Bericht met pk {key} is {value} keer bekeken")

        return response

    def process_template_response(self, request, response):
        pk = self._get_pk(request)
        if pk:
            count = self.count_posts.get(pk, 0)
            response.context_data["count"] = count

        return response
