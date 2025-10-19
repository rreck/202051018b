```json
{
  "id": "a9be5c4096687d79",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294781,
  "host_pid": "9e6742732c60:1",
  "hash": "ac60cf6b6e6a11363eb4a41fef07371f1ff92789673f629fe184ebe3f05f21b6",
  "cid": "QmV1ac60cf6b6e6a11363eb4a41fef07371f1ff92789",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294781,
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
      "evaluated_at": 1760294781
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
  "sig": "836e40ecf169f59ac6daa573cc744cbf3f820516328110798aba7280c074061d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100278681806
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 244, 'threshold': 50, 'total_amount': 114748320, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 243, 'first_seen': 1760285765, 'matching_hash': '5ddc61c49d89e409'}}}