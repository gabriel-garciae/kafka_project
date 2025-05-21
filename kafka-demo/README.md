# Exercise of configuration and production of message

## Prerequisites

1. **Confluent Cloud Cluster:** Make sure you have configured the Confluent Cloud Cluster and CLI according to the previous exercises.
2. **Kafka CLI:** Have the Kafka CLI installed and configured to connect to your Confluent Cloud cluster.

## Exercise Steps

### 1. Create an account on confluent cloud
- Go to the [Confluent Cloud URL](https://confluent.cloud).
- Enter your name, email, and password.
- click the "Start Free" button and wait to receive a confirmation email.
- Confirm your email to proceed with the cluster creation.

### 2. Configure the cluster
- After confirming your email, follow the instructions to set up your cluster.
- Choose between a basic, standard, or dedicated cluster. For this exercise, choose the basic cluster.

### 3. Apply promotional code
- Navigate to "Settings" > "Billing and Payment".
- Enter the promotional code <kafka101> to get an additional $101 in free usage.

### 4. Create a topic

#### Create a topic using the web interface
- On the Confluent Cloud home page, select the "Topics" tab.
- Click "Create Topic" and name the topic tecnologias.
- Keep the default number of partitions (6) and create the topic.

#### Create a topic using the CLI
- In the terminal, after configuring the CLI as shown in the next steps, create a topic:

    ```bash
    confluent kafka topic create tecnologias --partitions 6
    ```

### 5. Produce messages using the web interface
- Navigate to the "Messages" tab to view real-time message production and consumption.
- Click on "Produce a new message to this topic".
- Enter 1 as the key and Python as the value, then click "Produce".

### 6. Configure the command line interface (CLI)
- On the Confluent Cloud page, go to "CLI and Tools" to download and configure the command-line tools.
- In the terminal, log in to Confluent Cloud:

    ```bash
    confluent login --save
    ```

- Use the same email and password you used to create your account.

### 7. Select environment and cluster
- List the available environments:

    ```bash
    confluent environment list
    ```

- Use the default environment ID:

    ```bash
    confluent environment use <environment_id>
    ```

- List the available Kafka clusters:

    ```bash
    confluent kafka cluster list
    ```

- Use the cluster ID:

    ```bash
    confluent kafka cluster use <cluster_id>
    ```

### 8. Create and configure API Key
- Create an API key:

    ```bash
    confluent api-key create --resource <cluster_id>
    ```

- Save the provided API key and secret.
- Use the API key:

    ```bash
    confluent api-key use <api_key> --resource <cluster_id>
    ```

### 9. Produce messages using the CLI
- List the available topics:

    ```bash
    confluent kafka topic list
    ```

- To produce messages to the "tecnologias" topic, open a CLI terminal and run:

    ```bash
    confluent kafka topic produce tecnologias
    ```

- At the prompt, enter one message at a time and press Enter:

    ```plaintext
    1:Python
    2:SQL
    3:Kafka
    4:Spark
    5:Airflow
    6:Kubernetes
    7:Terraform
    8:Docker
    ```

### 10. Consume messages using the CLI
- Open another CLI terminal to consume messages from the beginning of the topic:

    ```bash
    confluent kafka topic consume tecnologias --from-beginning
    ```

### 11. Check messages in the web console
- Go back to the Confluent Cloud web interface and check the produced messages.
- To view messages in the web interface, set the offset to zero and check each partition.

### Conclusion

If you followed all the steps, you completed several important activities:
- Created an account on Confluent Cloud and configured your first Kafka cluster.
- Created a topic and produced messages using the web interface.
- Installed the CLI, created an API key, and produced/consumed messages using the CLI.

### References
- [Confluent Cloud Documentation](https://docs.confluent.io/cloud/current/get-started/index.html)
- [Kafka Documentation](https://kafka.apache.org/documentation/)
- [Luciano Galvão, BR version](https://github.com/lvgalvao/kafka-workshop/blame/main/kafka-demo/README.md)

---