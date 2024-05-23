<template>
  <div class="chat-container">
    <div class="rounded mb-1 py-1" style="background-color: #ffbd2e;">
      <div class="mt-3" style=" color: black; font-weight: bold; font-size: 25px;">
        <p class="text-center">챗봇에게 영화를 추천 받아보세요!</p>        
      </div>
    </div>
    <div class="chat-log" id="chat-messages" ref="chatMessages">
      <div
        v-for="(message, index) in reversedMessages"
        :key="index"
        :class="{
          user: message.role === 'user',
          bot: message.role === 'assistant',
        }"
        class="message"
      >
        {{ message.content }}
      </div>
    </div>
    <div class="user-input">
      <input
        v-model="userInput"
        @keyup.enter="sendMessage"
        placeholder="챗봇에게 물어봐"
        id="user-input"
      />
      <button @click="sendMessage" id="send-button">전송</button>
    </div>
  </div>
</template>

<script setup>
import { ref, nextTick, computed } from "vue";

const messages = ref([]);
const userInput = ref("");
const chatMessages = ref(null);

const apiKey = import.meta.env.VITE_APP_OPENAI_API_KEY;
const apiEndpoint = "https://api.openai.com/v1/chat/completions";

const addMessage = (sender, message) => {
  messages.value.push({
    role: sender === "나" ? "user" : "assistant",
    content: message,
  });
  nextTick(() => {
    chatMessages.value.scrollTop = chatMessages.value.scrollHeight;
  });
};

const fetchAIResponse = async (prompt) => {
  const requestOptions = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${apiKey}`,
    },
    body: JSON.stringify({
      model: "gpt-3.5-turbo",
      messages: [
        {
          role: "user",
          content: prompt,
        },
      ],
      temperature: 0.8,
      max_tokens: 1024,
      top_p: 1,
      frequency_penalty: 0.5,
      presence_penalty: 0.5,
    }),
  };

  try {
    const response = await fetch(apiEndpoint, requestOptions);
    const data = await response.json();
    const aiResponse = data.choices[0].message.content;
    return aiResponse;
  } catch (error) {
    console.error("OpenAI API 호출 중 오류 발생:", error);
    return "OpenAI API 호출 중 오류 발생";
  }
};

const sendMessage = async () => {
  if (userInput.value.trim() === "") return;

  let message = userInput.value.trim();
  addMessage("나", message);
  userInput.value = "";
  
  // 
  message += '. 앞 대화 내용을 참고해서 영화를 추천 해주세요. 아니면 일상적으로 대화해주시면 됩니다. 앞 대화 내용을 참고해서 추천해주셨다는 말은 안하셔도 됩니다.'
  
  const aiResponse = await fetchAIResponse(message);
  addMessage("챗봇", aiResponse);
};

// Computed property to reverse the order of messages
const reversedMessages = computed(() => [...messages.value].reverse());
</script>

<style scoped>
body {
  margin: 0;
  font-family: Arial, sans-serif;
  background-color: #f5f5f5;
}

/* 대화형 컨테이너 스타일 */
.chat-container {
  max-width: calc(800px);
  margin: 20px auto;
  padding: 10px;  
  border-radius: 5px;
  background-color: #e0e0e0;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

/* 채팅 로그 스타일 */
.chat-log {
  height: 70vh; /* Set the height to 70% of the viewport height */
  margin-bottom: 10px;
  padding: 10px;
  border-radius: 5px;
  background-color:   #f0f0f0;
  overflow-y: scroll;
  display: flex;
  flex-direction: column-reverse; /* Stack messages from bottom 
    to top */
  display: flex;
  background-image: url("/filmatBackGround2.jpg"); /* Use your image URL here */
  background-size: cover;
  background-repeat: no-repeat;  
  opacity: 0.9;
}


/* 사용자 입력 폼 스타일 */
.user-input {
  display: flex;
  align-items: center;
  margin-top: 10px;
}

/* 사용자 입력 필드 스타일 */
#user-input {
  flex: 1;
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-right: 10px;
}

/* 전송 버튼 스타일 */
#send-button {
  padding: 8px 16px;
  font-weight: 800;
  background-color: #ffbd2e;
  color: #000000;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.2s;
}

#send-button:hover {
  background-color: #0056b3;
}

/* 로딩 표시 스타일 */
.loading-indicator {
  display: none;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

.spinner {
  border: 4px solid rgba(0, 0, 0, 0.1);
  border-top: 4px solid #007bff;
  border-radius: 50%;
  width: 24px;
  height: 24px;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

/* 채팅 메시지 스타일 */
.message {
  padding: 20px;
  border-radius: 20px;
  margin: 10px 0;
  color: black; /* 텍스트 색상을 검정색으로 설정 */
  font-size: 23px;
  font-weight: bold;
  background-color: rgba(
    255,
    255,
    255,
    0.9
  ); /* Make speech bubbles non-transparent */
}

/* 사용자 메시지 배경색 */
.user {
  background-color: #c2d2f3;
  color: black;
  align-self: flex-end; /* 사용자 메시지를 오른쪽에 정렬 */
  margin-left: auto; /* 오른쪽 정렬을 유지하기 위해 왼쪽 마진을 auto로 설정 */
}

/* 챗봇 메시지 배경색 */
.bot {
  background-color: #ecd3e3;
  align-self: flex-start; /* 챗봇 메시지를 왼쪽에 정렬 */
  margin-right: auto; /* 왼쪽 정렬을 유지하기 위해 오른쪽 마진을 auto로 설정 */
}
</style>
