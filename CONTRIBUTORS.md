# Contributors
Hello there, welcome.

We're super excited that you're thinking of contributing, and helping improve this project.
This project strives to help provide a structured learning pathway, and mappings of core concepts in Application Security for the community. 

We're all volunteers here, and we can only do so much in our spare time to make this world a little better. To help this project keep doing that, we all understand that by submitting a pull request agree to release your submission under Creative Commons Attribution-ShareAlike v4.0 to the OWASP Foundation, and that you had the rights to do so.

## Getting Started

Contributions are being accepted via Pull Requests to this repository.
If you are new to contributing via GitHub, Digital Ocean has [a pretty good guide](https://www.digitalocean.com/community/tutorials/how-to-create-a-pull-request-on-github) on how this works. If you need a primer on [how to use Git](https://docs.github.com/en/github/using-git), GitHub has some excellent guides.

Once a Pull Request is created, please allow a few days for the repository maintainers to review your submission. If you don't hear from us (in over a week), please reach out to us on the OWASP Slack in the #education-committee channel.

### Conventions and Norms

- [ TO DO ]
.


### What can I help with?

Well, we're glad you asked. Thank you.
Here are some suggestions, of things we need help with. Not a complete list, but, a start.

- [STUFF TODO]


# About this Repository
## Background

To help identify the skills, and knowledge that is needed to perform the role of an Application Security Professional, we first look to the expected outcomes of such an individual. The clearest form these expectations are articulated are as Application Security Standards.

The best example of a well adopted framework within the OWASP Foundation is the Application Security Verification Standard (ASVS). Through tight collaboration and support from the team behind the ASVS, it was elected as the first source standard that will inform this curriculum.

To ensure the longevity and continued evolution of this project to fulfill the continually evolving needs and landscape of Application Security, we've taken a methododical approach, with an aspiration towards increased automation, to utilise multiple standards as sources to inform the outcome curriculum.

Think of this as a mapping of AppSec Standards against [Bloom's Taxanomy](https://en.wikipedia.org/wiki/Bloom%27s_taxonomy) to help inform the level of educational learning objective a person needs to achieve to perform a specified task. As such some understanding of Bloom's taxonomy is going to be needed. Here are some resources; [BloomsTaxonomy.net](https://www.bloomstaxonomy.net/) and [[Wikipedia](https://en.wikipedia.org/wiki/Bloom%27s_taxonomy).

.

### The Repository Structure
The original source content (eg. ASVS) files are pulled from the project's source repository into the `src` directory. These source text files are then transformed into the corresponding `.yaml` files in `current` using the the scripts stored in `src`.

Here's an overview of the repository structure:
```
➜  Application-Security-Curriculum git:(master) tree
.
├── README.md
├── current
│   └── asvs.yaml
├── scripts
│   └── generate-curriculum.py
└── src
    └── asvs-4.0.2-en.txt

```

To provide educational guidance, we map each item of knowledge that needs to be taught from the `actions` to the level that needs to be taught/understood using [Bloom's Taxonomy](https://www.psia-nw.org/blooms-taxonomy-levels-of-understanding/). 

![Bloom's Taxanomy](https://www.bloomstaxonomy.net/application/files/thumbnails/large/3315/8103/5712/Blooms-Taxonomy-650x366.jpg)

In the data structure representing the `units` to be taught (shown in later sections) we use the representation where 
    level `1` = `remember`, and 
    level `6' = `create`



### What to do

You will need to locate the source `.yaml` file, that the script has generated. In this case, the `asvs.yaml` file in the `current` folder.

Transformation script outputs the follow:
```
-
    chapter_id: V2
    module: Authentication
    chapter_name: Authentication Verification Requirements
    section_id: V2.5
    section_name: Credential Recovery Requirements
    req_id: V2.5.1
    req_description: Verify that a system generated initial activation or recovery secret is not sent in clear text to the user. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering))
    level1: ✓
    level2: ✓
    level3: ✓
    cwe: 640
    nist: 5.1.1.2
```

The `contribution` focus right now is to add the following to the above.
```
    units:
        -
            unit: ''
            terms: ''
            level: 
    actions:
        -
            action: ''
            level: 
            mappings:
                -
    notes: ''
```
So that the stucture is expanded like this example below:
```
    chapter_id: V2
    module: Authentication
    chapter_name: Authentication Verification Requirements
    section_id: V2.5
    section_name: Credential Recovery Requirements
    req_id: V2.5.1
    req_description: Verify that a system generated initial activation or recovery secret is not sent in clear text to the user. ([C6](https://owasp.org/www-project-proactive-controls/#div-numbering))
    level1: ✓
    level2: ✓
    level3: ✓
    cwe: 640
    nist: 5.1.1.2
    units:
        -
            unit: ''
            terms: ''
            level: 
    actions:
        -
            action: ''
            level: 
            mappings:
                -
    notes: ''
```

The above forms the skeleton for each "requirement" for the ASVS standard.

Next, for each requirement, we'll need to deconstruct the requirements, so that we map them to corresponding learning `units`, such as the shown in the snippet below:

```
-
    chapter_id: V1
    module: Designing a Secure System
    chapter_name: Architecture, Design and Threat Modeling Requirements
    section_id: V1.5
    section_name: Input and Output Architectural Requirements
    req_id: V1.5.2
    req_description: Verify that serialization is not used when communicating with untrusted clients. If this is not possible, ensure that adequate integrity controls (and possibly encryption if sensitive data is sent) are enforced to prevent deserialization attacks including object injection.
    level1:
    level2: ✓
    level3: ✓
    cwe: 502
    nist:
    units:
        -
            unit: 'Data Security'
            terms: 
                - 'serialization'
                - 'deserialization'
                - 'integrity controls'
                - 'encryption'
                - 'sensitive data'
            level: 5
        -
            unit: 'Network Security'
            terms: 
                - 'communicating with untrusted clients'
                - 'encryption'
            level: 5
        -
            unit: 'Attack Types'
            terms: 
                - 'deserialization attacks'
                - 'object injection'
            level: 5
    actions:
        -
            action: 'Verify that serialization is not used'
            level: 2
            mappings:
                - 'Data Security'
                - 'Network Security'
        -
            action: 'ensure that adequate'
            level: 5
            mappings:
                - 'Data Security'
                - 'Network Security'
                - 'Attack Types'
            notes: 'We should define "adequate controls" for using serialization with untrusted client, most likely referring to separate guidance from OWASP.'
```

Here's the current recommended approach to creating the necessary information.
(If you have pedagogy background, we welcome your improvements) 

Using the example above this, we look at the `req_description` to determine the actions required of the person implementing the controls or the person reviewing it.

Breaking down the requirements description:
```
Verify that serialization is not used when communicating with untrusted clients. If this is not possible, ensure that adequate integrity controls (and possibly encryption if sensitive data is sent) are enforced to prevent deserialization attacks including object injection.
```

We first identify the actions needed :
Action 1: `Verify that serialization is not used` 
Action 2: `... ensure that adequate ...`

Create a new action stub for each action identified.
`action:`
```
        -
            action: ''
            level: 
            mappings:
                -
```
Based on the verbs being used, referencing Blooms' Taxonomy, and your AppSec knowledge, identify the minimum level of knowledge require to perform the task. 

Using `Action 1` as the example, we identify it to be a Level 2. 
To successfully complete this action, the person only needs to be able to identify, recognise, and classify that "serialization" is used. 

Thus, apply the number 2 label, as shown below:
```
    actions:
        -
            action: 'Verify that serialization is not used'
            level: 2
            mappings:
                - 
```

Next, we need to identify the `mappings`.
These are predefined `units` that these actions are being "mapped" to.
Refer to this mapping file (TODO @rewtd), for the list of units available to use.

Based on your current understanding, list all relevant units that apply to that "action" from the mapping list.

In this example, with the relevant study "units" (topics) we produce the following:
```
        -
            action: 'Verify that serialization is not used'
            level: 2
            mappings:
                - 'Data Security'
                - 'Network Security'
```

Repeat this process until all actions are mapped. 
If there's any judgement calls, ambiguity and/or other notes, do add a notes section to the action.


Then we move on to identifying the "units" and the knowledge level that needs to be acquired to fulfill the requirements.

Taking a look at the `units` section:
```
    units:
        -
            unit: 'Data Security'
            terms: 
                - 'serialization'
                - 'deserialization'
                - 'integrity controls'
                - 'encryption'
                - 'sensitive data'
            level: 5
        -
            unit: 'Network Security'
            terms: 
                - 'communicating with untrusted clients'
                - 'encryption'
            level: 5
        -
            unit: 'Attack Types'
            terms: 
                - 'deserialization attacks'
                - 'object injection'
            level: 5
```

From the `actions` that needs to be taken by the person executing this requirement, we identify 3 `units` (topics) that need to be taught.

They are `Data Security`, `Network Security` and `Attack Types`.
Across all the `actions`, identify the key terms/phrases that appears in the requirements that relates to the corresponding topic. To identify the relevant terms, look at the text, identify the adverbs and nouns that define the scope of the statement. In the example above, they are:

    - 'serialization'
    - 'deserialization'
    - 'integrity controls'
    - 'encryption'
    - 'sensitive data'
    - 'communicating with untrusted clients'
    - 'encryption'
    - 'deserialization attacks'
    - 'object injection'

Take for example, `Network Security`. In the text we identify the key phrases, `communicating with untrusted clients` and `encryption`. This maps onto the `units` section like this:
```
    -    
        unit: 'Network Security'
            terms: 
                - 'communicating with untrusted clients'
                - 'encryption'
```
Repeat this for all `action`, and until all `unit` are done.

Now, for the last bit. Looking back at the `action` that references a the `unit`, look for the highest level of knowledge required across all `unit` for this requirement. This will identify the highest level of knowledge required to fulfil this requirement and all the corresponding actions.

Following the `Network Security` example, we identify that the highest level across all `action` is Level 5. So, we assign level 5 to this `unit` as follow: 

```
        -
            unit: 'Network Security'
            terms: 
                - 'communicating with untrusted clients'
                - 'encryption'
            level: 5
```
Repeat until all `unit` is complete.
Repeat until all requirements for the standard has been mapped.

In short, the whole process is basically
```
Action words -> Blooms level req to do the action -> determine to highest bloom level to req understand.
Terms  - groups together the knowledge required --^
```
This then produces a list of "Units" with corresponding levels of knowledge required to accomplish requirements of ASVS.

It's a bit repetitive.
If you've got a way to automate this process reliably, please do reach out.

Thanks heaps for contributing.


TODO: Keywords Mapping to be provided by @rewtd 


# Notes & References

- https://www.teachthought.com/learning/a-simplified-blooms-taxonomy-poster-for-students/
- https://www.celt.iastate.edu/teaching/effective-teaching-practices/revised-blooms-taxonomy/blooms-revised-taxonomy-model/


# Thank you
## For authoring contributions

- rewtd
- hellodanielting



## For other supporting contributions

- organsation name here - contribution [date]
