```json
{
  "id": "7360dc67c7ffa52e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288077,
  "host_pid": "9e6742732c60:1",
  "hash": "a8b5b6ad16ed804a113ac8b526866433fd81097257d978f1c2eafb7e5d631e54",
  "cid": "QmV1a8b5b6ad16ed804a113ac8b526866433fd810972",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288077,
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
      "evaluated_at": 1760288077
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
  "sig": "01ac77103fdb66b8a6d3f0d98d576f0ec4e710d536d87fdcd31aaca963b6d380"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105158436711
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 82, 'threshold': 50, 'total_amount': 37795850, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 81, 'first_seen': 1760285763, 'matching_hash': '839de208acaae015'}}}