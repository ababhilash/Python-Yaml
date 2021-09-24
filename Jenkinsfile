import org.yaml.snakeyaml.Yaml
import org.yaml.snakeyaml.DumperOptions
import static org.yaml.snakeyaml.DumperOptions.FlowStyle.BLOCK

pipeline {
    agent any
    stages{
        stage ('SCM chkout-1'){
            steps{
                git branch: 'main', credentialsId: 'b7bb71f2-0269-4e2c-b855-edceee0ba06f', url: 'https://github.com/ababhilash/Python-Yaml'
            }
        }
        stage ("Dynamically write dictionary variables") {
            steps{
                def amap = ['something': 'my datas', 'size': 3, 'isEmpty': false]
                writeYaml file: 'items.yaml', data: amap
                def read = readYaml file: 'items.yaml'

                assert read.something == 'my datas'
                assert read.size == 3
                assert read.isEmpty == false
            }
        }
        stage ("Print the contents of yaml file") {
            steps{
                sh "python3 data.py"
            }    
        }    
    }
}
