```json
{
  "id": "b980996ea3b9c61d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287464,
  "host_pid": "9e6742732c60:1",
  "hash": "2218cc3fd44fb880b1f086ca11135a6103b324b2208373019fb16f869b8af77b",
  "cid": "QmV12218cc3fd44fb880b1f086ca11135a6103b324b2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287464,
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
      "evaluated_at": 1760287464
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
  "sig": "a35cc6b3d55c47a76443b7026f2d33688c986acf188270762ae82a2cdb2b4fd1"
}
```

Fraud detected: round_amount_pattern (score: 65)
Transaction: 122105159813222
Details: {'velocity': {'fraud_detected': True, 'risk_score': 72, 'details': {'transaction_count': 61, 'threshold': 50, 'total_amount': 30500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 60, 'first_seen': 1760285764, 'matching_hash': 'b185e366ced12ee8'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}