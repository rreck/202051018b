```json
{
  "id": "1c2c9a9dda3de4d1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294273,
  "host_pid": "9e6742732c60:1",
  "hash": "13145262a657113dd3d67ef371a99f31d8b667e66c04c2711362806cebcb6eff",
  "cid": "QmV113145262a657113dd3d67ef371a99f31d8b667e6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294273,
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
      "evaluated_at": 1760294273
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
  "sig": "1849cbbc8fab864cb6f0145cd6f81c84e19a3b4cc9e870d7e04db5acb8a37a4a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022915367
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 235, 'threshold': 50, 'total_amount': 97704775, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 234, 'first_seen': 1760285763, 'matching_hash': '4fdfaefd2437a484'}}}