```json
{
  "id": "6f62c4c2ba6bcb78",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288410,
  "host_pid": "9e6742732c60:1",
  "hash": "6f72546da64c071dcd65ae789ff8c1bbfff3bfe54950d8f82499c83963956f34",
  "cid": "QmV16f72546da64c071dcd65ae789ff8c1bbfff3bfe5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288410,
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
      "evaluated_at": 1760288410
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
  "sig": "c89506f394e0db7252846e57a551d257fd683d60e7819a38fe230259fc8bdbd8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025198728
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 92, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 91, 'first_seen': 1760285765, 'matching_hash': 'ff4b51392b1a88ca'}}}