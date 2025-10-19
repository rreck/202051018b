```json
{
  "id": "6515b6a79ad6928a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290913,
  "host_pid": "9e6742732c60:1",
  "hash": "b8e3f52d0c45308505b917c688e6f63de5fbd1dd91996b95da09c0f0b7293f83",
  "cid": "QmV1b8e3f52d0c45308505b917c688e6f63de5fbd1dd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290913,
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
      "evaluated_at": 1760290913
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
  "sig": "8ede9ca4753a2e70d229d2800017001dad79f869580e93e0c4019724acc13627"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598542542
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 162, 'threshold': 50, 'total_amount': 54181062, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 161, 'first_seen': 1760285764, 'matching_hash': '3cc1c7bbce52acf6'}}}