```json
{
  "id": "f013d51a21d33bae",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286180,
  "host_pid": "9e6742732c60:1",
  "hash": "9dcd7670b0ac6b32d983e9d0cb74ee611a7b3682063a660f0413545505f59bf3",
  "cid": "QmV19dcd7670b0ac6b32d983e9d0cb74ee611a7b3682",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286180,
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
      "evaluated_at": 1760286180
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
  "sig": "ddeb9a274ed305f5e197b83fecfc5bd3a8bdd7ceb5469faa850f578ff44bfe2d"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000024762963
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 16, 'first_seen': 1760285764, 'matching_hash': 'dd3a0eba0797b423'}}}