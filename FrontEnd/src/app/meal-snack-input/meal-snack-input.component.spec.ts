import { ComponentFixture, TestBed } from '@angular/core/testing';
import { MealSnackInputComponent } from './meal-snack-input.component';

describe('MealSnackInputComponent', () => {
  let component: MealSnackInputComponent;
  let fixture: ComponentFixture<MealSnackInputComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ MealSnackInputComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MealSnackInputComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
