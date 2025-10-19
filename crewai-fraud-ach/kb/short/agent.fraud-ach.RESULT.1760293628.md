```json
{
  "id": "faee5a65418ae9af",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293628,
  "host_pid": "9e6742732c60:1",
  "hash": "7be7b38db041bfafd0d5d505bcffecd9bef0a15070861a2c8258eea05b596aa2",
  "cid": "QmV17be7b38db041bfafd0d5d505bcffecd9bef0a150",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293628,
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
      "evaluated_at": 1760293628
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
  "sig": "140ccd4e605db73564f1d79346cb75d4aa9768d5b8dfbe243f3f27c84c93e815"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034053694
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 222, 'threshold': 50, 'total_amount': 11899644, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 221, 'first_seen': 1760285765, 'matching_hash': 'f3f5d61420936f73'}}}