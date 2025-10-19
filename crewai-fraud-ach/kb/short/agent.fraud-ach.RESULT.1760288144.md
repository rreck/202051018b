```json
{
  "id": "3d0aaad2665f0603",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288144,
  "host_pid": "9e6742732c60:1",
  "hash": "ef834b94c13a36f725b0e6ea6a6d1270c13d330c5fae2b5fef318fc944aec141",
  "cid": "QmV1ef834b94c13a36f725b0e6ea6a6d1270c13d330c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288144,
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
      "evaluated_at": 1760288144
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
  "sig": "5c4e5bc50f371920734fb5e365cc2f89815791d408af55241c8ddfa97e8dd5a0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000024392225
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 84, 'threshold': 50, 'total_amount': 37160088, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 83, 'first_seen': 1760285765, 'matching_hash': 'c2833deea8e214b7'}}}