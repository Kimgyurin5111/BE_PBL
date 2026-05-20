package com.likelion.PBL.config;


import com.likelion.PBL.step2.MemberRepository;
import com.likelion.PBL.step2.MemberService;
import com.likelion.PBL.step2.MemoryMemberRepository;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class AppConfig {
    @Bean
    public MemberRepository memberRepository() {
        return new MemoryMemberRepository();
    }

    @Bean
    public MemberService memberService() {
        return new MemberService(memberRepository());
    }
}
