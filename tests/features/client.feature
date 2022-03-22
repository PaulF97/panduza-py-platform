Feature: Client

    Scenario Outline: A client must be created from url and port
        Given a client created with the mqtt test broker url:"<url>" and port:"<port>"
        When the client start the connection
        Then the client is connected

    Examples: Local Broker
        | url           | port          |
        | localhost     | 1883          |


    Scenario Outline: A client must be created from an alias
        Given aliases from the file:"<file>"
        And a client created with the mqtt test broker alias:"<alias>"
        When the client start the connection
        Then the client is connected

    Examples: Local Broker
        | file                      | alias                 |
        | aliases_test_01.json      | local_test            |


