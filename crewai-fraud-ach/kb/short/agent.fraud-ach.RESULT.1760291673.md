```json
{
  "id": "09a0935999da26d2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291673,
  "host_pid": "9e6742732c60:1",
  "hash": "b45aaee4aa01b8e3c35077243f1961668ccfd3ec3b93475a7433ed62a0450314",
  "cid": "QmV1b45aaee4aa01b8e3c35077243f1961668ccfd3ec",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291673,
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
      "evaluated_at": 1760291673
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
  "sig": "a89f05642a9476bb90ad77395d8c36871fa80a472d5655aff15ef0d07f4a1a59"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000033751291
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 180, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 179, 'first_seen': 1760285765, 'matching_hash': '04859aaf1143bd8f'}}}