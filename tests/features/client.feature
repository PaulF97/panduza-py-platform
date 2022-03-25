Feature: Client

    @fixture.client.test
    Scenario: A client must be created from url and port
        Given the client "test" initialized with test broker url:"localhost" and port:"1883"
        When the client "test" start the connection
        Then the client "test" is connected

    @fixture.client.test
    Scenario: A client must be created from an alias
        Given core aliases loaded with file "platform_alias.json"
        And a client "test" initialized with the mqtt test broker alias:"local_test"
        When the client "test" start the connection
        Then the client "test" is connected

    @fixture.client.pub
    @fixture.client.sub
    Scenario: A client must be able to publish and subscribe to a mqtt topic
        Given core aliases loaded with file "platform_alias.json"
        And a client "pub" initialized with the mqtt test broker alias:"local_test"
        And a client "sub" initialized with the mqtt test broker alias:"local_test"
        When the client "pub" start the connection
        And  the client "sub" start the connection
        # When the client "test" start the connection
        # When the client "test" scan the interfaces
        # Then at least a platform interface must be found

    @fixture.client.test
    Scenario: A client must be able to scan interfaces
        Given core aliases loaded with file "platform_alias.json"
        And a client "test" initialized with the mqtt test broker alias:"local_test"
        When the client "test" start the connection
        When the client "test" scan the interfaces
        Then at least a platform interface must be found

