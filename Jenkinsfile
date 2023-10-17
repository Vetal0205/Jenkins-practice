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
            agent  {
                docker { 
                    image 'python:3.11.5-alpine' 
                    args '-u root'
                }
            }
            steps {
                sh 'echo hi'
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
