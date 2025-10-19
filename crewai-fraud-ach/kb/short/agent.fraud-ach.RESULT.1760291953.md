```json
{
  "id": "5fd544ad1bef1de2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291953,
  "host_pid": "9e6742732c60:1",
  "hash": "8de2c97a16987670afb5ed4950ef8a3c57df7a881eb6b322c0105de48fddba69",
  "cid": "QmV18de2c97a16987670afb5ed4950ef8a3c57df7a88",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291953,
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
      "evaluated_at": 1760291953
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
  "sig": "bb98626243752049a197079c520e0002d88865b397c7498851d3bc8a8153b88b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201463831807
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 187, 'threshold': 50, 'total_amount': 33711425, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 186, 'first_seen': 1760285763, 'matching_hash': 'ac2384e4a351cc1b'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '398958456', 'validation_error': 'Invalid routing number checksum'}}}