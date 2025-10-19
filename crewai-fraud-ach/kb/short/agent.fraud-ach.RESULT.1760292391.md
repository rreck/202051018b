```json
{
  "id": "187b5c3e4b0300c2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292391,
  "host_pid": "9e6742732c60:1",
  "hash": "63036944e27c9cb451accff6a9831de8539d4f78107521a77e6624efc1302a6b",
  "cid": "QmV163036944e27c9cb451accff6a9831de8539d4f78",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292391,
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
      "evaluated_at": 1760292391
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
  "sig": "3f90d4ce29af33ea8290413060f24e26a5e89328bc6ddfc677cbb831f73a826c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 196, 'threshold': 50, 'total_amount': 62376608, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 195, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}