import spacy
from spacy.matcher import PhraseMatcher

skills_set = [('.net', 'language'), ('2checkout', 'tool'), ('2d', 'skill'), ('3d', 'skill'), ('abap', 'language'),
              ('accord.net', 'framework'), ('acrobat', 'tool'), ('actionscript', 'language'),
              ('activision engine', 'tool'), ('ada', 'language'), ('adabas', 'tool'), ('adminer', 'tool'),
              ('ado.net', 'tool'), ('adobe', 'tool'), ('agile', 'skill'), ('ai', 'skill'), ('aix', 'tool'),
              ('ajax', 'tool'), ('alchemy', 'tool'), ('algol', 'language'), ('alice', 'language'), ('alipay', 'tool'),
              ('altibase', 'tool'), ('amazon athena', 'tool'), ('amazon emr', 'tool'), ('amazon keyspaces', 'tool'),
              ('amazon lumberyard', 'tool'), ('amazon machine learning', 'tool'), ('amazon pay', 'tool'),
              ('amazon quicksight', 'tool'), ('amazon rds', 'tool'), ('amazon redshift', 'tool'),
              ('amazon sagemaker', 'framework'), ('anaconda', 'framework'), ('analysis', 'skill'),
              ('analytics', 'skill'), ('analyzer', 'skill'), ('analyzing', 'skill'), ('android', 'framework'),
              ('android pay', 'tool'), ('android studio', 'tool'), ('angular', 'framework'),
              ('angular.js', 'framework'), ('angularjs', 'framework'), ('ansi', 'language'), ('ansible', 'tool'),
              ('ant', 'tool'), ('antivirus', 'tool'), ('apache', 'framework'), ('apache flink', 'framework'),
              ('apache kafka', 'framework'), ('apache spark', 'framework'), ('apache wicket', 'framework'),
              ('apexsql monitor', 'tool'), ('api', 'language'), ('apl', 'language'), ('app watch', 'framework'),
              ('appgamekit', 'tool'), ('appium', 'framework'), ('apple pay', 'tool'), ('applix', 'tool'),
              ('apps', 'skill'), ('appstore', 'tool'), ('appworx', 'tool'), ('ar', 'tool'), ('arcgis', 'framework'),
              ('arcgixb', 'framework'), ('architecting', 'skill'), ('archiving', 'skill'), ('arcsight', 'framework'),
              ('arduino', 'tool'), ('areva', 'framework'), ('arm', 'tool'), ('articulate', 'tool'),
              ('ascii', 'language'), ('asl', 'language'), ('asp', 'framework'), ('asp.net', 'framework'),
              ('asp.net core', 'framework'), ('assembly', 'language'), ('assembly language', 'language'),
              ('atom', 'language'), ('atom solidity linter', 'tool'), ('audacity', 'tool'), ('audit', 'framework'),
              ('authorize.net', 'tool'), ('autocad', 'tool'), ('autofac', 'framework'), ('automation', 'skill'),
              ('automl', 'tool'), ('autosys', 'tool'), ('avionics', 'tool'), ('awk', 'language'), ('aws', 'framework'),
              ('aws glue', 'tool'), ('aws lake formation', 'tool'), ('axure', 'tool'), ('azure', 'framework'),
              ('azure cosmos db', 'tool'), ('azure synapse analytics', 'tool'), ('baas', 'tool'),
              ('backbone.js', 'framework'), ('backbonejs', 'framework'), ('backdrop cms', 'tool'), ('backend', 'skill'),
              ('backtrack', 'tool'), ('bbc basic', 'language'), ('bi', 'tool'), ('bigml', 'framework'),
              ('bigquery', 'tool'), ('bios', 'tool'), ('bitbucket', 'tool'), ('blender', 'tool'),
              ('blizzard engine', 'framework'), ('blockchain', 'skill'), ('blockchain-as-a-service', 'tools'),
              ('bluesnap', 'tool'), ('bolt', 'tool'), ('bookshelf.js', 'framework'), ('bookshelfjs', 'framework'),
              ('bootstrap', 'language'), ('bottle', 'framework'), ('braintree', 'tool'), ('bridging', 'skill'),
              ('buildbox', 'tool'), ('c', 'language'), ('c#', 'language'), ('c++', 'language'), ('cabling', 'skill'),
              ('caffe', 'tool'), ('cakephp', 'language'), ('card.io', 'tool'), ('cd/ci', 'tool'), ('celtx', 'tool'),
              ('centos', 'tool'), ('cerberus x', 'tool'), ('cfr', 'framework'), ('cgi', 'framework'),
              ('cgs', 'framework'), ('cherrypy', 'framework'), ('cisco', 'tool'), ('cloud', 'tool'),
              ('cloudera', 'tool'), ('cmake', 'tool'), ('cmod', 'tool'), ('cms', 'tool'), ('cmvc', 'framework'),
              ('cobol', 'language'), ('cocoa', 'framework'), ('cocos2d', 'framework'), ('codeigniter', 'framework'),
              ('codeigniter', 'framework'), ('coldfusion', 'tool'), ('compiler', 'tool'), ('compiling', 'skill'),
              ('complexity', 'skill'), ('computer vision', 'skill'), ('computing', 'skill'), ('configuring', 'skill'),
              ('construct 3', 'language'), ('coral', 'tool'), ('coredata', 'framework'), ('corel', 'tool'),
              ('corona', 'framework'), ('cpanel', 'tool'), ('crm', 'tool'), ('cryengine', 'framework'),
              ('cryptography', 'tool'), ('cs5', 'tool'), ('css', 'language'), ('cuda', 'tool'), ('cuv', 'framework'),
              ('cxml', 'tool'), ('cyberark', 'tool'), ('cybersecurity', 'skill'), ('cygwin', 'tool'),
              ('dapper', 'framework'), ('dart', 'language'), ('data science', 'skill'), ('data warehouse', 'framework'),
              ('database', 'skill'), ('database concepts', 'skill'), ('databricks', 'framework'), ('datacamp', 'tool'),
              ('dataflex', 'tool'), ('datalab', 'tool'), ('datarobot', 'tool'), ('daz3d', 'tool'), ('db', 'skill'),
              ('db visualizer', 'tool'), ('db2', 'tool'), ('dbflow', 'tool'), ('dbms', 'tool'), ('dbschema', 'tool'),
              ('ddos', 'tool'), ('ddos', 'tool'), ('debian', 'tool'), ('debugging', 'skill'),
              ('deep learning', 'skill'), ('delphi', 'language'), ('deployment', 'skill'), ('deployment', 'skill'),
              ('designer', 'skill'), ('designing', 'skills'), ('desktop', 'skill'), ('devart', 'tool'),
              ('developer', 'skill'), ('development', 'skill'), ('devops', 'framework'), ('dhcp', 'skill'),
              ('dhtml', 'tool'), ('digital ocean', 'framework'), ('django', 'framework'), ('dlib', 'tool'),
              ('dns', 'skill'), ('docker', 'tool'), ('dockerizing', 'skill'), ('docking', 'skill'),
              ('doctrine', 'framework'), ('dojo', 'framework'), ('dos', 'tool'), ('dot-abi-cli', 'tool'),
              ('dotcms', 'tool'), ('dotnet', 'language'), ('dreamweaver', 'tool'), ('drupal', 'framework'),
              ('dsl', 'tool'), ('dudaone', 'tool'), ('dwolla', 'tool'), ('dynamics', 'skill'), ('dynamodb', 'tool'),
              ('e-check', 'tool'), ('easy ar', 'tool'), ('ec2', 'tool'), ('eclipse', 'tool'), ('edi', 'framework'),
              ('edifact', 'tool'), ('edifecs', 'tool'), ('edrms', 'framework'), ('eigrp', 'skill'),
              ('elastic search', 'tool'), ('elixir', 'language'), ('emass', 'tool'), ('embark', 'framework'),
              ('embedded', 'skill'), ('emr', 'framework'), ('ems', 'framework'), ('ems sql manager', 'tool'),
              ('encoding', 'skill'), ('encryption', 'skill'), ('engineering', 'skill'), ('ent', 'framework'),
              ('enterprise', 'language'), ('entity', 'framework'), ('entity framework', 'framework'),
              ('entity framework core', 'framework'), ('epicor', 'framework'), ('epm', 'tool'), ('erd', 'skill'),
              ('erlang', 'language'), ('erp', 'framework'), ('esm tools', 'tool'), ('eth fiddle', 'framework'),
              ('ethereum-abi-ui', 'framework'), ('ethereumj', 'framework'), ('ethereumjs vm', 'framework'),
              ('etherlime', 'framework'), ('ethernet', 'tool'), ('ethpm-spec', 'framework'), ('etl', 'tool'),
              ('express.js', 'framework'), ('extranet', 'tool'), ('f#', 'language'), ('farm', 'framework'),
              ('fastapi', 'framework'), ('filemaker', 'tool'), ('filenet', 'tool'), ('finance', 'tool'),
              ('firebase', 'tool'), ('firewall', 'skill'), ('firmware', 'tool'), ('flask', 'framework'),
              ('forth', 'language'), ('fortran', 'language'), ('framework', 'framework'), ('frontend', 'skill'),
              ('ftp', 'skill'), ('fuelphp', 'framework'), ('functional programming', 'skill'), ('fusion 2.5', 'tool'),
              ('gamebench', 'tool'), ('gamemaker studio 2', 'tool'), ('ganache', 'tool'), ('ganache cli', 'tool'),
              ('genome', 'tool'), ('gensim', 'framework'), ('geth', 'tool'), ('gideros', 'framework'),
              ('gis', 'framework'), ('git', 'tool'), ('github', 'tool'), ('gitlab', 'tool'), ('glueviz', 'tool'),
              ('go', 'language'), ('go ethereum', 'tool'), ('gocardless', 'tool'), ('godot', 'tool'),
              ('golang', 'language'), ('google bigquery', 'tool'), ('google cloud automl', 'tool'),
              ('google cloud bigtable', 'tool'), ('google cloud platform', 'framework'),
              ('google cloud spanner', 'tool'), ('google colab', 'tool'), ('gorm', 'tool'), ('graphdbgraphic', 'tool'),
              ('graphviz', 'tool'), ('groovy', 'language'), ('gui', 'tool'), ('hadoop', 'framework'),
              ('hadoop hdfs', 'tool'), ('haproxy', 'tool'), ('haskell', 'language'), ('haxe 4', 'language'),
              ('helix core', 'tool'), ('heroku', 'tool'), ('hibernate', 'tool'), ('houdini fx', 'tool'),
              ('html', 'language'), ('html5', 'language'), ('iaas', 'skill'), ('ibm db2', 'tool'),
              ('ibm db2 warehouse', 'framework'), ('ibm watson', 'tool'), ('icloud', 'tool'), ('idl', 'language'),
              ('iis', 'tool'), ('image processing', 'skill'), ('imap', 'skill'), ('implementation', 'skill'),
              ('incredibuild', 'tool'), ('infura', 'tool'), ('inpage', 'tool'), ('insight', 'framework'),
              ('installation', 'skill'), ('integrating', 'skill'), ('integration', 'skill'), ('interfaces', 'skill'),
              ('internet of things', 'skill'), ('intranet', 'tool'), ('intune', 'tool'), ('invision', 'tool'),
              ('ionic', 'framework'), ('ios', 'tool'), ('iot', 'skill'), ('ip', 'skill'), ('ipps', 'framework'),
              ('ipsec', 'skill'), ('ipv4', 'skill'), ('ipv6', 'skill'), ('irs', 'framework'), ('isdn', 'tool'),
              ('jamf', 'tool'), ('java', 'language'), ('javafx', 'language'), ('javascript', 'language'),
              ('javascript', 'language'), ('jdk', 'tool'), ('jenkins', 'tool'), ('jira', 'tool'), ('jit', 'tool'),
              ('joomla', 'tool'), ('jquery', 'language'), ('js', 'language'), ('jscript', 'language'),
              ('json', 'skill'), ('json rpc api', 'tool'), ('json-rpc', 'tool'), ('julia', 'language'),
              ('jupyter notebook', 'tool'), ('keras', 'framework'), ('kernel', 'tool'), ('knack', 'tool'),
              ('knime', 'tool'), ('kobiton', 'tool'), ('kotlin', 'language'), ('kubernetes', 'tool'), ('l2tp', 'skill'),
              ('lan', 'skill'), ('landesk', 'skill'), ('laravel', 'framework'), ('latex', 'tool'), ('ldap', 'skill'),
              ('lift', 'framework'), ('linq', 'framework'), ('linux', 'tool'), ('linux', 'tool'), ('liquidity', 'tool'),
              ('logic', 'skill'), ('logical', 'skill'), ('longrange', 'tool'), ('lua', 'language'), ('lync', 'tool'),
              ('mac os', 'tool'), ('machine learning', 'skill'), ('magento', 'tool'), ('mahout', 'tool'),
              ('management', 'skill'), ('marmalade', 'tool'), ('matlab', 'language'), ('maven', 'tool'),
              ('mean', 'skill'), ('memsql', 'tool'), ('mern', 'skill'), ('metamask', 'tool'), ('meteor', 'framework'),
              ('mevn', 'skill'), ('microsoft access', 'tool'), ('microsoft power bi', 'tool'),
              ('microsoft sql server', 'tool'), ('microsoft windows', 'tool'), ('middleware', 'tool'), ('mist', 'tool'),
              ('mixamo', 'tool'), ('mlflow', 'tool'), ('mlops', 'skill'), ('mlpack', 'tool'),
              ('mobile angular ui', 'framework'), ('mobincube', 'tool'), ('mojolicious', 'framework'),
              ('mongodb', 'tool'), ('monogame', 'framework'), ('ms access', 'tool'), ('ms dos', 'tool'),
              ('ms excel', 'tool'), ('ms exchange', 'tool'), ('ms sql', 'tool'), ('ms windows', 'tool'),
              ('ms word', 'tool'), ('ms.net', 'tool'), ('msxml', 'tool'), ('multitask', 'skill'),
              ('multitasking', 'skill'), ('multithread', 'skill'), ('multithreading', 'skill'), ('mvc', 'framework'),
              ('mvc 4', 'framework'), ('mvc 5', 'framework'), ('mvp', 'skill'), ('mvs', 'tool'), ('mvvm', 'skill'),
              ('my sql workbench', 'tool'), ('mysql', 'skill'), ('nat', 'skill'), ('nativescript', 'framework'),
              ('neo4j', 'tool'), ('netapp', 'tool'), ('netbeans', 'tool'), ('netcdf', 'skill'),
              ('nethereum', 'framework'), ('netiq', 'skill'), ('netsuite', 'tool'), ('netware', 'tool'),
              ('network', 'skill'), ('network programming', 'skill'), ('networking', 'skill'), ('next.js', 'framework'),
              ('nginx', 'tool'), ('nlp', 'skill'), ('nmap', 'tool'), ('node', 'skill'), ('node.js', 'framework'),
              ('nodejs', 'framework'), ('nosql', 'skill'), ('ntservers', 'tool'), ('numba', 'framework'),
              ('nxt-g', 'tool'), ('oauth', 'tool'), ('objection.js', 'tool'), ('objectionjs', 'tool'),
              ('objective-c', 'language'), ('objectivesql', 'framework'), ('odoo', 'skill'), ('office', 'tool'),
              ('office365', 'tool'), ('oim', 'tool'), ('olap', 'tool'), ('oltp', 'skill'), ('omb', 'tool'),
              ('oms', 'tool'), ('onsen ui', 'framework'), ('oop', 'skill'), ('open nn', 'framework'),
              ('openam', 'framework'), ('opencl', 'framework'), ('opencv', 'skill'), ('opengl', 'tool'),
              ('opengl', 'tool'), ('oracle', 'framework'), ('oracle autonomous warehouse', 'tool'),
              ('oracle rdbms', 'tool'), ('oracle7', 'skill'), ('oracle8', 'skill'), ('oracle8i', 'skill'),
              ('oracle9', 'skill'), ('oracle9i', 'skill'), ('oraclexml', 'tool'), ('orange3', 'tool'),
              ('orient db', 'tool'), ('orm', 'skill'), ('os', 'skill'), ('osi', 'skill'), ('paas', 'skill'),
              ('parity', 'skill'), ('pascal', 'language'), ('payjunction', 'tool'), ('paymotion', 'tool'),
              ('payoneer', 'tool'), ('paypal', 'tool'), ('paysimple', 'tool'), ('paytm', 'tool'), ('perl', 'language'),
              ('phaser', 'tool'), ('photoshop', 'tool'), ('php', 'language'), ('phpcms', 'skill'),
              ('phpmyadmin', 'tool'), ('pl/sql', 'tool'), ('pop3', 'skill'), ('populus', 'tool'), ('postgres', 'skill'),
              ('postgresql', 'skill'), ('postgressql', 'skill'), ('postman', 'tool'), ('postscript', 'language'),
              ('powerbi', 'tool'), ('powershell', 'tool'), ('ppoe', 'skill'), ('prediction', 'skill'),
              ('prolog', 'language'), ('prototype', 'skill'), ('prototyping', 'skill'), ('prysm', 'tool'),
              ('pure data', 'skill'), ('pusher', 'tool'), ('putty', 'tool'), ('pycharm', 'tool'),
              ('pyethereum', 'framework'), ('pygame', 'framework'), ('pylons', 'framework'), ('pyqt', 'tool'),
              ('pyspark', 'framework'), ('python', 'language'), ('pytorch', 'framework'), ('qa', 'skill'),
              ('qlik', 'tool'), ('qos', 'skill'), ('qtp', 'skill'), ('quality assurance', 'skill'),
              ('quixel bridge', 'tool'), ('r', 'language'), ('r&d', 'skill'), ('rabbitmq', 'tool'),
              ('raspberry pi', 'tool'), ('ravendb', 'skill'), ('rdbms', 'skill'), ('rdlc', 'skill'),
              ('react', 'framework'), ('react native', 'framework'), ('react.js', 'framework'),
              ('reactjs', 'framework'), ('reconfiguration', 'skill'), ('redhat', 'skill'), ('redshift', 'tool'),
              ('redux', 'framework'), ('remix ide', 'tool'), ('rest', 'skill'), ('rest framework', 'framework'),
              ('restapi', 'framework'), ('restful', 'framework'), ('robomongo', 'tool'), ('ror', 'language'),
              ('rpg maker', 'tool'), ('rsa', 'skill'), ('rstudio', 'tool'), ('rtp', 'skill'), ('ruby', 'language'),
              ('ruby on rails', 'language'), ('rust', 'language'), ('s3', 'tool'), ('salesforce', 'tool'),
              ('saml', 'language'), ('sandbox', 'tool'), ('sap', 'tool'), ('sap data warehouse cloud', 'tool'),
              ('sap sybase ase', 'tool'), ('sas', 'skill'), ('scala', 'language'), ('scalegrid', 'tool'),
              ('sccm', 'skill'), ('scikit-learn', 'framework'), ('scipy', 'framework'), ('scm', 'skill'),
              ('scom', 'skill'), ('scripting', 'skill'), ('scrum', 'skill'), ('scrum', 'skill'), ('scsi', 'tool'),
              ('scylladb', 'skill'), ('sdk', 'tool'), ('sdlcs', 'skill'), ('selenium', 'tool'),
              ('selenium web driver', 'tool'), ('seo', 'skill'), ('sequel pro', 'tool'), ('sequelize', 'skill'),
              ('server', 'tool'), ('servlet', 'skill'), ('servlets', 'skill'), ('sftp', 'skill'), ('sha', 'skill'),
              ('sharepoint', 'tool'), ('shell', 'tool'), ('shellscript', 'tool'), ('shellscripting', 'skill'),
              ('shopify', 'framework'), ('siebel', 'skill'), ('sila', 'skill'), ('silex', 'skill'), ('simula', 'tool'),
              ('siprnet', 'skill'), ('sitebuilder', 'tool'), ('sitecore', 'tool'), ('sklearn', 'framework'),
              ('skrill', 'skill'), ('sla', 'skill'), ('slaframework', 'framework'), ('smart contracts', 'skill'),
              ('smtp', 'skill'), ('snapmanager', 'tool'), ('snowflake', 'tool'), ('soapui', 'tool'),
              ('software assessment', 'skill'), ('software assessment management', 'tool'),
              ('software development', 'skill'), ('software production', 'skill'),
              ('software production management', 'skill'), ('software testing', 'skill'), ('solar2d', 'tool'),
              ('solaris', 'language'), ('solaris10', 'tool'), ('solaris8', 'tool'), ('solaris9', 'tool'),
              ('solarwinds', 'tool'), ('solc', 'tool'), ('solidity', 'language'), ('sop', 'skill'), ('sops', 'skill'),
              ('soql', 'skill'), ('spacy', 'tool'), ('spark', 'framework'), ('spatialos', 'tool'),
              ('speedtree', 'tool'), ('spreedly', 'tool'), ('springboot', 'framework'), ('spritkit', 'tool'),
              ('spss', 'skill'), ('spyder', 'tool'), ('sqa', 'skill'), ('sql', 'skill'), ('sql developer', 'skill'),
              ('sql sentry', 'tool'), ('sql server', 'tool'), ('sql server management studio', 'tool'),
              ('sql+.net', 'tool'), ('sqlalchemy', 'tool'), ('sqlite', 'skill'), ('sqlyog', 'tool'),
              ('sqr', 'language'), ('squarespace', 'tool'), ('srs', 'skill'), ('saas', 'skill'), ('ssis', 'skill'),
              ('ssl', 'skill'), ('ssp', 'skill'), ('ssrs', 'skill'), ('stackby', 'tool'), ('stata', 'tool'),
              ('stencyl', 'tool'), ('stlc', 'skill'), ('stp', 'skill'), ('stripe', 'tool'), ('subnetting', 'skill'),
              ('sugar orm', 'tool'), ('sunos', 'tool'), ('swift', 'language'), ('swiftic', 'tool'),
              ('symantec', 'tool'), ('symfony', 'framework'), ('synchronization', 'skill'), ('tableau', 'tool'),
              ('tableplus', 'tool'), ('tcl', 'language'), ('tcp', 'skill'), ('tcp/ip', 'skill'), ('tcpip', 'skill'),
              ('teamdesk', 'tool'), ('tencent engine', 'framework'), ('tensorflow', 'framework'), ('teradata', 'tool'),
              ('tex', 'tool'), ('theano', 'framework'), ('titanium', 'tool'), ('tk', 'tool'), ('tkinter', 'tool'),
              ('toad', 'tool'), ('truffle', 'tool'), ('tsql', 'skill'), ('turbogears', 'framework'),
              ('typescript', 'language'), ('typo3', 'tool'), ('ubuntu', 'tool'), ('ui', 'skill'), ('ui/ux', 'skill'),
              ('uml', 'skill'), ('unity', 'tool'), ('unix', 'tool'), ('unreal engine', 'framework'),
              ('urban airship', 'tool'), ('user testing', 'skill'), ('ux', 'skill'), ('vaadin', 'tool'),
              ('vb', 'skill'), ('vb basic .net', 'language'), ('vb.net', 'language'), ('vba', 'skill'),
              ('vbscript', 'language'), ('vdi', 'skill'), ('vdm', 'skill'), ('verilog', 'language'),
              ('vhdl', 'language'), ('visio', 'tool'), ('visual basic .net', 'language'), ('visualstudio.net', 'tool'),
              ('vlan', 'skill'), ('vmd', 'skill'), ('vms', 'tool'), ('voip', 'tool'), ('vpn', 'tool'), ('vps', 'skill'),
              ('vue.js', 'framework'), ('vuejs', 'framework'), ('vuforia', 'tool'), ('vyper', 'language'),
              ('wan', 'skill'), ('wap', 'language'), ('wap/wml', 'language'), ('web3', 'framework'),
              ('web3.js', 'language'), ('web3j', 'tool'), ('webgui', 'tool'), ('webmoney', 'tool'),
              ('websphere', 'tool'), ('weebly', 'tool'), ('weka', 'tool'), ('wepay', 'tool'), ('win32', 'tool'),
              ('winjs', 'tool'), ('winpython', 'tool'), ('wireshark', 'tool'), ('wix', 'tool'), ('wlan', 'skill'),
              ('wml', 'language'), ('wms', 'tool'), ('wordpress', 'skill'), ('workflow', 'skill'),
              ('workflows', 'skill'), ('worldpay', 'tool'), ('wsdl', 'language'), ('x++', 'language'),
              ('xamarin', 'tool'), ('xaml', 'language'), ('xcode', 'tool'), ('xhtml', 'language'), ('xml', 'language'),
              ('xmlrpc', 'tool'), ('xsl', 'language'), ('yola', 'tool'), ('python developer', 'skill'),
              ('.net developer', 'skill'), ('ios developer', 'skill'), ('android developer', 'skill'),
              ('django developer', 'skill'), ('web developer', 'skill'), ('blockchain developer', 'skill'),
              ('game developer', 'skill'), ('flutter developer', 'skill'), ('mobile application developer', 'skill'),
              ('user acceptance testing', 'skill'), ('software testers', 'skill')]

skills_set_dict = {}
for sk, sk_tag in skills_set:
    if sk_tag in skills_set_dict:
        skills_set_dict[sk_tag].append(sk)
    else:
        skills_set_dict[sk_tag] = [sk]

nlp = spacy.load("en_core_web_sm")


def phrase_matcher(data):
    doc = nlp(data)

    skills = [sk[0] for sk in skills_set]

    for i in range(len(skills)):
        skills[i] = skills[i].lower()

    # Initialize the PhraseMatcher
    matcher = PhraseMatcher(nlp.vocab)

    # Create pattern Doc objects and add them to the matcher
    # Use nlp.pipe() when processing large volumes of text
    patterns = list(nlp.pipe(skills))
    matcher.add("skills", patterns)

    # Call the matcher on the test document and print the result
    matches = matcher(doc)
    return [doc[start:end] for match_id, start, end in matches]


def tag_matcher(data):
    target = dict()

    requests = data.pop('requests')
    for key, value in data.items():
        if isinstance(value, str):
            target[key] = value

        elif isinstance(value, list):
            index = 1
            for instance in value:

                for _key, _value in instance.items():
                    target[f"{key}_{index}_{_key}"] = _value
                index += 1
    result_order = {}
    for request in requests:
        result = []
        for queries in request["queries"]:
            query = queries['query']
            final_res = {
                'tools': [],
                'languages': [],
                'frameworks': [],
                'skills': []
            }
            keywords = list(phrase_matcher(query.lower()))
            keywords = [str(keyword) for keyword in keywords]
            for k in keywords:
                if k in skills_set_dict['skill']:
                    final_res["skills"].append(k)
                elif k in skills_set_dict['tool']:
                    final_res["tools"].append(k)
                elif k in skills_set_dict['language']:
                    final_res["languages"].append(k)
                elif k in skills_set_dict['framework']:
                    final_res["frameworks"].append(k)
            # print(keywords)
            for i in range(1, len(data['experiences']) + 1):
                sentences = target[f"experiences_{i}_description"].lower().split('.')
                for sentence in sentences:
                    if any(i in sentence for i in keywords):
                        result.append(sentence)
            queries['result'] = result
            # print(queries)
            result_order[queries["sortOrder"]] = final_res
    return result_order
