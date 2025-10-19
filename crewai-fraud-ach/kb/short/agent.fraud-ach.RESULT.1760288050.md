```json
{
  "id": "a47203682c39a883",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288050,
  "host_pid": "9e6742732c60:1",
  "hash": "4d0c5444fd7d519fdb033456dd6c1b7ae696d953eeead38f0ec49df4a89daff2",
  "cid": "QmV14d0c5444fd7d519fdb033456dd6c1b7ae696d953",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288050,
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
      "evaluated_at": 1760288050
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
  "sig": "d6a1d5c3e374e4c420aff6c015c41befbe32c92a8074aab67d2e3ad163170a3e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244875332
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 81, 'threshold': 50, 'total_amount': 26580717, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 80, 'first_seen': 1760285763, 'matching_hash': '627c737035c8c8c8'}}}