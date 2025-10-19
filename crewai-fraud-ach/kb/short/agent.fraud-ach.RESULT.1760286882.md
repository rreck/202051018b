```json
{
  "id": "741d354c60b75807",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286882,
  "host_pid": "9e6742732c60:1",
  "hash": "63ddecd008352d28f79a1532f5c3001bb38de940343388438e9bc8598bfdb924",
  "cid": "QmV163ddecd008352d28f79a1532f5c3001bb38de940",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286882,
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
      "evaluated_at": 1760286882
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "0a4f9067210c7e82b00b0d9a53b3e2b23b23d959ec0d3c059ae63bf6fc8b9f9b"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 12729920, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 39, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}