```json
{
  "id": "5ecd112c43503e76",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292834,
  "host_pid": "9e6742732c60:1",
  "hash": "d165ef23a71cbf67059451f3b76eddbc317c1c70dcf7f193417c77b91d123ee7",
  "cid": "QmV1d165ef23a71cbf67059451f3b76eddbc317c1c70",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292834,
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
      "evaluated_at": 1760292834
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
  "sig": "c2b7e900c154021bea43429970609bc82e44f1c6cdf4d1513a9320480e3c4334"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244875332
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 206, 'threshold': 50, 'total_amount': 67600342, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 205, 'first_seen': 1760285763, 'matching_hash': '627c737035c8c8c8'}}}