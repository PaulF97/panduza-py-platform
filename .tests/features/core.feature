Feature: Core


    Scenario Outline: Aliases can be configured from file
        When aliases "<file>" are loaded into the core
        Then each connection and aliases are declared

        Examples: Tricky files
        | file                      |
        | io_tree.json              |
#        | aliases_empty_file.json   |
#        | aliases_empty_object.json |


