```json
{
  "id": "4365efecde17172a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287492,
  "host_pid": "9e6742732c60:1",
  "hash": "11739f886f22483f9f87b8f03a7a2548ee6ad1d47e052fa04b8dc6e9f0967f21",
  "cid": "QmV111739f886f22483f9f87b8f03a7a2548ee6ad1d4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287492,
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
      "evaluated_at": 1760287492
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "2e2464e913f4764b3f3f2344835adf8aded958c817eb8181d3b8607f196a387f"
}
```

Fraud detected: duplicate_transaction (score: 79)
Transaction: 021000022401094
Details: {'velocity': {'fraud_detected': True, 'risk_score': 74, 'details': {'transaction_count': 62, 'threshold': 50, 'total_amount': 25307966, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 61, 'first_seen': 1760285763, 'matching_hash': '4e5cfda15432477b'}}}