```json
{
  "id": "ddf3e52f54d0a24b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285852,
  "host_pid": "9e6742732c60:1",
  "hash": "69a6389f4195ef32557d3b3363b86b21a38b8b1c8c33045f885d1b2fef075012",
  "cid": "QmV169a6389f4195ef32557d3b3363b86b21a38b8b1c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285852,
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
      "evaluated_at": 1760285852
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
  "sig": "15ade15040b86f2db4b110a8e0a95bd6fe75d72e2f74b2deea486a06afd18031"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 063100274128098
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 4, 'first_seen': 1760285765, 'matching_hash': 'e67ed82943972fb3'}}}