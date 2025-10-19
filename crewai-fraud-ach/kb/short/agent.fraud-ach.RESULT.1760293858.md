```json
{
  "id": "6491b87c2d7181ed",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293858,
  "host_pid": "9e6742732c60:1",
  "hash": "a1653288385e9ff2d73a35319ff8965e43012658991ce746537c73d0160c49fb",
  "cid": "QmV1a1653288385e9ff2d73a35319ff8965e43012658",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293858,
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
      "evaluated_at": 1760293858
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
  "sig": "52be9d1f040d3de9e717fbab2d572486d82963c077f577aeb1fbb4955fa4caf3"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105157761036
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 227, 'threshold': 50, 'total_amount': 17362322, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 226, 'first_seen': 1760285763, 'matching_hash': '6f087e4012bb31a6'}}}maly': {'fraud_detected': True, 'risk_score': 72, 'details': {'zscore': 3.28, 'mean': 719465.7956361999, 'stdev': 1757513.5850259534, 'iqr_bounds': {'lower': -194591.0, 'upper': 788265.0}, 'amount': 6478434}}}