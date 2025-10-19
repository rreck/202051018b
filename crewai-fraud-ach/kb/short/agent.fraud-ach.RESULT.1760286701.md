```json
{
  "id": "b1f7da0126ff5ef1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286701,
  "host_pid": "9e6742732c60:1",
  "hash": "17dd04abd58346d752dbaba8726657e446787db56504c6dfb3038de18bc80a02",
  "cid": "QmV117dd04abd58346d752dbaba8726657e446787db5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286701,
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
      "evaluated_at": 1760286701
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
  "sig": "3b9db09741a40f713718295db2af0f55193567ab3183186b6464f4898edfdcc8"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000022841229
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 33, 'first_seen': 1760285763, 'matching_hash': '5d206cfe266207b6'}}}