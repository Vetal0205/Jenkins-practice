pipeline {
    options{timestamps()}
    agent none

    stages {
        stage('Checkout') {
            agent any
            steps {
                checkout scm
            }
        }
        
        stage('Build and Test') {
            agent any
            steps {
                sh 'echo hi'
                sh 'apk add --update python3 py-pip'
                sh 'pip install -r requirements.txt'
                sh 'python -m unittest discover -s tests -p "test_*.py"'
            }
            post {
                always {
                    junit 'test-reports/*.xml'
                }
                success {
                    echo "Testing completed successfully."
                }
                failure {
                    echo "Tests failed."
                 }
            }
        }

        // stage('Build Container') {
        //     steps {
        //         sh 'docker build -t notebook_app .'
        //     }
        // }

        // stage('Deploy Container') {
        //     steps {
        //         sh 'docker run -d notebook_app'
        //     }
        // }
    }
}
