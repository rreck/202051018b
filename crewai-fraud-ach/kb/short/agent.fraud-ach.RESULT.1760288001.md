```json
{
  "id": "9c6351ff95866a3b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288001,
  "host_pid": "9e6742732c60:1",
  "hash": "ecb983505e2807ad98cf6245acccd9c863a884db74db0bb85501596490ebf8ad",
  "cid": "QmV1ecb983505e2807ad98cf6245acccd9c863a884db",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288001,
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
      "evaluated_at": 1760288001
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
  "sig": "36d567a3873e630dc2b48f7e02bc366fb70d74495c8fdc9a362471792e6e083c"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 121000248309566
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 79, 'threshold': 50, 'total_amount': 79000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 78, 'first_seen': 1760285765, 'matching_hash': '25ac79dd28618198'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}