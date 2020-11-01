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
                sh 'python -m py_compile common/FinanceCalcs.py calcs.py'
                stash(name: 'compiled-results', includes: 'sources/*.py*')
            }
        }
        stage('Test') {
            agent {
                docker {
                    image 'qnib/pytest'
                }
            }
            steps {
                echo "usando pruebas para confirmar que la application sirve"
                sh 'py.test --junit-xml test-reports/results.xml tests/test_calcs.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
       /* stage('Deploy') {
            agent any
            environment {
                VOLUME = '$(pwd)/sources:/src'
                IMAGE = 'cdrx/pyinstaller-linux:python3'
            }
            steps{
                dir(path: env.build_ID) {
                    unstash(name: 'compiled-results')
                    echo "compilando..."
                    sh "docker run --rm -v ${VOLUME} ${IMAGE} 'pyinstaller -F calcs.py'"
                }
            }
            post {
                success {
                    echo "Limpiando el folder con la application empaquetada"
                    archiveArtifacts "${env.BUILD_ID}/sources/dist/calcs"
                    sh "docker run --rm -v ${VOLUME} ${IMAGE} 'rm -rf build dist'"
                }
            } */
        }
    }
}