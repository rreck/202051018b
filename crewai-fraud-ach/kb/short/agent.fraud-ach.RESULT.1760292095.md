```json
{
  "id": "ca841e9173d13b8e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292095,
  "host_pid": "9e6742732c60:1",
  "hash": "9ece384c835bdb52afff5380f8a96bc95e97729acb6c03a6367e64b4305d7522",
  "cid": "QmV19ece384c835bdb52afff5380f8a96bc95e97729a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292095,
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
      "evaluated_at": 1760292095
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
  "sig": "f421df5b0fef960c1e7c18b86ac46bc0ddcaca4ba5b2207a6062019cfa25f032"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465580268
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 190, 'threshold': 50, 'total_amount': 60030310, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 189, 'first_seen': 1760285764, 'matching_hash': 'af9caaaec8320bfb'}}}