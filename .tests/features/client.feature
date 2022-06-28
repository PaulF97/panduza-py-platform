# Feature: Client


#     @fixture.client.test
#     Scenario: A client must be created from url and port
#         Given the client "test" initialized with test broker url:"localhost" and port:"1883"
#         When  the client "test" start the connection
#         Then  the client "test" is connected


#     @fixture.client.test
#     Scenario: A client must be created from an alias
#         Given core aliases loaded with file "platform_alias.json"
#         And   a client "test" initialized with the mqtt test broker alias:"local_test"
#         When  the client "test" start the connection
#         Then  the client "test" is connected


#     @fixture.client.pub
#     @fixture.client.sub
#     Scenario: A client must be able to publish and subscribe to a mqtt topic
#         Given core aliases loaded with file "platform_alias.json"
#         And   a client "pub" initialized with the mqtt test broker alias:"local_test"
#         And   a client "sub" initialized with the mqtt test broker alias:"local_test"
#         When  the client "pub" start the connection
#         And   the client "sub" start the connection
#         When  the client "sub" subscribe to topic "test/topic"
#         Then  the client "sub" has "1" listener
#         When  the client "pub" send "foo" in topic "test/topic"
#         Then  the client "sub" has recieved "foo"
#         When  the client "sub" unsubscribe from the topic "test/topic"
#         Then  the client "sub" has "0" listener


#     @fixture.client.test
#     Scenario: A client must be able to unsubscribe just one callback
#         Given core aliases loaded with file "platform_alias.json"
#         And   a client "test" initialized with the mqtt test broker alias:"local_test"
#         When  the client "test" start the connection
#         When  the client "test" subscribe 3 callback to topic "test/topic" and unsubscribe 1
#         Then  the client "test" has "2" listener


#     @fixture.client.test
#     Scenario: A client must be able to scan interfaces
#         Given core aliases loaded with file "platform_alias.json"
#         And   a client "test" initialized with the mqtt test broker alias:"local_test"
#         When  the client "test" start the connection
#         When  the client "test" scan the interfaces
#         Then  at least a platform interface must be found

