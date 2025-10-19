```json
{
  "id": "6501f6f172481908",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294341,
  "host_pid": "9e6742732c60:1",
  "hash": "a86990e9b6da8487c713393e00906f21dd147edacc8ad9091fd822049ba3a088",
  "cid": "QmV1a86990e9b6da8487c713393e00906f21dd147eda",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294341,
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
      "evaluated_at": 1760294341
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
  "sig": "7d43596e6a35c9b4971265b68d87fcb14be409a44b6f8947fd0d96f0e3559fd2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150096733
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 236, 'threshold': 50, 'total_amount': 31850560, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 235, 'first_seen': 1760285763, 'matching_hash': 'a29467afaa3320eb'}}}