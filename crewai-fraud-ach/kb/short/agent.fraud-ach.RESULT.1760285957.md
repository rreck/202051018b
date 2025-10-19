```json
{
  "id": "6299b058bcad62a9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285957,
  "host_pid": "9e6742732c60:1",
  "hash": "7a111561fbaa177da718c1f7ba0d1919c7a17330299a2268f36ed400da64615a",
  "cid": "QmV17a111561fbaa177da718c1f7ba0d1919c7a17330",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285957,
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
      "evaluated_at": 1760285957
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
  "sig": "377d19e1f2abf9fffd814d0ca8fb34f9e3e135a3d75d53f73ed2145a7d52ea3d"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105156608425
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 8, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}