pipeline {
    agent {
        dockerfile {
            filename 'dockerfile'
            label 'zip-job-docker'
            args '--privileged'
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'python3 /tmp/zip_job.py'
                sh 'ls /tmp/'
                sh 'ls /tmp'
                sh 'ls /tmp/txt'
                sh 'ls /tmp/zip'
            }
        }
        stage('Publish') {
            steps {
                sh 'curl -u user:password -T *.zip "http://your-artifactory-instance/artifactory/your-repo/"'
            }
        }
    }
}
