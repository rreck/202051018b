```json
{
  "id": "5e3aa0a0b7a4d3ed",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294722,
  "host_pid": "9e6742732c60:1",
  "hash": "e0be03802c761aeb88e3a0bc5983e5b8378784d49b2a251b842498cb55e81d17",
  "cid": "QmV1e0be03802c761aeb88e3a0bc5983e5b8378784d4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294722,
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
      "evaluated_at": 1760294722
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
  "sig": "15dbe0f76fe097c8fa85fb3a42415770c217e28c2ae58b3274157467221bcb6c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026451752
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 319, 'threshold': 50, 'total_amount': 78692196, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 318, 'first_seen': 1760284979, 'matching_hash': 'ed66d17e763eb837'}}}