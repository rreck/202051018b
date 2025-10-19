```json
{
  "id": "204589b98ba1e5c3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285922,
  "host_pid": "9e6742732c60:1",
  "hash": "adb4c2e64a4df7efebfdd1909858e0a08192734271e68869e8da7d88d206f675",
  "cid": "QmV1adb4c2e64a4df7efebfdd1909858e0a081927342",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285922,
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
      "evaluated_at": 1760285922
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
  "sig": "67b141b134901d54d00b89863d8e89b9c855437fea3326b388db9ebbda48191d"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201460644681
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 7, 'first_seen': 1760285764, 'matching_hash': '02c671505c0a8698'}}}