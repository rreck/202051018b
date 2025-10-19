```json
{
  "id": "fd905412745b83b9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285918,
  "host_pid": "9e6742732c60:1",
  "hash": "226e36831ffd0a6f2011c5675d33b9bcf6e00117a8ee7faee2bd19aac4835519",
  "cid": "QmV1226e36831ffd0a6f2011c5675d33b9bcf6e00117",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285918,
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
      "evaluated_at": 1760285918
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
  "sig": "51c1228eec0f5eb2f366f249791ee11f60ab39b8ee860c7f0447aeb93a08fa49"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000023759733
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 7, 'first_seen': 1760285765, 'matching_hash': 'cdd972b8484ef71b'}}}: 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 83, 'first_seen': 1760284979, 'matching_hash': 'fdbb68f6e232305a'}}}