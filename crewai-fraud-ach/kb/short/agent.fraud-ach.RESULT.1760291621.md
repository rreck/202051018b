```json
{
  "id": "913684ff8eeaccbd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291621,
  "host_pid": "9e6742732c60:1",
  "hash": "df9d901d0057970e36fe2864ee657789b979b0239f4a0539ff5f75bd9fe2b507",
  "cid": "QmV1df9d901d0057970e36fe2864ee657789b979b023",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291621,
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
      "evaluated_at": 1760291621
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
  "sig": "0e05a0bc4940b71c7a34d0be685fef9c623a1d46730d2050af5fb5f3e2b337cf"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032692891
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 255, 'threshold': 50, 'total_amount': 115916880, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 254, 'first_seen': 1760284979, 'matching_hash': '069830b10839223a'}}}