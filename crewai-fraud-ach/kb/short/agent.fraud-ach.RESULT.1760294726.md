```json
{
  "id": "34994b37f8681fc5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294726,
  "host_pid": "9e6742732c60:1",
  "hash": "ca9ad60be0acac47c001633fe8fb22e91903b019d2932729b839c91762469a9a",
  "cid": "QmV1ca9ad60be0acac47c001633fe8fb22e91903b019",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294726,
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
      "evaluated_at": 1760294726
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
  "sig": "d178bad48ff1801e4e39665f15d5165783e3bff322fae0895954859dd1e75a3b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000029285635
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 243, 'threshold': 50, 'total_amount': 84619647, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 242, 'first_seen': 1760285763, 'matching_hash': '952b5fd24342145c'}}}