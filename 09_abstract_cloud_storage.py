"""
Abstraction - Program 9:
Create an abstract class CloudStorage with abstract methods:
a) upload_file()
b) download_file()
c) delete_file()
Create subclasses representing different storage services and implement the operations.
"""

from abc import ABC, abstractmethod

class CloudStorage(ABC):
    def __init__(self, service_name, account_id):
        self.service_name = service_name
        self.account_id = account_id

    @abstractmethod
    def upload_file(self, filename, file_size_mb):
        pass

    @abstractmethod
    def download_file(self, filename):
        pass

    @abstractmethod
    def delete_file(self, filename):
        pass


class GoogleDriveStorage(CloudStorage):
    def __init__(self, account_id):
        super().__init__("Google Drive", account_id)

    def upload_file(self, filename, file_size_mb):
        print(f"[Google Drive ({self.account_id})] Uploading '{filename}' ({file_size_mb} MB) to Google Workspace Drive...")
        print("  Generating shareable Google Docs link and syncing revision history.")

    def download_file(self, filename):
        print(f"[Google Drive ({self.account_id})] Fetching '{filename}' via Drive REST API v3...")

    def delete_file(self, filename):
        print(f"[Google Drive ({self.account_id})] Moving '{filename}' to Google Drive Trash (retained for 30 days).")


class AWSS3Storage(CloudStorage):
    def __init__(self, account_id, bucket_name="production-app-bucket"):
        super().__init__("Amazon AWS S3", account_id)
        self.bucket_name = bucket_name

    def upload_file(self, filename, file_size_mb):
        print(f"[AWS S3 ({self.account_id})] Initiating multipart PUT request for '{filename}' ({file_size_mb} MB)...")
        print(f"  Target: s3://{self.bucket_name}/{filename} | AES-256 Server-Side Encryption enabled.")

    def download_file(self, filename):
        print(f"[AWS S3 ({self.account_id})] Streaming GET request for s3://{self.bucket_name}/{filename} with presigned URL.")

    def delete_file(self, filename):
        print(f"[AWS S3 ({self.account_id})] Executing permanent object deletion from bucket '{self.bucket_name}'.")


class DropboxStorage(CloudStorage):
    def __init__(self, account_id):
        super().__init__("Dropbox Business", account_id)

    def upload_file(self, filename, file_size_mb):
        print(f"[Dropbox ({self.account_id})] Uploading '{filename}' ({file_size_mb} MB) via block-level delta sync...")

    def download_file(self, filename):
        print(f"[Dropbox ({self.account_id})] Downloading '{filename}' to local synced client folder.")

    def delete_file(self, filename):
        print(f"[Dropbox ({self.account_id})] Removing '{filename}' from team shared space.")


def backup_pipeline(cloud_provider: CloudStorage, file_to_backup, size_mb):
    """Abstraction in action: Caller interacts with the storage interface uniformly."""
    print(f"\n--- Initiating Backup on {cloud_provider.service_name} ---")
    cloud_provider.upload_file(file_to_backup, size_mb)
    cloud_provider.download_file(file_to_backup)
    cloud_provider.delete_file(file_to_backup)


if __name__ == "__main__":
    providers = [
        GoogleDriveStorage("user@college.edu"),
        AWSS3Storage("AWS_ACC_89123", bucket_name="apc-student-backups"),
        DropboxStorage("research_team@apc.org")
    ]

    print("=== Multi-Cloud Storage Management System (Abstraction Interface) ===")
    for provider in providers:
        backup_pipeline(provider, "database_dump_2026.sql", 128.5)
