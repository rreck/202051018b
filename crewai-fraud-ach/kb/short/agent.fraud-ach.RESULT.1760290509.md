```json
{
  "id": "078965da0847c852",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290509,
  "host_pid": "9e6742732c60:1",
  "hash": "93eb8b3362e01eb43c7913d75cfa5a531e144848e5a17b38d0f2849cbb48491e",
  "cid": "QmV193eb8b3362e01eb43c7913d75cfa5a531e144848",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290509,
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
      "evaluated_at": 1760290509
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
  "sig": "ac4feac980081427b2895801d34d80b6af83ec899140e7c0d0769a58cf8711aa"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462094881
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 152, 'threshold': 50, 'total_amount': 72475120, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 151, 'first_seen': 1760285763, 'matching_hash': '1dac8a668721a731'}}}