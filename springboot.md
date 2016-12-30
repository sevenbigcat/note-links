# Microservices
## SpringBoot
### ConfigurationProperties
[Spring Boot Inject Map From Application Yml](http://stackoverflow.com/questions/24917194/spring-boot-inject-map-from-application-yml)

###24.4 Profile-specific properties
In addition to application.properties files, profile-specific properties can also be defined using the naming convention application-{profile}.properties. The Environment has a set of default profiles (by default [default]) which are used if no active profiles are set (i.e. if no profiles are explicitly activated then properties from application-default.properties are loaded).

Profile-specific properties are loaded from the same locations as standard application.properties, with profile-specific files always overriding the non-specific ones irrespective of whether the profile-specific files are inside or outside your packaged jar.

If several profiles are specified, a last wins strategy applies. For example, profiles specified by the spring.profiles.active property are added after those configured via the SpringApplication API and therefore take precedence.

[Note]
If you have specified any files in spring.config.location, profile-specific variants of those files will not be considered. Use directories in`spring.config.location` if you also want to also use profile-specific properties.
###24.5 Placeholders in properties
The values in application.properties are filtered through the existing Environment when they are used so you can refer back to previously defined values (e.g. from System properties).

app.name=MyApp
app.description=${app.name} is a Spring Boot application
