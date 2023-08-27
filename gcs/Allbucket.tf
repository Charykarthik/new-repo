resource "google_storage_bucket"{
    name = "sceg_bucket"
    project = "modernization"
    location = "us-central1"
    force_destroy = true
    labels = test,devops
    storage_class = "standard"

    iam_configuration{
        public_access_prevention = "enforced"   # "unspecified" or "enforced"
        uniform_bucket_level_access = true      # uniform level true or false
        bucket_policy_only = true               # fine-grained true or false
    }
    versioning {
        enabled = true # true or false
    }

    encryption {
        default_kms_key_name = "google"
    }
}
