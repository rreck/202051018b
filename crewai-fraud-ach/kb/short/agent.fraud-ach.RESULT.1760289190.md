```json
{
  "id": "f6b383bb6102eea4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289190,
  "host_pid": "9e6742732c60:1",
  "hash": "f699255a1b45d8a6672243c7b58280fad219db0183708fb1f1c8a08527d5a7a5",
  "cid": "QmV1f699255a1b45d8a6672243c7b58280fad219db01",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289190,
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
      "evaluated_at": 1760289190
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
  "sig": "aeda794be4b3402e1b5751279afb47b13884306c87524c40487be369376751b8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460939533
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 116, 'threshold': 50, 'total_amount': 38008328, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 115, 'first_seen': 1760285763, 'matching_hash': '9fc2d1aa6be5a150'}}}