```json
{
  "id": "b1ebdb4d84be2c6b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287137,
  "host_pid": "9e6742732c60:1",
  "hash": "55b2d1a0a9a0040d11bc6c46d382a1b9736e3e1f70219a089499aec8a52d1eef",
  "cid": "QmV155b2d1a0a9a0040d11bc6c46d382a1b9736e3e1f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287137,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760287137
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "round_amount_pattern",
    "risk_high"
  ],
  "sig": "ff8818937cbe6b850c85636887f457b2f1ff6a283b1795256db1c999108646cc"
}
```

Fraud detected: round_amount_pattern (score: 65)
Transaction: 111000026431469
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 49000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 48, 'first_seen': 1760285765, 'matching_hash': '51112ae34069fd52'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}