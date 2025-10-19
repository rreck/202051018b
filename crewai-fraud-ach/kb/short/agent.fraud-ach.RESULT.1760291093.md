```json
{
  "id": "86e82adbadefa878",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291093,
  "host_pid": "9e6742732c60:1",
  "hash": "3087aa7102f8f8e5a097c5df7bec0a75e27fe5aea6845ca08a151b5a74d37445",
  "cid": "QmV13087aa7102f8f8e5a097c5df7bec0a75e27fe5ae",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291093,
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
      "evaluated_at": 1760291093
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
  "sig": "83892f714fe8202ae513db22a8a03e0cb0e120086493268a85d113c4a6ecc15c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000030232602
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 167, 'threshold': 50, 'total_amount': 10075110, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 166, 'first_seen': 1760285763, 'matching_hash': '54bba9b5de699774'}}}