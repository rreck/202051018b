```json
{
  "id": "a61ccbebfd99ed24",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288271,
  "host_pid": "9e6742732c60:1",
  "hash": "2eebfbc16b9d4764b8f666bd1b4b01ac1429634870d7d9cc23a7b15ac163f609",
  "cid": "QmV12eebfbc16b9d4764b8f666bd1b4b01ac14296348",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288271,
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
      "evaluated_at": 1760288271
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
  "sig": "35e753e987b624c4d32e3b519a6d3dbf647c2ad70ba8fb6f8880f3175dc9b7e7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274458495
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 88, 'threshold': 50, 'total_amount': 40146392, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 87, 'first_seen': 1760285764, 'matching_hash': '191d9163e8e6657e'}}}