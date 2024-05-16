1.	Introduction
1.1	Problem Statement
Network security is becoming a major issue for both people and enterprises in today's connected community. With our growing dependence on the internet and the increasing prevalence of cyberthreats, it is critical to protect networks against attacks and unauthorized access. Traditional firewalls may be very expensive and complicated. The goal of this project is to create a simple (Basic), easy-to-use packet filtering firewall. A complete security package could be very expensive for small networks or personal PCs, in which case our lightweight option is ideal. It is now essential to have an expandable and adaptable firewall system that can efficiently filter network traffic according to user-defined rules.
This project's main goal is to create a basic firewall that can filter packets according to a set of user-defined rules. Users should be able to define rules that regulate how incoming and outgoing network traffic is filtered by the firewall, giving them exact control over the kinds of connections and protocols that are allowed or prohibited. To analyze and filter packets based on their source IP addresses, destination IP addresses, port numbers, and protocol types, the firewall needs be built to function at the network layer.
1.2	Product Scope
The goal of the basic firewall project is to provide software that offers an adaptable and configurable packet filtering system. By allowing users to create rules that define when network traffic should be allowed or blocked, the firewall will improve network management and security.
The fundamental firewall's main attributes and advantages are as follows:

•	Packet filtering: Using user-defined rules, the firewall examines and filters network packets, permitting or prohibiting traffic depending on predetermined standards such IP addresses, port numbers, and protocol types.

•	Rule Configuration: Through a command-line interface, users will be able to add, edit, and remove rules, giving them freedom in designing and controlling the behavior of the firewall.

•	Traffic Monitoring: Users may keep an eye on and examine network activity thanks to the firewall's logging and reporting of all network traffic, including connections that are approved and rejected.

•	Extension: Because of its modular architecture, the firewall may handle more protocols and sophisticated filtering methods in the future.

The larger objectives of improving network security and giving users more control over their network traffic are in line with the fundamental firewall effort. The initiative addresses the unique demands of small companies and individuals looking to adopt strong security measures with flexibility by providing a solution that can be customized.
1.3	Project Report Structure
The remainder of this report is organized as follows:
•	Chapter 2: Methodology - Describes the requirements, analysis, design, implementation, and testing methodologies employed in the development of the basic firewall.
•	Chapter 3: Evaluation - Assesses the project results, discusses lessons learned, and outlines potential future work.
•	Chapter 4: Conclusion - Summarizes the project's achievements, highlights its significance, and provides concluding remarks.
•	Chapter 5: References - Lists the sources cited throughout the report.
•	Appendix A: Test Results - Presents additional test results and supporting documentation.

2.	Methodology
2.1	Requirements and Analysis
A systematic approach was taken in the creation of the basic firewall project, which started with an in-depth analysis of the requirements and use cases. The following requirements were identified for the packet filtering firewall:

•	Packet Filtering: Network packets must be able to be analyzed and filtered by the firewall using user-defined rules.
•	Rule Management: A command-line interface should allow users to add, edit, and remove rules.
•	Traffic Monitoring: Network traffic, including permitted and prohibited connections, should be recorded, and reported by the firewall.

Functional Requirements,
o	The ability to parse packet headers (IP, TCP/UDP) and capture raw network packets.
o	The ability to set rules according to protocols, ports, source/destination IP addresses, and directions.
o	system to permit or prohibit traffic according to established rules.

Non-Functional Requirements,
o	User-friendly interface for configuring firewall rules.
o	Efficient packet processing for minimal network performance impact.
o	Portability to run on different operating systems.

Created the activity diagram to show how the firewall works and how to connect.

2.2	Design
A system of modules is used by the basic firewall, which consists of many separate components that operate in unison. The Packet Capture Engine, located at the center, is in charge of intercepting network packets from the assigned interface. The Packet Parser receives these intercepted packets and uses them to extract important information like protocol types, ports, and IP addresses. The retrieved packet data is next examined by the Rule Engine, which does an analysis between it and a create of firewall rules that the user has established. The Rule Engine decides whether to allow or block each packet based on this rule matching process. The Action Engine component carries out the decision made by the Rule Engine. To successfully prohibit unintentional network activity, packets that match rules allowing traffic are permitted to continue their path, while those that do not comply with the rules are deleted. The User Interface component offers an intuitive interface to make rule maintenance and traffic monitoring easier. Administrators may set up firewall rules, examine reports and logs that list permitted and prohibited connections, and more using this interface. This modular design encourages maintainability, extensibility, and structure of the code, making it possible for the firewall to successfully adjust to evolving security requirements and requirements.

2.3	Implementation
Creating a functional software solution from the design was the task of the implementation phase. The following instruments and technologies were used:

•	Programming Language: Python
•	Development Environment: Linux OS, Visual Studio Code
•	Libraries and Frameworks: socket, struct, ctypes

•	socket: Enables raw socket communication for capturing network packets.
•	struct: Assists in unpacking binary data from packet headers.
•	ctypes: Facilitates interaction with C libraries for network interface card (NIC) access.
•	threading: Enables efficient handling of concurrent tasks like packet capture and rule processing.

•	send function: Transmits a packet to the designated destination IP address.
•	chack function: Checks a packet against the configured firewall rules and returns an allow/deny decision.
•	bind function: Binds the firewall to a specific network interface and initiates the packet capture and processing loop.

The implementation was done in a modular fashion, with distinct modules for rule management and packet inspection. Throughout the development process, best practices and reusable code were used to guarantee the quality and maintainability of the code.

2.4	Testing
Validating the firewall's dependability and performance required a thorough testing methodology. To ensure that modules such as packet capture, parsing, and rule matching are proper, unit testing thoroughly investigated each module separately. Data flow and efficient rule enforcement were guaranteed by the smooth interaction between modules, which was validated by integration testing. System testing assessed the firewall's overall functionality by simulating network environments and evaluating situations including allowing valid traffic, preventing malicious behavior, and managing rule conflicts. Throughout the development process, these thorough testing made that the firewall was functioning, dependable, and effective at protecting network security and integrity.

3.	Evaluation
3.1	Assessment of the Project results
The designed firewall accomplishes its main goals with success. In order to filter traffic, it parses headers, collects network packets, and applies user-defined rules. The user interface facilitates easy configuration, while the algorithms employed offer effective packet processing.

Limitations:

•	As the firewall depends on simple packet filtering, it is vulnerable to advanced attacks that take advantage of holes in more complex protocols.
•	Limited logging capability makes it difficult to do in-depth security analysis.
•	Networks with a lot of traffic may need performance tuning.
•	Although the command-line interface serves its purpose, adding a graphical user interface (GUI) would enhance the user experience in general and increase the firewall's accessibility for users with different levels of technical expertise.
3.2	Lessons Learned
This research gave me insightful knowledge about packet filtering methods and network security ideas. The significance of establishing thorough and unambiguous firewall rules in order to achieve optimal security. the compromise made while building a firewall between performance and security. realizing that in order to keep up with changing threats, firewall rules must be updated and monitored on a regular basis.

3.3	Future Work
•	Using deep packet inspection tools to find potentially harmful material in packets.
•	Including intrusion detection and prevention technologies in order to provide superior security against threats.
•	Creating sophisticated reporting and recording features for in-depth security investigation.
•	Investigating methods for managing network settings with heavy traffic and performance optimization.
•	Putting a graphical user interface into practice to improve usability.

Conclusion
This project's main goal was to create a working firewall application that could monitor over and filter network traffic according to rules that the user had created. Python's raw socket programming skills were successfully applied for this purpose. Through a command-line interface, the created firewall configure helps users to add, edit, and remove firewall rules. A rule can be defined according to a number of criteria, such as protocol number, source and destination IP addresses, source and destination ports, and actions (allow or reject). Based on these criteria, the program effectively filters packets and sends or drops them as necessary. This firewall application's simplicity and convenience of use are among its main advantages. Users with differing degrees of technical proficiency may easily manage firewall rules with the help of the command-line interface. The program's adaptability and suitability for various network contexts are further increased by its capacity to operate concurrently on several network interfaces. The current approach is not without its restrictions, though. To begin with, the program does not enable advanced functions like stateful packet inspection, which might enhance its security capabilities. Furthermore, people who are more used to visual interfaces may find it less intuitive in the lack of a graphical user interface (GUI). Future development might entail designing a user-friendly GUI and adding stateful packet inspection features to solve these constraints and further improve the firewall application. Furthermore, the program may be expanded to accommodate more sophisticated functions such interaction with other network security tools, virtual private network (VPN) capabilities, and intrusion detection and prevention systems (IDS/IPS).
Overall, this project proved that utilizing Python and raw socket programming to create a firewall application is feasible. The resultant program offers a strong framework for filtering and monitoring network traffic, with room for future development and integration with additional security tools. This firewall program might develop into a more powerful and all-encompassing network security solution by resolving the noted limitations and adding new capabilities. This would help enterprises by strengthening their network security posture and fending off possible attacks.

