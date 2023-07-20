pipeline {
    agent {
        dockerfile {
            filename 'Dockerfile'
            label 'zip-job-docker'
            args '--privileged'
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'pwd'
                sh 'ls -la'
                sh 'python3 zip_job.py'
                sh 'cd /tmp'
                sh 'ls'
                sh 'cd txt'
                sh 'ls'
                sh 'cd ..'
                sh 'cd zip'
                sh 'ls -la'
                sh 'pwd'
            }
        }
        stage('Publish') {
            steps {
                sh 'curl -u user:password -T *.zip "http://your-artifactory-instance/artifactory/your-repo/"'
            }
        }
    }
}
