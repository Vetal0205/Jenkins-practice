pipeline {
    options{timestamps()}
    agent none
    environment {
        WORKSPACE = "/var/jenkins_home/workspace/${JOB_NAME}"
    }
    stages {
        stage('Checkout') {
            agent any
            steps {
                checkout scm
            }
        }
        
        stage('Build and Test') {
            agent{ docker {
                image 'python:3.11.5-slim'
                args "-u root"}}
            steps {
                sh 'python -m venv venv'
                sh 'source venv/bin/activate && pip install -r requirements.txt'
                sh 'source venv/bin/activate && python -m unittest discover -s tests -p "test_*.py"'
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
