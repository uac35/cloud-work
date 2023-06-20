from google.cloud import secretmanager

class secrets:
    def __init__(self, project_id):
        self.project_id = project_id
        self.client = secretmanager.SecretManagerServiceClient()

    def access_secret_version(self, secret_id, version_id):
        # Build the resource name of the secret version.
        name = f"projects/{self.project_id}/secrets/{secret_id}/versions/{version_id}"

        # Access the secret version.
        response = self.client.access_secret_version(request={"name": name})

        # Return the decoded payload.
        return response.payload.data.decode('UTF-8')
