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
                sh 'python3 zip_job.py'
            }
        }
        stage('Publish') {
            steps {
                script {
                    def server = Artifactory.server '<jfrog>'
                    def uploadSpec = """{
                        "files": [
                            {
                                "pattern": "*.zip",
                                "target": "generic-local"
                            }
                        ]
                    }"""
                    
                    def buildInfo = "1.2.0"
                    server.upload spec: uploadSpec, buildInfo: buildInfo
                    
                    // Publish the build info to Artifactory
                    server.publishBuildInfo buildInfo
                }
            }
        stage('Report') {
           steps {
            emailext (
                to: 'vitaliyusf@gmail.com',
                subject: "Job '${env.JOB_NAME}' (${env.BUILD_NUMBER}) status",
                body: "Check console output at ${env.BUILD_URL} to view the results."
            )
            }
        }
    }
}
}

    
