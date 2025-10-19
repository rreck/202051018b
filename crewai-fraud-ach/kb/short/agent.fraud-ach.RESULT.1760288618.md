```json
{
  "id": "9bdab418213ca2bb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288618,
  "host_pid": "9e6742732c60:1",
  "hash": "aabc50ced7ca2e431eb3ced12d5a121e383876bb4e73b2eacd986671e906c5ea",
  "cid": "QmV1aabc50ced7ca2e431eb3ced12d5a121e383876bb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288618,
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
      "evaluated_at": 1760288618
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
  "sig": "c257091d97bb614a50457e10a67d927dc8b21031281c2366a4eed96823f8cd5e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467455813
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 99, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 98, 'first_seen': 1760285763, 'matching_hash': 'dd25b8ab6718ff18'}}}een': 1760285763, 'matching_hash': 'a33681b350a57503'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '701651308', 'validation_error': 'Invalid routing number checksum'}}}s': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 9655961}}}