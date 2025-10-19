```json
{
  "id": "786364fce1351438",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291571,
  "host_pid": "9e6742732c60:1",
  "hash": "9f947e7af8febf8e0246d903a9ffc67e4fa83b651026937ca64948e5cfb6fddd",
  "cid": "QmV19f947e7af8febf8e0246d903a9ffc67e4fa83b65",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291571,
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
      "evaluated_at": 1760291571
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
  "sig": "7629d15521e77c257d4e7fd3172683001fba10c381e6ce7d210602685a379b54"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469615703
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 178, 'threshold': 50, 'total_amount': 33910246, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 177, 'first_seen': 1760285763, 'matching_hash': '33adc30ff3203421'}}}