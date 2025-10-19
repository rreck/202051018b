```json
{
  "id": "d5e77816b9a48753",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291228,
  "host_pid": "9e6742732c60:1",
  "hash": "cdf40e1e42f76adf426391f46390b332e0e06e9b313083305a8ddd2dfcdaa999",
  "cid": "QmV1cdf40e1e42f76adf426391f46390b332e0e06e9b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291228,
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
      "evaluated_at": 1760291228
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
  "sig": "434d5851b3af91e9cf32fe29335ab583e269a25edc29b3337e6121ba9c43f48b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000033750281
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 170, 'threshold': 50, 'total_amount': 67146260, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 169, 'first_seen': 1760285764, 'matching_hash': '57e27cf175445fc0'}}}