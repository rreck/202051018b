```json
{
  "id": "f2ece70fa40c330c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287666,
  "host_pid": "9e6742732c60:1",
  "hash": "51b7ef8ed0d30038072a074043522d185f8ec124bebc8e465873c1c413be1be5",
  "cid": "QmV151b7ef8ed0d30038072a074043522d185f8ec124",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287666,
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
      "evaluated_at": 1760287666
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
  "sig": "43787caee35acea15b910a0a41c8d1768c35f1841c72c3041ed30d6cbfff457a"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 063100271240415
Details: {'velocity': {'fraud_detected': True, 'risk_score': 86, 'details': {'transaction_count': 68, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 67, 'first_seen': 1760285765, 'matching_hash': '8c20097da64de4ba'}}}een': 1760285763, 'matching_hash': '760b7e67ac1502b4'}}}