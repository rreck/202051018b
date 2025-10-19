```json
{
  "id": "3549500dfcf9b5da",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290048,
  "host_pid": "9e6742732c60:1",
  "hash": "4085e73be57ed769eb4444e4586a484ed2597131083e8cbb8239432b8d76f48e",
  "cid": "QmV14085e73be57ed769eb4444e4586a484ed2597131",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290048,
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
      "evaluated_at": 1760290048
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
  "sig": "500b899044d29803cf3d3b8356e76a372714f3468f70d91e05425ac3480902ad"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243741176
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 140, 'threshold': 50, 'total_amount': 42604100, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 139, 'first_seen': 1760285763, 'matching_hash': 'e78a513bf0bcec2f'}}}