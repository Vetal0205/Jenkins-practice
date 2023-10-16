pipeline {
    agent {
        docker {
            image 'python:3.8'
            args '-v /var/run/docker.sock:/var/run/docker.sock' // Mount Docker socket
        }
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build and Test') {
            steps {
                sh 'python -m venv venv'
                sh 'source venv/bin/activate && pip install -r requirements.txt'
                sh 'source venv/bin/activate && python -m unittest discover -s tests -p "test_*.py"'
            }
        }

        stage('Build Container') {
            steps {
                sh 'docker build -t my_notebook_app .'
            }
        }

        stage('Deploy Container') {
            steps {
                sh 'docker run -d -p 8080:8080 my_notebook_app'
            }
        }
    }
}
