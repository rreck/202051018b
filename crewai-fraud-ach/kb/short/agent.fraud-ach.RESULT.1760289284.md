```json
{
  "id": "fe22ae81c9360a3e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289284,
  "host_pid": "9e6742732c60:1",
  "hash": "f371b4ef0f17c4a66c0b19f1e3e8d58878b7ea3dd71f22c090c50f01a0035d86",
  "cid": "QmV1f371b4ef0f17c4a66c0b19f1e3e8d58878b7ea3d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289284,
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
      "evaluated_at": 1760289284
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
  "sig": "812de39e188806c79e3e3768cc0d9c5c8b7663fb89f662b630ccd5b52e52421a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009595927429
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 119, 'threshold': 50, 'total_amount': 17206567, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 118, 'first_seen': 1760285763, 'matching_hash': 'ad7b7e4988d8fb8c'}}}