```json
{
  "id": "b8f1800c6a622878",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288962,
  "host_pid": "9e6742732c60:1",
  "hash": "dec6ab40f652e660792fd44bc2bf40e2aa3009049b57a9c2ce1b3c144088eb4f",
  "cid": "QmV1dec6ab40f652e660792fd44bc2bf40e2aa300904",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288962,
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
      "evaluated_at": 1760288962
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
  "sig": "0c6ae8dbb7f80da1de59aea2794cb381825d9a8c235b51dbcdece49959428817"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241561723
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 109, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 108, 'first_seen': 1760285764, 'matching_hash': '61d0611cbf39c4a3'}}}