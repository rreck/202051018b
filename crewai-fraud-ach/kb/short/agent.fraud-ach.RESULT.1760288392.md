```json
{
  "id": "0bd4289e01d99f0b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288392,
  "host_pid": "9e6742732c60:1",
  "hash": "f73dd791c8796f0bb8e74f3c95acf936c5fef299f59073bd40f55a5b147dcbc1",
  "cid": "QmV1f73dd791c8796f0bb8e74f3c95acf936c5fef299",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288392,
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
      "evaluated_at": 1760288392
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
  "sig": "dfdca1c03050fe81fddba5abbfdfd5cbcbe092a7d56637616b9f0518dd4365fe"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 121000245827798
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 92, 'threshold': 50, 'total_amount': 46000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 91, 'first_seen': 1760285763, 'matching_hash': '00b0e4c8ffd2abdb'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}