package com.likelion.PBL.step2;

import com.likelion.PBL.dto.*;
import com.likelion.PBL.role.Lion;
import com.likelion.PBL.role.Role;
import com.likelion.PBL.role.Staff;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

/**
 * 멤버 관련 비즈니스 로직을 처리하는 역할 (서비스)
 *
 * [개선됨] 의존성 주입(DI) 적용
 * - Repository를 직접 생성하지 않고, 생성자를 통해 외부에서 주입받는다
 * - Repository 인터페이스에만 의존하므로 구현체가 바뀌어도 이 코드는 수정 불필요
 * - final 키워드로 불변성 보장
 */

@Service
@RequiredArgsConstructor
public class MemberService {
    private final MemberRepository repository;


    // Lion 생성
    public LionResponse createLion(LionCreateRequest request) {
        if (repository.existsByName(request.getName())) {
            return null;
        }
        Lion lion = new Lion(
                request.getName(),
                request.getMajor(),
                request.getGeneration(),
                request.getPart(),
                request.getStudentId()
        );
        repository.save(lion);
        return LionResponse.from(lion);
    }

    // Staff 생성
    public StaffResponse createStaff(StaffCreateRequest request) {
        if (repository.existsByName(request.getName())) {
            return null;
        }
        Staff staff = new Staff(
                request.getName(),
                request.getMajor(),
                request.getGeneration(),
                request.getPart(),
                request.getPosition()
        );
        repository.save(staff);
        return StaffResponse.from(staff);
    }

    // Lion 수정
    public LionResponse updateLion(String name, LionUpdateRequest request) {
        if (!repository.existsByName(name)) {
            return null;
        }
        Lion updated = new Lion(
                name, request.getMajor(),
                request.getGeneration(),
                request.getPart(),
                request.getStudentId()
        );
        repository.updateByName(name, updated);
        return LionResponse.from(updated);
    }

    // Staff 수정
    public StaffResponse updateStaff(String name, StaffUpdateRequest request) {
        if (!repository.existsByName(name)) {
            return null;
        }
        Staff updated = new Staff(
                name,
                request.getMajor(),
                request.getGeneration(),
                request.getPart(),
                request.getPosition()
        );
        repository.updateByName(name, updated);
        return StaffResponse.from(updated);
    }

    // 삭제
    public boolean deleteMember(String name) {
        return repository.deleteByName(name);
    }

    public Role findByName(String name) {
        return repository.findByName(name);
    }

}