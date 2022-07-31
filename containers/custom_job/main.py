import argparse
import pytz  # job作成時に必要
from google.cloud import aiplatform


def run(project_id, location, display_name, template_path, pipeline_root_path, service_account):
    aiplatform.init(
        project=project_id,
        location=location,
    )

    job = aiplatform.PipelineJob(
        display_name=display_name,
        template_path=template_path,
        pipeline_root=pipeline_root_path,
        enable_caching=False,
    )
    job.submit(service_account=service_account)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--project-id', type=str, required=True)
    parser.add_argument('--location', type=str, required=True)
    parser.add_argument('--display-name', type=str, required=True)
    parser.add_argument('--template-path', type=str, required=True)
    parser.add_argument('--pipeline-root-path', type=str, required=True)
    parser.add_argument('--service-account', type=str, required=True)
    args = parser.parse_args()

    run(**vars(args))
