```json
{
  "id": "2a7a72e2213bb42a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293360,
  "host_pid": "9e6742732c60:1",
  "hash": "964b9b2733941aa5221636c0f84eb574fed7e37ea1ad3435d364d1f5d6a4d468",
  "cid": "QmV1964b9b2733941aa5221636c0f84eb574fed7e37e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293360,
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
      "evaluated_at": 1760293361
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
  "sig": "70107c92d4d7ee32a826cc30fb14afa95b3fbf2009362f3c682e6cc009d4e21a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000247162231
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 217, 'threshold': 50, 'total_amount': 59920427, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 216, 'first_seen': 1760285763, 'matching_hash': '92769f469bceb512'}}}