```json
{
  "id": "791306e035e317d0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288820,
  "host_pid": "9e6742732c60:1",
  "hash": "2dd71965d96f26509b68bb4ac7ffc477260f5a51644a8d4fe37fb02a3739845f",
  "cid": "QmV12dd71965d96f26509b68bb4ac7ffc477260f5a51",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288820,
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
      "evaluated_at": 1760288820
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
  "sig": "d5c81abcfdedc5a9b652fd487fcc845f067b4d4651556a97c2454678f48da60e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241012804
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 105, 'threshold': 50, 'total_amount': 28995750, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 104, 'first_seen': 1760285763, 'matching_hash': 'ba9ba43773b08e05'}}}