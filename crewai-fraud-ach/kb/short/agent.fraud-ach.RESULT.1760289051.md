```json
{
  "id": "7e9d295306407023",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289051,
  "host_pid": "9e6742732c60:1",
  "hash": "cb1ff167ce7e37b1a03c8abb54c7986075ecdf37a348b5f20964cc5d90aa5e13",
  "cid": "QmV1cb1ff167ce7e37b1a03c8abb54c7986075ecdf37",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289051,
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
      "evaluated_at": 1760289051
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
  "sig": "af9054fb7795f5cf61ec6cc95d231c3a4f4b66e0b278d1f3060dede7fa547133"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000028116675
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 112, 'threshold': 50, 'total_amount': 38124240, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 111, 'first_seen': 1760285763, 'matching_hash': '276303153292771e'}}}