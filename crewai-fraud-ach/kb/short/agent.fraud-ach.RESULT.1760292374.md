```json
{
  "id": "bac66ebd597ee6cc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292374,
  "host_pid": "9e6742732c60:1",
  "hash": "47e89a75c44206c234ed88eb69dcfcd235b516035ca5be3b0cccf7d3326e9889",
  "cid": "QmV147e89a75c44206c234ed88eb69dcfcd235b51603",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292374,
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
      "evaluated_at": 1760292374
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
  "sig": "8b10afd1c090dc9e6f2c64c428747f26c522ab0130e0ae63d94f1e4116e58f8c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009592568865
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 196, 'threshold': 50, 'total_amount': 47428472, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 195, 'first_seen': 1760285763, 'matching_hash': 'ecded74c6845c7bc'}}}