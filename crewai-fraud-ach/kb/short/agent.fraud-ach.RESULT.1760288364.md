```json
{
  "id": "2064d235db90eec8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288364,
  "host_pid": "9e6742732c60:1",
  "hash": "f80251853cffb9597aea9314ef509c7dd5b2de3830243874cb240411b19bbfc5",
  "cid": "QmV1f80251853cffb9597aea9314ef509c7dd5b2de38",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288364,
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
      "evaluated_at": 1760288364
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
  "sig": "9be0b9759d8f9caff4f2c3de97811569064c7ea224d09e3cedbf13ac5e69a701"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000031287652
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 91, 'threshold': 50, 'total_amount': 25214007, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 90, 'first_seen': 1760285763, 'matching_hash': 'd2d8cdbc9df50106'}}}