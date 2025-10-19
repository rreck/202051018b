```json
{
  "id": "d293fa770d76a747",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294586,
  "host_pid": "9e6742732c60:1",
  "hash": "7f6a5a2a61bb3fbaf238dd7548e72515b12a426b4bc3fd4f5ad3989215466711",
  "cid": "QmV17f6a5a2a61bb3fbaf238dd7548e72515b12a426b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294586,
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
      "evaluated_at": 1760294586
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
  "sig": "e125e52cc3849194556f07714ef5920e29abfac4526db9f78fab8e15f700be96"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000026803563
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 241, 'threshold': 50, 'total_amount': 60457742, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 240, 'first_seen': 1760285763, 'matching_hash': 'cf30c88fa01e3081'}}}