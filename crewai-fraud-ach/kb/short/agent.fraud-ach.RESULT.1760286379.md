```json
{
  "id": "90734deb7cb50275",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286379,
  "host_pid": "9e6742732c60:1",
  "hash": "2020cf7c5588598a2103d7a42a005c014a5e30edae39a72944a3e002b003bb43",
  "cid": "QmV12020cf7c5588598a2103d7a42a005c014a5e30ed",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286379,
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
      "evaluated_at": 1760286379
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "round_amount_pattern",
    "risk_high"
  ],
  "sig": "a483032fc31f5e0277fe778629144859e588c1c3e7ffeeb7a9526cb3362503e8"
}
```

Fraud detected: round_amount_pattern (score: 65)
Transaction: 021000023602502
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 23000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 22, 'first_seen': 1760285765, 'matching_hash': 'eacad8d3d1630a37'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}