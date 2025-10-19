```json
{
  "id": "f53ee291266eb74d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286431,
  "host_pid": "9e6742732c60:1",
  "hash": "7a2b83c2979e4cc9404049758079dd490176afa9c90a04bcf8ccc2ee0e1f1811",
  "cid": "QmV17a2b83c2979e4cc9404049758079dd490176afa9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286431,
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
      "evaluated_at": 1760286431
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
  "sig": "1ed21e798bfddfac5bf929c95dacaed8dde7382f31053dadb4692b98178909e4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153716353
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 101, 'threshold': 50, 'total_amount': 16009813, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 100, 'first_seen': 1760284979, 'matching_hash': '4e18e54a79e9d8ab'}}}