import few_shot
from llm_helper import llm
from few_shot import FewShotPosts

few_shot = FewShotPosts()

def get_length_str(length):
    if length == "Short":
        return "1 to 5 lines"
    if length == "Medium":
        return "6 to 10 lines"
    if length == "Long":
        return "11 to 15 lines"



def generate_post(tag, length):
    length_str = get_length_str(length)
    prompt = f'''
        Generate a LinkedIn post using the below information. No preamble.

        1) Topic: {tag}
        2) Length: {length_str}
        '''
    examples = few_shot.get_filtered_posts(length, tag)

    if(len(examples) > 0):
        prompt += "3) Use the writing style as per the following examples."

        for i, post in enumerate(examples):
            post_text = post['text']
            prompt += f"\n\n Example{i} \n\n {post_text}"
            if i == 2:
                break


    response = llm.invoke(prompt)
    return response.content


if __name__ == "__main__":
    post = generate_post("Google", "Short")
    print(post)