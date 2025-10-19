```json
{
  "id": "d405a56aea15bb22",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288048,
  "host_pid": "9e6742732c60:1",
  "hash": "f6f57ab6cd8a3d8b7a5f1f561d18c7b670b0483c71c0a58a2da2766ee6bde009",
  "cid": "QmV1f6f57ab6cd8a3d8b7a5f1f561d18c7b670b0483c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288048,
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
      "evaluated_at": 1760288048
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
  "sig": "e2e770ce75876c8dcee29e820c1f7fc96d46a93698f9c177e80f72db6d99f7f6"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 026009594828050
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 81, 'threshold': 50, 'total_amount': 81000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 80, 'first_seen': 1760285763, 'matching_hash': '3e77f188c48013ab'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}