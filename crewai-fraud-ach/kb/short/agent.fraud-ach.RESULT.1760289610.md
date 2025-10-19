```json
{
  "id": "3497fb0d2935b4e0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289610,
  "host_pid": "9e6742732c60:1",
  "hash": "e168e8b169f482e66cc5964b4b1fb480c013a3ce094b409b533956aa481ed99f",
  "cid": "QmV1e168e8b169f482e66cc5964b4b1fb480c013a3ce",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289610,
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
      "evaluated_at": 1760289610
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
  "sig": "87ef87f1835f4fec036a0ebe8249c077ff0d9c9d3af1d658a7f5e390d130d220"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279947961
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 128, 'threshold': 50, 'total_amount': 11029376, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 127, 'first_seen': 1760285763, 'matching_hash': '22db2c62b181c93f'}}}