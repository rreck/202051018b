```json
{
  "id": "e9af7ad05765de0d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293903,
  "host_pid": "9e6742732c60:1",
  "hash": "ebb8d7560033272c0ee457cbf11cf17a379ac2d6e540a6df3c794f5d4724e2a3",
  "cid": "QmV1ebb8d7560033272c0ee457cbf11cf17a379ac2d6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293903,
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
      "evaluated_at": 1760293903
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
  "sig": "a639d5dad24302ad5553d4517550208aecee62833faa85038f8ec13100cba49c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009595927429
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 228, 'threshold': 50, 'total_amount': 32967204, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 227, 'first_seen': 1760285763, 'matching_hash': 'ad7b7e4988d8fb8c'}}}