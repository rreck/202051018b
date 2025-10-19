```json
{
  "id": "c6d46dfe800780d2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286560,
  "host_pid": "9e6742732c60:1",
  "hash": "f8a52169f6dacdf15bbebc940dbc05aa770c87a5df6e48b04e5bfdf4c823faa9",
  "cid": "QmV1f8a52169f6dacdf15bbebc940dbc05aa770c87a5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286560,
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
      "evaluated_at": 1760286560
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
  "sig": "9c1e2b8eeca36b59502881212bf931b1e9c403f7e18707df2828212bccc31845"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 063100273461392
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 10344068, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 28, 'first_seen': 1760285765, 'matching_hash': 'ee78248c8d3d65fe'}}}