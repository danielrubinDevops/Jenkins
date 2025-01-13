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
                    sh 'for i in {1..5}; do sudo apt update -y && break || sleep 15; done'  // Retry 5 times with a 15-second delay
                    sh 'sudo apt install python3 -y'
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

        stage('Install python3-venv') {
            steps {
                script {
                    echo 'Installing python3-venv package...'
                    sh 'sudo apt install python3-venv -y'  // Install the python3-venv package
                }
            }
        }

        stage('Create Virtual Environment') {
            steps {
                script {
                    echo 'Creating virtual environment...'
                    sh 'python3 -m venv venv'  // Create a virtual environment in the "venv" folder
                    sh '. venv/bin/activate'  // Activate the virtual environment (dot instead of source)
                    echo 'Virtual environment created and activated.'
                }
            }
        }

        stage('Install dependencies') {
            steps {
                script {
                    echo 'Installing dependencies...'
                    sh '. venv/bin/activate && pip install -r requirements.txt'  // Install Python dependencies within the virtual environment
                }
            }
        }

        stage('Run tests') {
            steps {
                script {
                    echo 'Running tests...'
                    def result = sh(script: ". venv/bin/activate && python -m unittest discover -s tests", returnStatus: true)
                    // If tests fail (status != 0), the pipeline will stop
                    if (result != 0) {
                        error("Tests failed, stopping pipeline.")
                    }
                }
            }
        }

        stage('Deploy') {
            when {
                branch 'main'
            }
            steps {
                script {
                    echo 'Deploying application...'
                    // Add your deployment script here
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline finished successfully!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
