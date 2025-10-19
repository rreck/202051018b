```json
{
  "id": "a7b84baa824e8c22",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289764,
  "host_pid": "9e6742732c60:1",
  "hash": "779a590ab96db016d7f575177a112df383a7b2a8b37ae44158dfb0a99a070f24",
  "cid": "QmV1779a590ab96db016d7f575177a112df383a7b2a8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289764,
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
      "evaluated_at": 1760289764
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
  "sig": "2e4fc5f39b17ad5ea305314d9fee6e493964e7ac4d5556a0e67e2e97aa5bc0ee"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271527804
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 132, 'threshold': 50, 'total_amount': 64909680, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 131, 'first_seen': 1760285764, 'matching_hash': '5c006846cf6d606a'}}}