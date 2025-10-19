```json
{
  "id": "edcc6d3826a876df",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292968,
  "host_pid": "9e6742732c60:1",
  "hash": "8d56d36b9685b8ac7c7bbd3e589b49179c46606f4b7a4eec92fa31b744c6ee6f",
  "cid": "QmV18d56d36b9685b8ac7c7bbd3e589b49179c46606f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292968,
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
      "evaluated_at": 1760292968
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
  "sig": "cdb0d62574412c13f5c53970575b20ad8f88949fca59c4012e8d83dfcc78befe"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599553408
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 209, 'threshold': 50, 'total_amount': 24943314, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 208, 'first_seen': 1760285763, 'matching_hash': '67e91645ed6012ef'}}}