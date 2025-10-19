```json
{
  "id": "045d74a895db26b0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292988,
  "host_pid": "9e6742732c60:1",
  "hash": "50cca29c522e7002d424936bb08cff37015b160dda0da6f443a1f84fbefb0851",
  "cid": "QmV150cca29c522e7002d424936bb08cff37015b160d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292988,
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
      "evaluated_at": 1760292988
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
  "sig": "bd31cf1981c43da5cf666b8577205d159a2122fa34c4b051027381b5f1977658"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100270009801
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 209, 'threshold': 50, 'total_amount': 101135727, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 208, 'first_seen': 1760285763, 'matching_hash': '0a6cdd943232be17'}}}