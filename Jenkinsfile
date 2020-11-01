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
                sh 'python -m py_compile FinanceCalcs.py calcs.py'
                stash(name: 'compiled-results', includes: '*.py*')
            }
        }
        stage('Tests') {
            agent {
                docker {
                    image 'qnib/pytest'
                }
            }
            steps {
                echo "a ver si puede correr las pruebas"
                sh 'py.test --junit-xml test-reports/results test_calcs.py'
            }
            post {
                always {
                    junit 'test-reports/results'
                }
            }
        }
    }
}