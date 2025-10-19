```json
{
  "id": "7016276ac743dbec",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293101,
  "host_pid": "9e6742732c60:1",
  "hash": "0ce3cf3f57bcff827f5bbdeefb12441c4949b57162f6b1803ceb33651edcdf84",
  "cid": "QmV10ce3cf3f57bcff827f5bbdeefb12441c4949b571",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293101,
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
      "evaluated_at": 1760293101
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
  "sig": "8ef908bf032e545aefb5b723d57c684aa4db1003f4ea888d3a3d92525a38b3c2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000249254910
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 211, 'threshold': 50, 'total_amount': 24095778, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 210, 'first_seen': 1760285765, 'matching_hash': '80dc97a16e454830'}}}