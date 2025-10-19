```json
{
  "id": "7c2aba5b588c4b8d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287590,
  "host_pid": "9e6742732c60:1",
  "hash": "18c80e340223f0ed2e03f76c024824a9af7299c0baec6346f71f93eedf5fb4b8",
  "cid": "QmV118c80e340223f0ed2e03f76c024824a9af7299c0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287590,
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
      "evaluated_at": 1760287590
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
  "sig": "4a11284ffbd87ceaae0137139e65fe4e317d648f3be8d03f9cf74b54f4d3302f"
}
```

Fraud detected: duplicate_transaction (score: 82)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 80, 'details': {'transaction_count': 65, 'threshold': 50, 'total_amount': 20686120, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 64, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}