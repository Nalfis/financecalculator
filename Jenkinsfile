pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:2-alpine'
                }
            }
            steps{
                echo "Compilando los dos programitas"
                sh 'python -m py_compile calcs.py'
                stash(name: 'compiled-results', includes: '*.py*')
            }
        }
    }
}