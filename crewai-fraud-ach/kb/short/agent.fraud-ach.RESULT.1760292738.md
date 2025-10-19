```json
{
  "id": "047fde16b45f1138",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292738,
  "host_pid": "9e6742732c60:1",
  "hash": "9d9d41bae9755bd9ece93f3a716765efb262c347a68088640630542534314552",
  "cid": "QmV19d9d41bae9755bd9ece93f3a716765efb262c347",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292738,
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
      "evaluated_at": 1760292738
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
  "sig": "3cae2baf5381367f9ea2b84bf9cc2c00aca179b317650a1479971176763a851b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100276534342
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 204, 'threshold': 50, 'total_amount': 63680844, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 203, 'first_seen': 1760285763, 'matching_hash': '3bb091557ce86ea6'}}}