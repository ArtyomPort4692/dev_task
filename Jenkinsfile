pipeline {
    agent {
        dockerfile {
            filename 'Dockerfile'
            args '--privileged'
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'python3 zip_job.py'
            }
        }
        // stage('Publish') {
        //     steps {
        //         sh 'curl -u user:password -T *.zip "http://your-artifactory-instance/artifactory/your-repo/"'
        //     }
        // }
        stage('Report') {
           steps {
            emailext (
                to: 'test@gmail.com',
                subject: "Job '${env.JOB_NAME}' (${env.BUILD_NUMBER}) Failed",
                body: "Check console output at ${env.BUILD_URL} to view the results."
            )
    }
}
    }
    post {
        success {
            emailext (
                to: 'test@gmail.com',
                subject: "Job '${env.JOB_NAME}' (${env.BUILD_NUMBER}) Succeeded",
                body: "Check console output at ${env.BUILD_URL} to view the results."
            )
        }
        failure {
            emailext (
                to: 'test@gmail.com',
                subject: "Job '${env.JOB_NAME}' (${env.BUILD_NUMBER}) Failed",
                body: "Check console output at ${env.BUILD_URL} to view the results."
            )
        }
    }
}
        
