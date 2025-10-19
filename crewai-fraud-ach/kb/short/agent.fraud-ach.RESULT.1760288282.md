```json
{
  "id": "31923a07526a9804",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288282,
  "host_pid": "9e6742732c60:1",
  "hash": "49fd49a8a22690cff53cbcb428b238d8ea5a1684a07604838956196c18abad6a",
  "cid": "QmV149fd49a8a22690cff53cbcb428b238d8ea5a1684",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288282,
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
      "evaluated_at": 1760288282
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
  "sig": "0bfa08db5502bc758d87df879f7de744662d5eb1326c57c68f2c196ddd83648e"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 111000026431469
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 88, 'threshold': 50, 'total_amount': 88000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 87, 'first_seen': 1760285765, 'matching_hash': '51112ae34069fd52'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}