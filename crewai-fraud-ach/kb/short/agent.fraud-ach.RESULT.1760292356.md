```json
{
  "id": "f6ba9c81c13f2958",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292356,
  "host_pid": "9e6742732c60:1",
  "hash": "ea58df035263b8852b1870a109d54e98cb6409aec9e710c49a7777f7101105d8",
  "cid": "QmV1ea58df035263b8852b1870a109d54e98cb6409ae",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292356,
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
      "evaluated_at": 1760292356
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
  "sig": "475d287895443ef4c9599f46e553483c7c2ad20918c062ae2566f78e3e79100d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000031517905
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 196, 'threshold': 50, 'total_amount': 87327996, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 195, 'first_seen': 1760285763, 'matching_hash': 'e8f76fb2eb784ea5'}}}