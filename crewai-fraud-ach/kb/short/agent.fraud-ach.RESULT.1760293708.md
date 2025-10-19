```json
{
  "id": "0bb865fd4309c7d2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293708,
  "host_pid": "9e6742732c60:1",
  "hash": "a141f049e0bf69e232bdc244e962157be78401a86b15bc39e2f83392cf30d3bd",
  "cid": "QmV1a141f049e0bf69e232bdc244e962157be78401a8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293708,
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
      "evaluated_at": 1760293708
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
  "sig": "303ab9e5e7419c32ff070e1e8c59d752a1028b482dbf1b07d03ce2dd50693b65"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025820321
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 224, 'threshold': 50, 'total_amount': 57751232, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 223, 'first_seen': 1760285763, 'matching_hash': 'cf65bb25527720c5'}}}