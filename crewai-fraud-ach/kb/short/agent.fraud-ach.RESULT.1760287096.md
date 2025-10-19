```json
{
  "id": "ef3ef6d25f119189",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287096,
  "host_pid": "9e6742732c60:1",
  "hash": "e3b13d42969fb493c9307acbc813320c95753c7a15a01ad97c61928d3c0e724d",
  "cid": "QmV1e3b13d42969fb493c9307acbc813320c95753c7a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287096,
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
      "evaluated_at": 1760287096
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
  "sig": "e7885f9c36ad0e17f1dc274f8e59409716692be7e82f54632d898e6717317a50"
}
```

Fraud detected: round_amount_pattern (score: 65)
Transaction: 122105152842303
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 24000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 47, 'first_seen': 1760285764, 'matching_hash': 'f130ef58b190a1ab'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}