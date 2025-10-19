```json
{
  "id": "5f1e753c59d647af",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293887,
  "host_pid": "9e6742732c60:1",
  "hash": "8d804355e8a74086f914c54e723560699d906b8666e550356afe26278ff46aee",
  "cid": "QmV18d804355e8a74086f914c54e723560699d906b86",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293887,
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
      "evaluated_at": 1760293887
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
  "sig": "51d81d64d1a949fdf766bbb7e2da26e662ba0269cd7c53d75120f1634502824d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460625527
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 227, 'threshold': 50, 'total_amount': 108998590, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 226, 'first_seen': 1760285765, 'matching_hash': 'd2e448c8360c8b26'}}}