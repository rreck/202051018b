```json
{
  "id": "318554798335964c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290982,
  "host_pid": "9e6742732c60:1",
  "hash": "e614068df29fe4b9afdd03c89a290f2d8c69f0cfc98eeb697d27c1289474d8ee",
  "cid": "QmV1e614068df29fe4b9afdd03c89a290f2d8c69f0cf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290982,
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
      "evaluated_at": 1760290982
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
  "sig": "0ea9c7b088f5ff33c2c2234cda468c04158a303148095d3ba0bb49189b3c08ba"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244206130
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 164, 'threshold': 50, 'total_amount': 15541460, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 163, 'first_seen': 1760285764, 'matching_hash': '13fbcd8431ec0e21'}}}