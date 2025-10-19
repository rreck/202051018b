```json
{
  "id": "6a856649899081c0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292268,
  "host_pid": "9e6742732c60:1",
  "hash": "4e128ea409e63cff9f4309c3bd24c7fa7cb97f08e775d6345828c5642bebb78c",
  "cid": "QmV14e128ea409e63cff9f4309c3bd24c7fa7cb97f08",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292268,
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
      "evaluated_at": 1760292268
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
  "sig": "3ba204523474305dd4b657af082b6d31f7d946b486aaeec948cee996dbf35eeb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465033668
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 194, 'threshold': 50, 'total_amount': 88295996, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 193, 'first_seen': 1760285763, 'matching_hash': '0c3b43b3004009ec'}}}