Feature: Client for broker connection

    Scenario Outline: A client must be created from url and port
        Given a client created with the mqtt test broker url:"<url>" and port:"<port>"
        When the client start the connection
        Then the client is connected

    Examples: Test broker
        | url           | port          |
        | localhost     | 1883          |


