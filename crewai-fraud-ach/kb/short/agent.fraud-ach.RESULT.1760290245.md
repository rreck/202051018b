```json
{
  "id": "c6c7f9ae26c21daf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290245,
  "host_pid": "9e6742732c60:1",
  "hash": "ccca2700ebdb7f068745c12c8dbba9d73ac2545f828c4b3bcfc39bb3b9d838e8",
  "cid": "QmV1ccca2700ebdb7f068745c12c8dbba9d73ac2545f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290245,
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
      "evaluated_at": 1760290245
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
  "sig": "afbb7eb0078fd4a35fc62756774e7e8519ba7e10daff3071ebf4ee5edf2e7829"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 044000033820068
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 145, 'threshold': 50, 'total_amount': 72500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 144, 'first_seen': 1760285763, 'matching_hash': 'f27958456f681c61'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}