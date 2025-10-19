```json
{
  "id": "e0737f4e53121436",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288080,
  "host_pid": "9e6742732c60:1",
  "hash": "69b28a52c700b2477ad352479c388cb5464b58ededceadb643f62d9fb21ff982",
  "cid": "QmV169b28a52c700b2477ad352479c388cb5464b58ed",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288080,
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
      "evaluated_at": 1760288080
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
  "sig": "3c3f9c2e4b1ae3d70c96a143670b81193153656d2944fe576f4c3624586b6028"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 121000245827798
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 82, 'threshold': 50, 'total_amount': 41000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 81, 'first_seen': 1760285763, 'matching_hash': '00b0e4c8ffd2abdb'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}