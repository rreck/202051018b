```json
{
  "id": "1519f572129d9e04",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291219,
  "host_pid": "9e6742732c60:1",
  "hash": "590ef02ffd1ee2cea7a3adac6b862414b461c95cf03ba7494926cc68f60aeb51",
  "cid": "QmV1590ef02ffd1ee2cea7a3adac6b862414b461c95c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291219,
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
      "evaluated_at": 1760291219
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
  "sig": "19d4c7db978abd27115f9b554baf279f7920068ac06b5748b6b0a4fcfb6f8135"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 031201467541453
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 170, 'threshold': 50, 'total_amount': 85000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 169, 'first_seen': 1760285763, 'matching_hash': '2d82340c3dc0e840'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}