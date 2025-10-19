```json
{
  "id": "2e3f13687a8d8a89",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290013,
  "host_pid": "9e6742732c60:1",
  "hash": "ff15e12a01b28c6308aa576a9ad5f1f4d6d6ea0084e187908058eda5a40865fb",
  "cid": "QmV1ff15e12a01b28c6308aa576a9ad5f1f4d6d6ea00",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290013,
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
      "evaluated_at": 1760290013
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
  "sig": "4ecf9c3ac441335b7d9370aff23b7384bb14f36669d7ec73ce239842ff575ee0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270776467
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 139, 'threshold': 50, 'total_amount': 67955988, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 138, 'first_seen': 1760285763, 'matching_hash': 'a0c66d95a4fd4e21'}}}