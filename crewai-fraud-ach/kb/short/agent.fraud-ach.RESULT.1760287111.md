```json
{
  "id": "6653fc3fa82c0ff6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287111,
  "host_pid": "9e6742732c60:1",
  "hash": "47f9d7ee5e389229cb875d304e438e1774ee29942f7d1e586291876704057446",
  "cid": "QmV147f9d7ee5e389229cb875d304e438e1774ee2994",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287111,
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
      "evaluated_at": 1760287111
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "8c4686bc436147e7449f363e86b8e622acc7fdcf80c7b686952e2c207183a2be"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 15275904, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 47, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}