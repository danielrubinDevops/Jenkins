pipeline {
    agent any  // יכול לרוץ על כל סוכן פנוי
    
    environment {
        PYTHON_ENV = 'python3'  // גרסה/נתיב לפייתון
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
            sh 'pip install -r requirements.txt'  // Install Python dependencies from a requirements file
        }
    }
}


        stage('Install dependencies') {
            steps {
                script {
                    // התקנת ספריות Python באמצעות pip
                    echo 'Installing Python dependencies...'
                    sh "${env.PYTHON_ENV} -m pip install -r requirements.txt"
                }
            }
        }

        stage('Run tests') {
            steps {
                script {
                    // הרצת קובץ הבדיקות (הפעלת unittest או כל ספריית בדיקות אחרת)
                    echo 'Running tests...'
                    def result = sh(script: "python -m unittest discover -s tests", returnStatus: true)
                    // אם הבדיקות לא הצליחו (status != 0), הפייפליין ייכשל
                    if (result != 0) {
                        error("Tests failed, stopping pipeline.")
                    }
                }
            }
        }

        stage('Deploy') {
            when {
                // הבדיקות עברו בהצלחה, אז נבצע את שלב הפריסה
                branch 'main'  // בדוק אם אנחנו בבראנץ' "main"
            }
            steps {
                script {
                    // פעולת פריסה (נניח העתקה לשרת או הפעלת פרויקט כלשהו)
                    echo 'Deploying application...'
                    // כאן תוכל להוסיף את הקוד שיבצע את הפריסה
                }
            }
        }
    }

    post {
        // אם כל הבדיקות עברו בהצלחה, נשלח הודעה
        success {
            echo 'Pipeline finished successfully!'
        }
        // אם הפייפליין נכשל, נשלח הודעה
        failure {
            echo 'Pipeline failed.'
        }
    }
}
