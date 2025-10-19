```json
{
  "id": "0dc1aa762736ab67",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290423,
  "host_pid": "9e6742732c60:1",
  "hash": "69c08a755061d0d89540697d62bfa86208d5d54a19fc5b39a4fb990793570fd9",
  "cid": "QmV169c08a755061d0d89540697d62bfa86208d5d54a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290423,
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
      "evaluated_at": 1760290423
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
  "sig": "a728c764da6b7bbf4e3d0c1fde6590441c7de00c075f250c1af7a025f1716174"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034782199
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 150, 'threshold': 50, 'total_amount': 16312950, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 149, 'first_seen': 1760285763, 'matching_hash': '89ad1f50f76a063c'}}}