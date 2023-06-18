import os
import nbformat
from nbconvert import HTMLExporter
from django.http import HttpResponse
from django.conf import settings
from django.views import View
from django.shortcuts import render

class NotebookView(View):
    template_name = 'neural_networks_nb_view.html'

    def get(self, request):
        # Locate your .ipynb file
        notebook_path = os.path.join(settings.BASE_DIR, 'static', 'ipynb', 'nn-makemore-wavenet.ipynb')

        # Read the notebook
        with open(notebook_path) as f:
            nb = nbformat.read(f, as_version=4)

        # Convert to HTML
        html_exporter = HTMLExporter()
        body, resources = html_exporter.from_notebook_node(nb)

        # Return as HTML response
        return render(request, self.template_name, {'nb': body})