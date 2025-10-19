```json
{
  "id": "0465518def464044",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289471,
  "host_pid": "9e6742732c60:1",
  "hash": "ff50effdd7318a933784305cafd257456f9971e61d2d27e1a1d89192826f6b09",
  "cid": "QmV1ff50effdd7318a933784305cafd257456f9971e6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289471,
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
      "evaluated_at": 1760289471
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
  "sig": "a006205f98557c2c6201c67c4c66740d821971295a09e6f314e69d02b42e2c75"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100278037585
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 124, 'threshold': 50, 'total_amount': 13170784, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 123, 'first_seen': 1760285763, 'matching_hash': '27cb7a10328c75d5'}}}