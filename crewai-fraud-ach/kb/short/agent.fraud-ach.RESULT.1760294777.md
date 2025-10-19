```json
{
  "id": "8966b4ea23937f67",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294777,
  "host_pid": "9e6742732c60:1",
  "hash": "b46fd640c4da3783b42a8b9b03995da5c2d7c405ca3fb11762112fc02e92c23b",
  "cid": "QmV1b46fd640c4da3783b42a8b9b03995da5c2d7c405",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294777,
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
      "evaluated_at": 1760294777
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
  "sig": "6ef982be4a7d6a2f3dab6d8bcd1a3c1f2753a968ccb84ac1546c72df80547dd9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000031032710
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 244, 'threshold': 50, 'total_amount': 57877044, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 243, 'first_seen': 1760285763, 'matching_hash': 'e5dc8a38744b9e1c'}}}