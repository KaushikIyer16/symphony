from textwrap import dedent

task_generation_examples=[
  {
    "objective": "Look up AI news from today (May 27, 2023) and write a poem.",
    "taskList": dedent("""
    [
  {{\"id\":1,\"task\":\"AI news today\",\"tool\":\"web-search\",\"dependent_task_ids\":[],\"status\":\"incomplete\",\"result\":null,\"result_summary\":null}},
  {{\"id\":2,\"task\":\"Summarize a news article\",\"tool\":\"text-completion\",\"dependent_task_ids\":[1],\"status\":\"incomplete\",\"result\":null,\"result_summary\":null}},
  {{\"id\":3,\"task\":\"Pick up important news\",\"tool\":\"text-completion\",\"dependent_task_ids\":[2],\"status\":\"incomplete\",\"result\":null,\"result_summary\":null}},
  {{\"id\":4,\"task\":\"Final summary report\",\"tool\":\"text-completion\",\"dependent_task_ids\":[1,2,3],\"status\":\"incomplete\",\"result\":null,\"result_summary\":null}}
    ]
    """)
  },
  {
    "objective": "Find me the top questions asked for Sales and Marketing on Quora today and draft impactful responses for each of those questions that you found.",
    "taskList": dedent("""
    [
    {{\"id\": 1,\"task\":\"List down the top questions found\",\"tool\":\"scraping\",\"dependent_task_ids\":[],\"status\":\"incomplete\", \"result\": null, \"result_summary\": null}},
    {{\"id\": 2,\"task\":\"Draft impactful responses for each question\",\"tool\":\"text-completion\",\"dependent_task_ids\":[1],\"status\":\"incomplete\", \"result\": null, \"result_summary\": null}},
    {{\"id\": 3,\"task\":\"Review and refine responses\",\"tool\":\"text-completion\",\"dependent_task_ids\":[2],\"status\":\"incomplete\", \"result\": null, \"result_summary\": null}},
    {{\"id\": 4,\"task\":\"Finalize responses\",\"tool\":\"text-completion\",\"dependent_task_ids\":[3],\"status\":\"incomplete\", \"result\": null, \"result_summary\": null}}
    ]
    """)
  },
  {
    "objective": "Find me the CRO's or VP of Sales Names and LinkedIn Profiles for people in the following companies : Salesforce Microsoft Intuit Veeva Systems Oracle Cvent Druva Box Google Workspace Zendesk",
    "taskList": dedent("""
    [
    {{\"id\": 1,\"task\":\"Salesforce CRO or VP of Sales\",\"tool\":\"web-search\",\"dependent_task_ids\":[],\"status\":\"incomplete\", \"result\": null, \"result_summary\": null}},
    {{\"id\": 2,\"task\":\"Microsoft CRO or VP of Sales\",\"tool\":\"web-search\",\"dependent_task_ids\":[],\"status\":\"incomplete\", \"result\": null, \"result_summary\": null}},
    {{\"id\": 3,\"task\":\"Intuit CRO or VP of Sales\",\"tool\":\"web-search\",\"dependent_task_ids\":[],\"status\":\"incomplete\", \"result\": null, \"result_summary\": null}},
    {{\"id\": 4,\"task\":\"Veeva Systems CRO or VP of Sales\",\"tool\":\"web-search\",\"dependent_task_ids\":[],\"status\":\"incomplete\", \"result\": null, \"result_summary\": null}},
    {{\"id\": 5,\"task\":\"Oracle CRO or VP of Sales\",\"tool\":\"web-search\",\"dependent_task_ids\":[],\"status\":\"incomplete\", \"result\": null, \"result_summary\": null}},
    {{\"id\": 6,\"task\":\"Cvent CRO or VP of Sales\",\"tool\":\"web-search\",\"dependent_task_ids\":[],\"status\":\"incomplete\", \"result\": null, \"result_summary\": null}}
    ]
    """)
  },
  {
    "objective": "What are the trending topics in Software as a Service on social media?",
    "taskList": dedent("""
    [
    {{\"id\": 1,\"task\":\"Search for 'trending topics in Software as a Service on social media'\",\"tool\":\"scraping\",\"dependent_task_ids\":[],\"status\":\"incomplete\", \"result\": null, \"result_summary\": null}},
    {{\"id\": 2,\"task\":\"Search for 'Software as a Service trending hashtags on Twitter'\",\"tool\":\"scraping\",\"dependent_task_ids\":[],\"status\":\"incomplete\", \"result\": null, \"result_summary\": null}},
    {{\"id\": 3,\"task\":\"Search for 'Software as a Service trending discussions on LinkedIn'\",\"tool\":\"scraping\",\"dependent_task_ids\":[],\"status\":\"incomplete\", \"result\": null, \"result_summary\": null}},
    {{\"id\": 4,\"task\":\"Summarize the top 5 trending topics found\",\"tool\":\"text-completion\",\"dependent_task_ids\":[1,2,3],\"status\":\"incomplete\", \"result\": null, \"result_summary\": null}},
    {{\"id\": 5,\"task\":\"Summarize the top 5 trending hashtags found\",\"tool\":\"text-completion\",\"dependent_task_ids\":[1,2,3],\"status\":\"incomplete\", \"result\": null, \"result_summary\": null}},
    {{\"id\": 6,\"task\":\"Summarize the top 5 trending discussions found\",\"tool\":\"text-completion\",\"dependent_task_ids\":[1,2,3],\"status\":\"incomplete\", \"result\": null, \"result_summary\": null}},
    {{\"id\": 7,\"task\":\"Combine all the summaries into a final report\",\"tool\":\"text-completion\",\"dependent_task_ids\":[4,5,6],\"status\":\"incomplete\", \"result\": null, \"result_summary\": null}}
    ]
    """)
  },
  {
    "objective": "What are the top pain points mentioned by sales Managers on social media?",
    "taskList": dedent("""
    [
    {{\"id\": 1,\"task\":\"Search for 'Sales Managers pain points' on social media\",\"tool\":\"web-search\",\"dependent_task_ids\":[],\"status\":\"incomplete\", \"result\": null, \"result_summary\": null}},
    {{\"id\": 2,\"task\":\"Search for 'Sales Managers challenges' on social media\",\"tool\":\"web-search\",\"dependent_task_ids\":[],\"status\":\"incomplete\", \"result\": null, \"result_summary\": null}},
    {{\"id\": 3,\"task\":\"Search for 'List the top 5 pain points mentioned by sales managers'\",\"tool\":\"text-completion\",\"dependent_task_ids\":[1,2],\"status\":\"incomplete\", \"result\": null, \"result_summary\": null}},
    {{\"id\": 4,\"task\":\"Final summary report\",\"tool\":\"text-completion\",\"dependent_task_ids\":[1,2,3],\"status\":\"incomplete\", \"result\": null, \"result_summary\": null}}
    ]
    """)
  },
  {
    "objective": "Find me the names top 50 companies in Software as a Service industry in companies with >500 employees in United States",
    "taskList": dedent("""
    [
    {{\"id\": 1,\"task\":\"Top 50 SaaS companies in the US\",\"tool\":\"web-search\",\"dependent_task_ids\":[],\"status\":\"incomplete\", \"result\": null, \"result_summary\": null}},
    {{\"id\": 2,\"task\":\"Filter companies with more than 500 employees\",\"tool\":\"scraping\",\"dependent_task_ids\":[1],\"status\":\"incomplete\", \"result\": null, \"result_summary\": null}},
    {{\"id\": 3,\"task\":\"Create a list of these companies\",\"tool\":\"text-completion\",\"dependent_task_ids\":[1,2],\"status\":\"incomplete\", \"result\": null, \"result_summary\": null}},
    {{\"id\": 4,\"task\":\"Final list of top 50 SaaS companies in the US with more than 500 employees\",\"tool\":\"text-completion\",\"dependent_task_ids\":[1,2,3],\"status\":\"incomplete\", \"result\": null, \"result_summary\": null}}
    ]
    """)
  },
  {
    "objective": "Find me a list of top 10 mining companies in : Mining, Oil & Gas, Logistics (Freight, Shipping, etc), Manufacturing",
    "taskList": dedent("""
    [
    {{\"id\": 1,\"task\":\"Top 10 mining companies\",\"tool\":\"scraping\",\"dependent_task_ids\":[],\"status\":\"incomplete\", \"result\": null, \"result_summary\": null}},
    {{\"id\": 2,\"task\":\"Top 10 oil & gas companies	\",\"tool\":\"scraping\",\"dependent_task_ids\":[1],\"status\":\"incomplete\", \"result\": null, \"result_summary\": null}},
    {{\"id\": 3,\"task\":\"Top 10 logistics companies\",\"tool\":\"scraping\",\"dependent_task_ids\":[1,2],\"status\":\"incomplete\", \"result\": null, \"result_summary\": null}},
    {{\"id\": 4,\"task\":\"Top 10 manufacturing companies\",\"tool\":\"scraping\",\"dependent_task_ids\":[1,2],\"status\":\"incomplete\", \"result\": null, \"result_summary\": null}},
    {{\"id\": 5,\"task\":\"Summarize the list of top 10 mining companies\",\"tool\":\"text-completion\",\"dependent_task_ids\":[1,2,3],\"status\":\"incomplete\", \"result\": null, \"result_summary\": null}},
    {{\"id\": 6,\"task\":\"Summarize the list of top 10 oil & gas companies\",\"tool\":\"text-completion\",\"dependent_task_ids\":[1,2,3],\"status\":\"incomplete\", \"result\": null, \"result_summary\": null}},
    {{\"id\": 7,\"task\":\"Summarize the list of top 10 logistics companies\",\"tool\":\"text-completion\",\"dependent_task_ids\":[1,2,3],\"status\":\"incomplete\", \"result\": null, \"result_summary\": null}},
    {{\"id\": 8,\"task\":\"Summarize the list of top 10 manufacturing companies\",\"tool\":\"text-completion\",\"dependent_task_ids\":[1,2,3],\"status\":\"incomplete\", \"result\": null, \"result_summary\": null}},
    {{\"id\": 9,\"task\":\"Combine all the summaries into a final report	\",\"tool\":\"text-completion\",\"dependent_task_ids\":[5,6,7,8],\"status\":\"incomplete\", \"result\": null, \"result_summary\": null}}
    ]
    """)
  },
  {
    "objective": "Give me all the details about Saumya Bhatnagar at involve.ai",
    "taskList": dedent("""
    [
    {{\"id\": 1,\"task\":\"Saumya Bhatnagar involve.ai	\",\"tool\":\"scraping\",\"dependent_task_ids\":[],\"status\":\"incomplete\", \"result\": null, \"result_summary\": null}},
    {{\"id\": 2,\"task\":\"Summarize the professional background of Saumya Bhatnagar	\",\"tool\":\"text-completion\",\"dependent_task_ids\":[1],\"status\":\"incomplete\", \"result\": null, \"result_summary\": null}},
    {{\"id\": 3,\"task\":\"List the roles and responsibilities of Saumya Bhatnagar at involve.ai	\",\"tool\":\"text-completion\",\"dependent_task_ids\":[1,2],\"status\":\"incomplete\", \"result\": null, \"result_summary\": null}},
    {{\"id\": 4,\"task\":\"Find any recent news or updates related to Saumya Bhatnagar at involve.ai\",\"tool\":\"web-search\",\"dependent_task_ids\":[1,2],\"status\":\"incomplete\", \"result\": null, \"result_summary\": null}},
    {{\"id\": 5,\"task\":\"Summarize the recent news or updates	\",\"tool\":\"text-completion\",\"dependent_task_ids\":[1,2,3],\"status\":\"incomplete\", \"result\": null, \"result_summary\": null}},
    {{\"id\": 6,\"task\":\"Final report on Saumya Bhatnagar at involve.ai	\",\"tool\":\"text-completion\",\"dependent_task_ids\":[1,2,3,4,5],\"status\":\"incomplete\", \"result\": null, \"result_summary\": null}}
    ]
    """)
  },
  {
    "objective": "Find me the names and details of 2 VP of Sales who work at companies that belong to the Software as a Service industry",
    "taskList": dedent("""
    [
    {{\"id\": 1,\"task\":\"Search for top Software as a Service companies\",\"tool\":\"scraping\",\"dependent_task_ids\":[],\"status\":\"incomplete\", \"result\": null, \"result_summary\": null}},
    {{\"id\": 2,\"task\":\"Extract the names of the top 10 companies\",\"tool\":\"text-completion\",\"dependent_task_ids\":[1],\"status\":\"incomplete\", \"result\": null, \"result_summary\": null}},
    {{\"id\": 3,\"task\":\"Search for the VP of Sales at the first company\",\"tool\":\"scraping\",\"dependent_task_ids\":[1,2],\"status\":\"incomplete\", \"result\": null, \"result_summary\": null}},
    {{\"id\": 4,\"task\":\"Search for the VP of Sales at the second company\",\"tool\":\"scraping\",\"dependent_task_ids\":[1,2],\"status\":\"incomplete\", \"result\": null, \"result_summary\": null}},
    {{\"id\": 5,\"task\":\"Extract the name and details of the VP of Sales at the second company	\",\"tool\":\"text-completion\",\"dependent_task_ids\":[1,2,3],\"status\":\"incomplete\", \"result\": null, \"result_summary\": null}},
    {{\"id\": 6,\"task\":\"Compile the names and details of all 2 VP of Sales	\",\"tool\":\"text-completion\",\"dependent_task_ids\":[1,2,3],\"status\":\"incomplete\", \"result\": null, \"result_summary\": null}}
    ]
    """)
  },
  {
    "objective": "I want to research https://www.linkedin.com/in/bhattacharyagaurav and get a summary of their entire profile, news etc",
    "taskList": dedent("""
    [
    {{\"id\": 1,\"task\":\"https://www.linkedin.com/in/bhattacharyagaurav\",\"tool\":\"linkedin\",\"dependent_task_ids\":[],\"status\":\"incomplete\", \"result\": null, \"result_summary\": null}},
    {{\"id\": 2,\"task\":\"Summarize Work history\",\"tool\":\"text-completion\",\"dependent_task_ids\":[1],\"status\":\"incomplete\", \"result\": null, \"result_summary\": null}},
    {{\"id\": 3,\"task\":\"Extract education details\",\"tool\":\"text-completion\",\"dependent_task_ids\":[1],\"status\":\"incomplete\", \"result\": null, \"result_summary\": null}},
    {{\"id\": 4,\"task\":\"Summarize recent posts\",\"tool\":\"text-completion\",\"dependent_task_ids\":[1],\"status\":\"incomplete\", \"result\": null, \"result_summary\": null}},
    {{\"id\": 5,\"task\":\"Infer job responsibilities\",\"tool\":\"text-completion\",\"dependent_task_ids\":[1],\"status\":\"incomplete\", \"result\": null, \"result_summary\": null}},
    {{\"id\": 6,\"task\":\"Extract technical skills\",\"tool\":\"text-completion\",\"dependent_task_ids\":[1],\"status\":\"incomplete\", \"result\": null, \"result_summary\": null}}
    ]
    """)
  }
]