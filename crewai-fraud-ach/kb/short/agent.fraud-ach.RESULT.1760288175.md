```json
{
  "id": "6ebb72c3be6b80df",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288175,
  "host_pid": "9e6742732c60:1",
  "hash": "4fc077c18efc3dbf8af6dad6cc1ff22ac26fad9c468ab74e649ef1539c0dac99",
  "cid": "QmV14fc077c18efc3dbf8af6dad6cc1ff22ac26fad9c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288175,
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
      "evaluated_at": 1760288175
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
  "sig": "e0f20bc68e9c892dde520471594e9ba434680c1c7c0397e2ca71531812e398e1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467383207
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 85, 'threshold': 50, 'total_amount': 21596205, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 84, 'first_seen': 1760285763, 'matching_hash': 'cf3979d2ed99750b'}}}