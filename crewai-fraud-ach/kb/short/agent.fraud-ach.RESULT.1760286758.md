```json
{
  "id": "f583b425ab67d4fc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286758,
  "host_pid": "9e6742732c60:1",
  "hash": "eb7e865d8c65cbfef6498072388c90be8a7311a61d61e2adb5716dada15d01b4",
  "cid": "QmV1eb7e865d8c65cbfef6498072388c90be8a7311a6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286758,
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
      "evaluated_at": 1760286758
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
  "sig": "bf9f2bc860df6266928bc4ed0496d4c1853ad31f151306beeb3dee82a05eee5a"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009597785743
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 35, 'first_seen': 1760285765, 'matching_hash': 'c11d2019f761950d'}}}ue, 'risk_score': 85, 'details': {'duplicate_count': 35, 'first_seen': 1760285763, 'matching_hash': 'd8ced4219e23835b'}}}