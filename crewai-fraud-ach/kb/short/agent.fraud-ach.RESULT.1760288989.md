```json
{
  "id": "d11ed35a9a8b1b81",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288989,
  "host_pid": "9e6742732c60:1",
  "hash": "1c4387efb9afe342657908c6d427223f4a132e4c118763c34b802851c71cb27f",
  "cid": "QmV11c4387efb9afe342657908c6d427223f4a132e4c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288989,
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
      "evaluated_at": 1760288989
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
  "sig": "234f278c0972c2c1af2bd886549c04b2bcd8f125bf755ee22fb96d6c54962b4a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039436848
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 110, 'threshold': 50, 'total_amount': 49613190, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 109, 'first_seen': 1760285763, 'matching_hash': '703cb1be49d2cf8f'}}}