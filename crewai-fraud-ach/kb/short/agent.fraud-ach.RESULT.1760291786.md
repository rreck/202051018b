```json
{
  "id": "790e78504d35ec97",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291786,
  "host_pid": "9e6742732c60:1",
  "hash": "876ab44cb9a4e528378096fcfbe7c0cd0ecc0d49bd1faedbc76652dcba721449",
  "cid": "QmV1876ab44cb9a4e528378096fcfbe7c0cd0ecc0d49",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291786,
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
      "evaluated_at": 1760291786
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
  "sig": "7e64d5e1a9f2f340702bc4fd5fdb539444f0e3b16befb67929356b330faa3231"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464749166
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 183, 'threshold': 50, 'total_amount': 65259996, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 182, 'first_seen': 1760285764, 'matching_hash': '2c72b457e71ecad2'}}}