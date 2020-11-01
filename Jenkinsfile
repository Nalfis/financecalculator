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
                sh 'python -m py_compile FinanceCalcs.py calcs.py finance.py'
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
        stage('Deploy') {
            agent any
            environment {
                VOLUME = '$(pwd)/:/src'
                IMAGE = 'cdrx/pyinstaller-linux:python3'
            }
            steps{
                dir(path: env.build_ID) {
                    unstash(name: 'compiled-results')
                    echo "compilando..."
                    sh "docker run --rm -v ${VOLUME} ${IMAGE} 'pyinstaller -F finance.py'"
                }
            }
            post {
                success {
                    echo "Limpiando el folder con la application empaquetada"
                    archiveArtifacts "${env.BUILD_ID}/dist/"
                    sh "docker run --rm -v ${VOLUME} ${IMAGE} 'rm -rf build dist'"
                }
            }
        }
    }
}