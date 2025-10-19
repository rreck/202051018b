```json
{
  "id": "9e0b84aafe1d897d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290695,
  "host_pid": "9e6742732c60:1",
  "hash": "3c38f68cecfd572d77ad857d8a2143960fce0373c1edbd3ec648f44a9ef76b31",
  "cid": "QmV13c38f68cecfd572d77ad857d8a2143960fce0373",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290695,
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
      "evaluated_at": 1760290695
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
  "sig": "9466b9d54b0a469cd5f2a474456da750ce437a37ec91d6e71bd08f257b936d2c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100277276019
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 157, 'threshold': 50, 'total_amount': 59342703, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 156, 'first_seen': 1760285763, 'matching_hash': '90b38bd8812494f9'}}}