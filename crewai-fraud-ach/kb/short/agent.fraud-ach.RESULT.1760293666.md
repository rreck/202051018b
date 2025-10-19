```json
{
  "id": "4e554737d30c171d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293666,
  "host_pid": "9e6742732c60:1",
  "hash": "cc69e4d17c5e77dfceeea2c4d6243daa7965f41d3e2a7b4fe0e0a6489103e5e6",
  "cid": "QmV1cc69e4d17c5e77dfceeea2c4d6243daa7965f41d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293666,
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
      "evaluated_at": 1760293666
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
  "sig": "8380730ac6dacccc0192e84f0f073fbcff20051de9e7be70c058483489fe6aa8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248764263
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 223, 'threshold': 50, 'total_amount': 80993154, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 222, 'first_seen': 1760285763, 'matching_hash': '9f14c95be52dc67f'}}}