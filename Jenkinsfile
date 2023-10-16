pipeline {
    options { timestamps() }

    agent none
    stages {
        stage('Check scm') {
            agent any
            steps {
                checkout scm
            }
        }
        stage('Test') {
            agent { docker { image 'alpine' args '-u=\"root\"' } }
            steps {
                sh 'apk add --update python3 py-pip'
                sh 'pip install logging'
                sh 'pip install xmlrunner'
                sh 'python3 test_note_book.py'
            }
            post {
                always {
                    junit 'Test-Reports/*.xml'
                }
                success {
                    echo "Application testing successfully completed "
                }
                failure {
                    echo "Ooopps!!! Tests failed!"
                }
            }
        }
    }
}
