```json
{
  "id": "ff32a385e298d45e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288884,
  "host_pid": "9e6742732c60:1",
  "hash": "1c7ee538066adb24944d21e52b98d4972c133f28826f11fee3833d119dc6e306",
  "cid": "QmV11c7ee538066adb24944d21e52b98d4972c133f28",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288884,
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
      "evaluated_at": 1760288884
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
  "sig": "69e5edd5d99b38bb3d2bc14b4c2f70e4c5bbeb7939292428670f171df756f3e4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000026865262
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 107, 'threshold': 50, 'total_amount': 52402287, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 106, 'first_seen': 1760285763, 'matching_hash': 'acc989ae5f5d7052'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}