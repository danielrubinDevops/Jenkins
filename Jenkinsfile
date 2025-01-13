pipeline {
    agent any  // יכול לרוץ על כל סוכן פנוי

    environment {
        // הגדרות סביבות עבודה (למשל, אם יש צורך בהגדרת PATH למיקום pip)
        PYTHON_ENV = 'python3'  // אפשר להגדיר את הגרסה או את המיקום של Python
    }

    stages {
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
