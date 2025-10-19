```json
{
  "id": "11a3424e204062f3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294271,
  "host_pid": "9e6742732c60:1",
  "hash": "25899abd6def55c4fd935963c2c765e46aa249f99f61c8a64ae1f60c4ba455a4",
  "cid": "QmV125899abd6def55c4fd935963c2c765e46aa249f9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294271,
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
      "evaluated_at": 1760294271
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
  "sig": "9234f9949db7eab80340950d6d5a8fb87f946a055468a68a23cba88940664ef2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244516225
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 235, 'threshold': 50, 'total_amount': 34456875, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 234, 'first_seen': 1760285763, 'matching_hash': '305c81c4ba1c9c62'}}}maly': {'fraud_detected': True, 'risk_score': 84, 'details': {'zscore': 4.45, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 8542478}}}