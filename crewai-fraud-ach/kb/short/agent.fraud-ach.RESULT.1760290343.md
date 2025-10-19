```json
{
  "id": "930bfe0927596981",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290343,
  "host_pid": "9e6742732c60:1",
  "hash": "65cfbe00fee026ed113ae5ffff7853850cc04428dad98820c0547016b4c2dadc",
  "cid": "QmV165cfbe00fee026ed113ae5ffff7853850cc04428",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290343,
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
      "evaluated_at": 1760290343
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
  "sig": "58ebd8cc1e58159f9598b2d2271b9b9c8d4f3b114220160b6f255d2dcadab357"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022025451
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 148, 'threshold': 50, 'total_amount': 69329860, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 147, 'first_seen': 1760285763, 'matching_hash': '147c6cadc877e9f2'}}}