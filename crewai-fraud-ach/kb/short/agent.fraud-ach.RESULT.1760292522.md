```json
{
  "id": "dc3ec1032b30a92f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292522,
  "host_pid": "9e6742732c60:1",
  "hash": "635befc8e4d197d8e61868f571b97bac0d0760a83d741abe1a006533843b27ba",
  "cid": "QmV1635befc8e4d197d8e61868f571b97bac0d0760a8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292522,
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
      "evaluated_at": 1760292522
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
  "sig": "6b5b7286f345a1edda1e87a917d8f86524f97e596264231ab298a5dd9f505f76"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469103825
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 199, 'threshold': 50, 'total_amount': 71996011, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 198, 'first_seen': 1760285764, 'matching_hash': 'e83bf56ea8077a45'}}}