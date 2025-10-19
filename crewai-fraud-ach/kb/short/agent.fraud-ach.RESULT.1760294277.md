```json
{
  "id": "f7f64afc61b9b1e1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294277,
  "host_pid": "9e6742732c60:1",
  "hash": "10787c2aaf4c2f2988efb14f6cb9185ef912a8fdca17d292a31407a11579c408",
  "cid": "QmV110787c2aaf4c2f2988efb14f6cb9185ef912a8fd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294277,
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
      "evaluated_at": 1760294277
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
  "sig": "bc347c20d86a131d2fd921bef7c79fed6e3830ea783ac9c75dfd3c0e13a1bac1"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 121000245827798
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 235, 'threshold': 50, 'total_amount': 117500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 234, 'first_seen': 1760285763, 'matching_hash': '00b0e4c8ffd2abdb'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}outing number checksum'}}}