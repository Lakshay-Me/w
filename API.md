API



**Open AI PY**



from openai import OpenAI



client = OpenAI(

&nbsp; base\_url="https://openrouter.ai/api/v1",

&nbsp; api\_key="<OPENROUTER\_API\_KEY>",

)



completion = client.chat.completions.create(

&nbsp; extra\_headers={

&nbsp;   "HTTP-Referer": "<YOUR\_SITE\_URL>", # Optional. Site URL for rankings on openrouter.ai.

&nbsp;   "X-Title": "<YOUR\_SITE\_NAME>", # Optional. Site title for rankings on openrouter.ai.

&nbsp; },

&nbsp; extra\_body={},

&nbsp; model="deepseek/deepseek-chat-v3-0324:free",

&nbsp; messages=\[

&nbsp;   {

&nbsp;     "role": "user",

&nbsp;     "content": "What is the meaning of life?"

&nbsp;   }

&nbsp; ]

)

print(completion.choices\[0].message.content)





**PY**



import requests

import json



response = requests.post(

&nbsp; url="https://openrouter.ai/api/v1/chat/completions",

&nbsp; headers={

&nbsp;   "Authorization": "Bearer <OPENROUTER\_API\_KEY>",

&nbsp;   "Content-Type": "application/json",

&nbsp;   "HTTP-Referer": "<YOUR\_SITE\_URL>", # Optional. Site URL for rankings on openrouter.ai.

&nbsp;   "X-Title": "<YOUR\_SITE\_NAME>", # Optional. Site title for rankings on openrouter.ai.

&nbsp; },

&nbsp; data=json.dumps({

&nbsp;   "model": "deepseek/deepseek-chat-v3-0324:free",

&nbsp;   "messages": \[

&nbsp;     {

&nbsp;       "role": "user",

&nbsp;       "content": "What is the meaning of life?"

&nbsp;     }

&nbsp;   ],

&nbsp;   

&nbsp; })

)









**TPSC**



fetch("https://openrouter.ai/api/v1/chat/completions", {

&nbsp; method: "POST",

&nbsp; headers: {

&nbsp;   "Authorization": "Bearer <OPENROUTER\_API\_KEY>",

&nbsp;   "HTTP-Referer": "<YOUR\_SITE\_URL>", // Optional. Site URL for rankings on openrouter.ai.

&nbsp;   "X-Title": "<YOUR\_SITE\_NAME>", // Optional. Site title for rankings on openrouter.ai.

&nbsp;   "Content-Type": "application/json"

&nbsp; },

&nbsp; body: JSON.stringify({

&nbsp;   "model": "deepseek/deepseek-chat-v3-0324:free",

&nbsp;   "messages": \[

&nbsp;     {

&nbsp;       "role": "user",

&nbsp;       "content": "What is the meaning of life?"

&nbsp;     }

&nbsp;   ]

&nbsp; })

});









**Open AI TPSC**



import OpenAI from 'openai';

const openai = new OpenAI({

&nbsp; baseURL: "https://openrouter.ai/api/v1",

&nbsp; apiKey: "<OPENROUTER\_API\_KEY>",

&nbsp; defaultHeaders: {

&nbsp;   "HTTP-Referer": "<YOUR\_SITE\_URL>", // Optional. Site URL for rankings on openrouter.ai.

&nbsp;   "X-Title": "<YOUR\_SITE\_NAME>", // Optional. Site title for rankings on openrouter.ai.

&nbsp; },

});

async function main() {

&nbsp; const completion = await openai.chat.completions.create({

&nbsp;   model: "deepseek/deepseek-chat-v3-0324:free",

&nbsp;   messages: \[

&nbsp;     {

&nbsp;       "role": "user",

&nbsp;       "content": "What is the meaning of life?"

&nbsp;     }

&nbsp;   ],

&nbsp;   

&nbsp; });



&nbsp; console.log(completion.choices\[0].message);

}



main();





**Curl**







curl https://openrouter.ai/api/v1/chat/completions \\

&nbsp; -H "Content-Type: application/json" \\

&nbsp; -H "Authorization: Bearer $OPENROUTER\_API\_KEY" \\

&nbsp; -d '{

&nbsp; "model": "deepseek/deepseek-chat-v3-0324:free",

&nbsp; "messages": \[

&nbsp;   {

&nbsp;     "role": "user",

&nbsp;     "content": "What is the meaning of life?"

&nbsp;   }

&nbsp; ]

&nbsp; 

}'



