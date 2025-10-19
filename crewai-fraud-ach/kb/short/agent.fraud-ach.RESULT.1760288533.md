```json
{
  "id": "35fb79eb6c8bcd31",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288533,
  "host_pid": "9e6742732c60:1",
  "hash": "da678fb0f02d2069b8bf6be5912c3a3cc3ada4ad62faf95bd09b0739f5e1c0df",
  "cid": "QmV1da678fb0f02d2069b8bf6be5912c3a3cc3ada4ad",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288533,
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
      "evaluated_at": 1760288533
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
  "sig": "99eeb82ceb470671dc94432df517c137cfc03cda917a32f1eed6c3d1bdd1631e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241271300
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 96, 'threshold': 50, 'total_amount': 21958464, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 95, 'first_seen': 1760285763, 'matching_hash': 'c5ade7cea17f41fa'}}}