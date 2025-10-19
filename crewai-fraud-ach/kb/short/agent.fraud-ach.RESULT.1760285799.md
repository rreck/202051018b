```json
{
  "id": "cc02800c1104a20f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285799,
  "host_pid": "9e6742732c60:1",
  "hash": "c77bd1856e79b6cf3a67009561607e8924f55b08153b88ca1c3d7e35e95f3ec8",
  "cid": "QmV1c77bd1856e79b6cf3a67009561607e8924f55b08",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285799,
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
      "evaluated_at": 1760285799
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "51fa8c979783add640ec78c7bc279ba446cddc251775c3aaaf1ce4a66daccc64"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000241906665
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 2, 'first_seen': 1760285764, 'matching_hash': '6ca698820fae5f27'}}}