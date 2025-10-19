```json
{
  "id": "0e2e404bcebe3933",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290010,
  "host_pid": "9e6742732c60:1",
  "hash": "18cc2536e2cd1e47d3dccfb84fc13f7e3b46f204ab384e234f4b84eb4fda7c9c",
  "cid": "QmV118cc2536e2cd1e47d3dccfb84fc13f7e3b46f204",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290010,
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
      "evaluated_at": 1760290010
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
  "sig": "abd461f10d423eec76dc31d6ca1c491b751a91e209f81922659e9305e9851316"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150046055
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 139, 'threshold': 50, 'total_amount': 54637981, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 138, 'first_seen': 1760285764, 'matching_hash': 'b44312efb353b904'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}