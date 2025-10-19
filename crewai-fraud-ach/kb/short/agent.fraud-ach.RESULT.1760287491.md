```json
{
  "id": "155ca6f7e6dfb8b4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287491,
  "host_pid": "9e6742732c60:1",
  "hash": "8ce969991f1cacea4ac0f9cbf260e8a3c2b03cd0b2f620c54023d35eae63bab0",
  "cid": "QmV18ce969991f1cacea4ac0f9cbf260e8a3c2b03cd0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287491,
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
      "evaluated_at": 1760287491
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
  "sig": "eebd51b4c0aadd66c3cf8c514fbc8d58c42b915a4c60327017ded19095f53c03"
}
```

Fraud detected: duplicate_transaction (score: 79)
Transaction: 021000027727543
Details: {'velocity': {'fraud_detected': True, 'risk_score': 74, 'details': {'transaction_count': 62, 'threshold': 50, 'total_amount': 21106846, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 61, 'first_seen': 1760285763, 'matching_hash': '30f273873102b27a'}}}