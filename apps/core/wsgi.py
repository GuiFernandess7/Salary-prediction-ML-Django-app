import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
application = get_wsgi_application()

# ML registry
import inspect
from ml.registry import MLRegistry
from ml.income_classifier.random_forest import RandomForestClassifier
from ml.income_classifier.extra_trees import ExtraTreesClassifier

try:
    registry = MLRegistry()
    rf = RandomForestClassifier()
    registry.add_algorithm(endpoint_name="income_classifier",
                            algorithm_object=rf,
                            algorithm_name="random forest",
                            algorithm_status="production",
                            algorithm_version="0.0.1",
                            owner="Piotr",
                            algorithm_description="Random Forest with simple pre- and post-processing",
                            algorithm_code=inspect.getsource(RandomForestClassifier)
                        )

    et = ExtraTreesClassifier()
    registry.add_algorithm(endpoint_name="income_classifier",
                            algorithm_object=et,
                            algorithm_name="extra trees",
                            algorithm_status="testing",
                            algorithm_version="0.0.1",
                            owner="Piotr",
                            algorithm_description="Extra Trees with simple pre- and post-processing",
                            algorithm_code=inspect.getsource(RandomForestClassifier)
                        )

except Exception as e:
    print("Exception while loading the algorithms to the registry,", str(e))
    import traceback
    traceback.print_exc()