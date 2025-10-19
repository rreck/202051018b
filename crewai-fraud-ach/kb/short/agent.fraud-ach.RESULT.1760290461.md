```json
{
  "id": "9a334799503bd7ca",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290461,
  "host_pid": "9e6742732c60:1",
  "hash": "61e4b521043ccc1a2a9917eb233bd5b9f33b64721471802946c5b36309061f5f",
  "cid": "QmV161e4b521043ccc1a2a9917eb233bd5b9f33b6472",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290461,
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
      "evaluated_at": 1760290461
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
  "sig": "dbdccc4bd6fbbcf6220d5087ca512aac5eaf7e5c3104bf784ef2a4d2b986dec8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026691588
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 151, 'threshold': 50, 'total_amount': 61104717, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 150, 'first_seen': 1760285763, 'matching_hash': '1da0382cf03ec7d2'}}}