```json
{
  "id": "6e06b5f0e681719c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292907,
  "host_pid": "9e6742732c60:1",
  "hash": "a713578a17fbc892fbedfce669ba1a2ee7bb2b1d9608feff1f42459fedde5c4b",
  "cid": "QmV1a713578a17fbc892fbedfce669ba1a2ee7bb2b1d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292907,
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
      "evaluated_at": 1760292907
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
  "sig": "ed7f55134b923218b5d96b6a759ee7348475a97ba284c348f5ad31a4d9d06402"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465822757
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 207, 'threshold': 50, 'total_amount': 93708693, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 206, 'first_seen': 1760285765, 'matching_hash': '1a67314a077331d2'}}}