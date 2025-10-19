```json
{
  "id": "1c3ccb7e3207424e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293031,
  "host_pid": "9e6742732c60:1",
  "hash": "7501390d2441fb15f228e86101ee18b210c3d9d2fc4acd92fb047d1e35b041bd",
  "cid": "QmV17501390d2441fb15f228e86101ee18b210c3d9d2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293031,
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
      "evaluated_at": 1760293031
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
  "sig": "bcd82e0dac1caf90306c15a9c41062cf14b9ab80d6ca664971a53d26c5704c96"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153838694
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 210, 'threshold': 50, 'total_amount': 76040160, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 209, 'first_seen': 1760285763, 'matching_hash': '9b5298dfc7691fa1'}}}