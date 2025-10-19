```json
{
  "id": "9b3a1cab1ec40faf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287158,
  "host_pid": "9e6742732c60:1",
  "hash": "fce26b1e2d06c040d950fc4ef44a3aa0e4aac078385c2d59dd27f09fbe8977b0",
  "cid": "QmV1fce26b1e2d06c040d950fc4ef44a3aa0e4aac078",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287158,
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
      "evaluated_at": 1760287158
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
  "sig": "6559018e6dbbc9c467ddb5103cb50ffd2d0a820907089765934dce7ae800b602"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105155616727
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 49, 'first_seen': 1760285765, 'matching_hash': 'b26c49bc45dba458'}}}k_score': 85, 'details': {'duplicate_count': 49, 'first_seen': 1760285763, 'matching_hash': '2178be3eb8984b5a'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '491975133', 'validation_error': 'Invalid routing number checksum'}}}