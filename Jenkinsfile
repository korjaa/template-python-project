pipeline {
  agent { docker { image 'python:3.7.4' } }
  stages {
    stage('build') {
      steps {
        sh 'pip install .'
      }
    }
    stage('test') {
      steps {
        sh 'python -m unittest'
      }
    }
  }
}
