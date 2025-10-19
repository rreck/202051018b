```json
{
  "id": "235fd0e563662e1e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292899,
  "host_pid": "9e6742732c60:1",
  "hash": "919ee0863757232c5e64ee7776fe90725469e594cb7972baee700ef2fc7f412b",
  "cid": "QmV1919ee0863757232c5e64ee7776fe90725469e594",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292899,
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
      "evaluated_at": 1760292899
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
  "sig": "42dea7f5e293431ce256b77e0a272eec257c14cf2909e2914d9be489adcbaaa4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034778259
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 207, 'threshold': 50, 'total_amount': 37662408, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 206, 'first_seen': 1760285763, 'matching_hash': 'b6b775805828fc60'}}}