pipeline {
    agent none
    stages {
        stage('Run Docker Container') {
            steps {
                script {
                    docker.image('my-python-app').run('--privileged --label=zip-job-docker')
                }
            }
        }
           stage('Build') {
            steps {
                sh 'python3 tmp/zip_job.py'
            }
        }
        stage('Publish') {
            steps {
                sh 'curl -u user:password -T *.zip "http://your-artifactory-instance/artifactory/your-repo/"'
            }
        }
    }
}
Ï
