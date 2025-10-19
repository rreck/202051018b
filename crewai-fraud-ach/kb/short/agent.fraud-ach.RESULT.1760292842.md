```json
{
  "id": "a919c01ba26bc20c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292842,
  "host_pid": "9e6742732c60:1",
  "hash": "8e84073619d34283d54d8e08bf5b051eec508c61dbeb33b101c11e496acf360b",
  "cid": "QmV18e84073619d34283d54d8e08bf5b051eec508c61",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292842,
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
      "evaluated_at": 1760292842
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
  "sig": "fca1d00c18f18a2c6e83a0df47a720495ad807dbddf338ff9306e5a1ea7361aa"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243890645
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 206, 'threshold': 50, 'total_amount': 37511570, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 205, 'first_seen': 1760285764, 'matching_hash': '25ed426365fec5d8'}}}