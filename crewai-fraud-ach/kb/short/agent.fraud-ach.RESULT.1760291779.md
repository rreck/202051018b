```json
{
  "id": "1687c21458d7be20",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291779,
  "host_pid": "9e6742732c60:1",
  "hash": "c5b9d3d37c64a5b4c6f19235aaee1face238b6c3dd9fcc1073537bad6a6db846",
  "cid": "QmV1c5b9d3d37c64a5b4c6f19235aaee1face238b6c3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291779,
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
      "evaluated_at": 1760291779
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
  "sig": "d4d6c303c52704316730fb9a149f85e87f1be1e167bd299575ebf6ae2721cc7d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022915367
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 183, 'threshold': 50, 'total_amount': 76084995, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 182, 'first_seen': 1760285763, 'matching_hash': '4fdfaefd2437a484'}}}