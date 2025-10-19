```json
{
  "id": "23b6080402e6e3b4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289855,
  "host_pid": "9e6742732c60:1",
  "hash": "28112987f7383067ae16e7122ac00fa6e6e25917485ad30537ca973790ef7e65",
  "cid": "QmV128112987f7383067ae16e7122ac00fa6e6e25917",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289855,
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
      "evaluated_at": 1760289855
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
  "sig": "0c9fe18f16af88caf3b750f6ed2fb1b673f067f6366c9eb5faf06dd25bb3061f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150128981
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 135, 'threshold': 50, 'total_amount': 25820100, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 134, 'first_seen': 1760285763, 'matching_hash': '59c56ba6c2207f9a'}}}