```json
{
  "id": "8415964d3844f9ad",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289121,
  "host_pid": "9e6742732c60:1",
  "hash": "cdbe33e1455110f3610b55b1a8eae5ee8dc998bb3d1e3c3cbedc8e110f74575d",
  "cid": "QmV1cdbe33e1455110f3610b55b1a8eae5ee8dc998bb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289121,
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
      "evaluated_at": 1760289121
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
  "sig": "e9d7173fb834a101d4482d7397bdd35315792c89fb812496eb4ac4f837cb8595"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039514582
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 114, 'threshold': 50, 'total_amount': 36341034, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 113, 'first_seen': 1760285763, 'matching_hash': 'c5d30db04a2c4cc4'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}