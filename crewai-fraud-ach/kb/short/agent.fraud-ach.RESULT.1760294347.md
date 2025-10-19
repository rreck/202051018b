```json
{
  "id": "5abad78cd35e12be",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294347,
  "host_pid": "9e6742732c60:1",
  "hash": "3648a8f135a1cf250d38fdd6c1e4e826ddc4afced1c83cf8170dbccb651f1c6d",
  "cid": "QmV13648a8f135a1cf250d38fdd6c1e4e826ddc4afce",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294347,
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
      "evaluated_at": 1760294347
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
  "sig": "95b6ac588e18b8c2219e870897ef1b9c6626511f09b979af2c8f57c6d9af8d63"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000031291734
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 236, 'threshold': 50, 'total_amount': 80375464, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 235, 'first_seen': 1760285763, 'matching_hash': 'b88361d419e7152d'}}}