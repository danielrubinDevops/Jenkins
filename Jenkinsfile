pipeline {
    agent any  // Can run on any available agent
    
    environment {
        PYTHON_ENV = 'python3'  // Version/path to Python
    }

    stages {
        stage('Install Python') {
            steps {
                script {
                    echo 'Checking if Python is installed...'
                    sh 'sudo apt update -y'  // Ensure package list is up-to-date
                    sh 'sudo apt install python3 -y'  // Install Python without prompt
                    echo 'Python is already installed.'
                }
            }
        }

        stage('Install pip') {
            steps {
                script {
                    echo 'Installing pip...'
                    sh 'sudo apt install python3-pip -y'  // Install pip without prompt
                }
            }
        }

        stage('Install dependencies') {
            steps {
                script {
                    echo 'Installing dependencies...'
                    sh "${env.PYTHON_ENV} -m pip install -r requirements.txt"  // Install Python dependencies from a requirements file
                }
            }
        }

        stage('Run tests') {
            steps {
                script {
                    // Run tests (e.g., using unittest or other testing libraries)
                    echo 'Running tests...'
                    def result = sh(script: "python -m unittest discover -s tests", returnStatus: true)
                    // If tests fail (status != 0), the pipeline will stop
                    if (result != 0) {
                        error("Tests failed, stopping pipeline.")
                    }
                }
            }
        }

        stage('Deploy') {
            when {
                // Only run deployment if we're on the 'main' branch
                branch 'main'
            }
            steps {
                script {
                    // Deployment action (e.g., copy to a server or trigger some project)
                    echo 'Deploying application...'
                    // Add your deployment script here
                }
            }
        }
    }

    post {
        // If all tests passed successfully, send a success message
        success {
            echo 'Pipeline finished successfully!'
        }
        // If the pipeline failed, send a failure message
        failure {
            echo 'Pipeline failed.'
        }
    }
}
