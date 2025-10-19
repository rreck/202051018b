```json
{
  "id": "fc7917563ca487c2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288189,
  "host_pid": "9e6742732c60:1",
  "hash": "b48a50073251dd07ee19225b31662109fe9afeaa9eda9b521cd940e00d76e27e",
  "cid": "QmV1b48a50073251dd07ee19225b31662109fe9afeaa",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288189,
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
      "evaluated_at": 1760288189
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
  "sig": "98f25071d3f46c2a6b106cb34294bb9ed116994d18e97b5acd7552b7ef014bf0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274128098
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 85, 'threshold': 50, 'total_amount': 35259360, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 84, 'first_seen': 1760285765, 'matching_hash': 'e67ed82943972fb3'}}}