pipeline {
    agent any  // יכול לרוץ על כל סוכן פנוי

    environment {
        PYTHON_ENV = 'python3'  // גרסה/נתיב לפייתון
    }

    stages {
        stage('Install Python') {
            steps {
                script {
                    // בדיקה אם פייתון מותקן
                    echo 'Checking if Python is installed...'
                    def pythonCheck = sh(script: "python3 --version", returnStatus: true, wait: true)
                    if (pythonCheck != 0) {
                        echo 'Python not installed. Installing Python...'
                        // התקנת פייתון
                        if (isUnix()) {
                            // עבור לינוקס/מקרו
                            sh 'sudo apt-get update && sudo apt-get install -y python3 python3-pip'
                        } else {
                            // עבור Windows
                            echo 'Please install Python manually or use a pre-configured environment.'
                            error('Python installation is required.')
                        }
                    } else {
                        echo 'Python is already installed.'
                    }

                    // התקנת pip אם הוא לא נמצא
                    def pipCheck = sh(script: "python3 -m pip --version", returnStatus: true, wait: true)
                    if (pipCheck != 0) {
                        echo 'pip not found. Installing pip...'
                        sh 'python3 -m ensurepip --upgrade'
                    } else {
                        echo 'pip is already installed.'
                    }
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
