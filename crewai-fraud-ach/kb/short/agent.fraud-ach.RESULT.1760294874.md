```json
{
  "id": "eb13f0c57d64f1ca",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294874,
  "host_pid": "9e6742732c60:1",
  "hash": "fdd3354c8bd206e026c433e641328fad236cb1d847b75f82a1df0e0b666ad82e",
  "cid": "QmV1fdd3354c8bd206e026c433e641328fad236cb1d8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294874,
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
      "evaluated_at": 1760294874
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "amount_anomaly",
    "risk_critical"
  ],
  "sig": "e1201b3f151a91fb6940a76b3d4e5c23b95aa7a1a14d2856e3ebd78fcc94d6db"
}
```

Fraud detected: amount_anomaly (score: 86)
Transaction: 021000029420003
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 246, 'threshold': 50, 'total_amount': 1624232220, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 245, 'first_seen': 1760285764, 'matching_hash': '37b4044b8dabc650'}}, 'amount_anomaly': {'fraud_detected': True, 'risk_score': 73, 'details': {'zscore': 3.35, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 6602570}}}