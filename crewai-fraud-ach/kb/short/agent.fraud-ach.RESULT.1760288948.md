```json
{
  "id": "15e2ef6278ec782a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288948,
  "host_pid": "9e6742732c60:1",
  "hash": "30d93e846668b124bf6644c6b83d8a6dfcf14672e551406a7981af83798dd437",
  "cid": "QmV130d93e846668b124bf6644c6b83d8a6dfcf14672",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288948,
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
      "evaluated_at": 1760288948
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
  "sig": "e05a665e43b480745acbf6650437553d3f3f8732fd159d22899d5f812705a3d0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027960877
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 109, 'threshold': 50, 'total_amount': 35515252, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 108, 'first_seen': 1760285763, 'matching_hash': '750facc395053d7c'}}}