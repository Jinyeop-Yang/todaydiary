<template>
	<div class="main-wrap">
		<div class="main-image">
			<img
				class="main-logo"
				src="@/assets/images/로고1.png"
				alt="오늘하루의 로고"
			/>
		</div>
		<div class="main-content">
			<p class="main-title">당신의 오늘 하루는 어떠셨나요?</p>
			<div class="accout">
				<P class="main-test" @click="onTestAccount">테스트 계정으로 로그인</P>
				<KakaoLogin
					:api-key="kakaoAPI"
					image="kakao_account_login_btn_medium_wide"
					:on-success="onSuccess"
					:on-failure="onFailure"
					style="cursor:pointer;"
				/>
			</div>
		</div>
	</div>
</template>

<script>
import KakaoLogin from 'vue-kakao-login';
import { onSuccess, onFailure } from '@/utils/kakao';
export default {
	components: {
		KakaoLogin,
	},
	methods: {
		onSuccess,
		onFailure,
		onTestAccount() {
			this.$router.push('/login');
		},
	},
	computed: {
		kakaoAPI() {
			return process.env.VUE_APP_KAKAO_API;
		},
	},
	mounted() {
		window.scrollTo(0, 0);
	},
};
</script>

<style lang="scss">
.main-wrap {
	width: 100%;
	height: 100vh;
	box-sizing: border-box;
	display: flex;
	flex-direction: column;
	align-items: center;
	.main-image {
		width: 100%;
		height: 60vh;
		display: flex;
		justify-content: center;
		align-items: center;
		.main-logo {
			margin-top: 2rem;
			width: 180px;
			height: 180px;
			border: 12px double rgba(202, 174, 137, 0.2);
			border-radius: 4px;
			@media (max-width: 300px) {
				width: 250px;
				height: 250px;
			}
		}
	}
}
.main-content {
	height: 40vh;
	width: 100%;
	display: flex;
	flex-direction: column;
	align-items: center;
	justify-content: space-around;
	.main-title {
		margin-top: -5.5rem;
		font-size: 1.1rem;
		@media (max-width: 300px) {
			margin-top: -5rem;
			font-size: 1rem;
		}
	}
	.main-test {
		margin-bottom: 20px;
		text-align: center;
		cursor: pointer;
	}
}
</style>
