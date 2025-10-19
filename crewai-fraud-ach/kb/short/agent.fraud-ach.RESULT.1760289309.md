```json
{
  "id": "15e861f69b57c677",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289309,
  "host_pid": "9e6742732c60:1",
  "hash": "90e05c1861aa3c6eedcbefc594b005524d6f0c3aa5f38aaa5157d8013a649058",
  "cid": "QmV190e05c1861aa3c6eedcbefc594b005524d6f0c3a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289309,
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
      "evaluated_at": 1760289309
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
  "sig": "950569bb006b1253819dd03eb6d12609c74c0469d3ea08dfb8ae540ef0f60850"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 119, 'threshold': 50, 'total_amount': 37871512, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 118, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}