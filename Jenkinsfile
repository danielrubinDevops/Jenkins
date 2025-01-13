pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building the application...'
                // Example of a build command
                sh 'echo Building...'
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
                // Example of running test scripts
                sh 'echo Running tests...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying the application...'
                // Example of deployment command
                // Example of deployment command
                sh 'echo Deploying...'
            }
        }
    }
    post {
        always {
            echo 'Pipeline completed.'
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
