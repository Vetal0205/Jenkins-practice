pipeline {
    options{timestamps()}
    agent none

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build and Test') {
            agent{ docker {image 'python:3.11.5-slim'}}
            steps {
                sh 'python -m venv venv'
                sh 'source venv/bin/activate && pip install -r requirements.txt'
                sh 'source venv/bin/activate && python -m unittest discover -s tests -p "test_*.py"'
            }
        }

        stage('Build Container') {
            steps {
                sh 'docker build -t notebook_app .'
            }
        }

        stage('Deploy Container') {
            steps {
                sh 'docker run -d notebook_app'
            }
        }
    }
}
