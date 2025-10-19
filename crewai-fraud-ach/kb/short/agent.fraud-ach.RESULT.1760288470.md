```json
{
  "id": "d30bbc11ce8fca54",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288470,
  "host_pid": "9e6742732c60:1",
  "hash": "b97c8485daae2299539e26a28366529ebb57ea2592037b2d372b99b599cdeb1f",
  "cid": "QmV1b97c8485daae2299539e26a28366529ebb57ea25",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288470,
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
      "evaluated_at": 1760288470
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
  "sig": "45e667fd2ae1863aa3296fe43c5c137405d9faae9bbcbc7ab9e8d63f26795e20"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201463787734
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 94, 'threshold': 50, 'total_amount': 30202670, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 93, 'first_seen': 1760285764, 'matching_hash': 'c4d507dbbdae18b2'}}}