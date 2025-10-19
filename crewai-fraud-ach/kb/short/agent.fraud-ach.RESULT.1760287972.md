```json
{
  "id": "e056f837843e3b84",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287972,
  "host_pid": "9e6742732c60:1",
  "hash": "075fc83e62a598a64bbf5f3228bccfcfe7c497f8a732f7ccd074c69f23ff00e8",
  "cid": "QmV1075fc83e62a598a64bbf5f3228bccfcfe7c497f8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287972,
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
      "evaluated_at": 1760287972
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
  "sig": "e356c49c56d553a2d5fe80177cf3302d7ce2cbee9a3d51eb850719c3c5324d35"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105152525323
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 78, 'threshold': 50, 'total_amount': 28707432, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 77, 'first_seen': 1760285765, 'matching_hash': '867ad08c0d495d7b'}}}