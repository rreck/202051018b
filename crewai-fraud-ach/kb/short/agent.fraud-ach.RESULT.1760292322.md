```json
{
  "id": "a2bca4776c322edf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292322,
  "host_pid": "9e6742732c60:1",
  "hash": "14bd03aacd13988a64ecbbd6166bc5985e68c88764f4ae05f5a5f854d833d85f",
  "cid": "QmV114bd03aacd13988a64ecbbd6166bc5985e68c887",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292322,
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
      "evaluated_at": 1760292322
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
  "sig": "d1a4248f882af835e93b12224937e799463ada36fb9e638e6a90641e0f213ec3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591103574
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 195, 'threshold': 50, 'total_amount': 91216125, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 194, 'first_seen': 1760285763, 'matching_hash': 'b913753ac5280baa'}}}