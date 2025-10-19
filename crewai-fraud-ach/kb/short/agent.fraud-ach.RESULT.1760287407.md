```json
{
  "id": "dc2f55a3edc88fc9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287407,
  "host_pid": "9e6742732c60:1",
  "hash": "7283ca7788bcc19f42164994cbbe22b67cd209f8268b7507dfd8a812fb3388cd",
  "cid": "QmV17283ca7788bcc19f42164994cbbe22b67cd209f8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287407,
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
      "evaluated_at": 1760287407
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "364dab3900f88d7d2e3d84acbd3d5ba3996c92fa14ab9f1f4f5cc3cf55703f03"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000026876887
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 59, 'threshold': 50, 'total_amount': 15744268, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 58, 'first_seen': 1760285763, 'matching_hash': 'ac27634a0ee0b6ee'}}}