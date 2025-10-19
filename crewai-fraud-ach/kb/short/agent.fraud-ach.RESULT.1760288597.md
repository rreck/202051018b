```json
{
  "id": "327e56010feae29e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288597,
  "host_pid": "9e6742732c60:1",
  "hash": "6786bb509a89654577606916d4327a3fad00fe5d4d1d21d8ba501c27d45f12ba",
  "cid": "QmV16786bb509a89654577606916d4327a3fad00fe5d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288597,
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
      "evaluated_at": 1760288597
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
  "sig": "60db6f5e84bd42f80ba88535fda09659599f536539a5187604c0a3dc58f6df75"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105158912506
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 98, 'threshold': 50, 'total_amount': 15078378, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 97, 'first_seen': 1760285765, 'matching_hash': 'bcd6f6796bd6b696'}}}