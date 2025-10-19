```json
{
  "id": "dfd47450a1a0bafc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286316,
  "host_pid": "9e6742732c60:1",
  "hash": "a2c001cb59cef2f300620bfcd82448dc303f1f8941c9455b5c08541cde97117c",
  "cid": "QmV1a2c001cb59cef2f300620bfcd82448dc303f1f89",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286316,
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
      "evaluated_at": 1760286316
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
  "sig": "c60511f672984c1fb5d2b9fdcd2357fd36f4df41330275f5fea7bce0d0e74ac2"
}
```

Fraud detected: round_amount_pattern (score: 65)
Transaction: 026009597287610
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 21000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 20, 'first_seen': 1760285765, 'matching_hash': 'd127b5f232f25796'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}