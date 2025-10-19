```json
{
  "id": "1cb1d3785bb7b6c3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293854,
  "host_pid": "9e6742732c60:1",
  "hash": "aca52e289188de0190ab7076eec2b7663c5dcb32ad2affc477fe0fecaf745019",
  "cid": "QmV1aca52e289188de0190ab7076eec2b7663c5dcb32",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293854,
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
      "evaluated_at": 1760293854
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
  "sig": "89341e408490d72a35f4eb34892089e2bc3dae5390a1c6040426f89fbd27c2f1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243162678
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 227, 'threshold': 50, 'total_amount': 17604985, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 226, 'first_seen': 1760285763, 'matching_hash': '6908b8eed250a93e'}}}