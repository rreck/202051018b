```json
{
  "id": "48e3ac0e01e1778c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288749,
  "host_pid": "9e6742732c60:1",
  "hash": "c1230b584867037355b69abe95c3c7abde0759ec29201fb7ef78d1515075cc50",
  "cid": "QmV1c1230b584867037355b69abe95c3c7abde0759ec",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288749,
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
      "evaluated_at": 1760288749
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
  "sig": "849395f6a839c576cf97e1a3d6c2ca68c6909ebee9ccb332cf23e492fcc4552e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034128514
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 103, 'threshold': 50, 'total_amount': 20811459, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 102, 'first_seen': 1760285763, 'matching_hash': '342851cb36b9daae'}}}