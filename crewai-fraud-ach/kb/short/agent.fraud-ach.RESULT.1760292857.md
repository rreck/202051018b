```json
{
  "id": "f5cfaedc54800612",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292857,
  "host_pid": "9e6742732c60:1",
  "hash": "a012f450ed1c86c15936ab86b016f767a10188c03472354de92276e7e4290a7d",
  "cid": "QmV1a012f450ed1c86c15936ab86b016f767a10188c0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292857,
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
      "evaluated_at": 1760292857
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
  "sig": "236c5325f0a9e65436954e4a7cd75c06b6e763a81cfb8391de205239e5f7da58"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593711033
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 206, 'threshold': 50, 'total_amount': 56983102, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 205, 'first_seen': 1760285765, 'matching_hash': 'a63e704272eccc25'}}}